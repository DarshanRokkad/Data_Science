from bokeh.plotting import figure, show
from bokeh.models import Slider, CustomJS, ColumnDataSource
from bokeh.layouts import column
from bokeh.io import curdoc

# Create a data source
my_source = ColumnDataSource(data={'x': [1, 2, 3, 6], 'y': [4, 6, 1, 3], 'color': ['blue', 'green', 'red', 'yellow']})

# Create a figure
p = figure(width=400, height=400, title="Interactive Bokeh Plot")
circle = p.circle('x', 'y', size=20, color='color', source=my_source)

# Create a slider widget
my_slider = Slider(start=0, end=3, value=0, step=1, title="Choose Color")

# Define JavaScript callback to update circle color
callback = CustomJS(args=dict(source=my_source, slider=my_slider), code="""
    const data = source.data;
    const color = data.color;
    const selected_color_index = slider.value;

    for (let i = 0; i < color.length; i++) {
        // Define an array of available colors
        const availableColors = ['blue', 'green', 'red', 'yellow'];
        
        // Set the color for each data point based on the slider value
        color[i] = availableColors[selected_color_index];
    }

    source.change.emit();
""")

# Attach the callback to the slider widget
my_slider.js_on_change('value', callback)

# Create a layout using Column
layout = column(p, my_slider)

# Add the layout to the current document
curdoc().add_root(layout)


# To run the code -> bokeh serve Assignment-22_Q4.py
# Open in browser -> http://localhost:5006/Assignment-22_Q4