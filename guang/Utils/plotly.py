import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np


class Subplots:
    def __init__(self, rows=1, cols=1, **kwargs):
        self.rows = rows
        self.cols = cols
        x_title = kwargs.get('x_title', 'x_title')
        y_title = kwargs.get('y_title', 'y_title')
        self.fig = make_subplots(rows=rows, cols=cols, x_title=x_title, y_title=y_title)
        self.count = 0

    def plot(self, x, y, **kwargs):
        '''
        Params:
            label: look like matplotlib's legend
            mode: 'lines', 'markers', 'lines+markers', 'text'

        '''
        label = kwargs.get('label', self.count + 1)
        mode = kwargs.get('mode', 'lines')  #
        row, col = np.divmod(self.count, self.cols)
        row, col = int(row + 1), int(col + 1)

        self.fig.add_trace(go.Scatter(x=x, y=y, mode=mode, name=label), row=row, col=col)

        self.count += 1

    def show(self, *args, **kwargs):
        self.fig.show(*args, **kwargs)


class Multiplots:
    def __init__(self, **kwargs):
        #         self.title = 'title'
        self.title = 'fig.title'
        self.fig = go.Figure()
        self.x_label = 'fig.x_label'
        self.y_label = 'fig.y_label'
        self.count = 0
        self.annotations = []

    def plot(self, *args, **kwargs):
        '''
        Params:
            :param label: look like matplotlib's legend.
            :param mode: 'lines'(default), 'markers', 'lines+markers', 'text'
            :param line_width: corresponding lines mode.
            :param marker_size: corresponding of markers mode.
            :param text: hovering text
        '''
        if (len(args) >1 and type(args[0]) != type(args[1])) or len(args)==1:
            y = args[0]
            x = np.arange(len(y))
        else:
            y = args[1]
            x = args[0]

        label = kwargs.get('label', self.count + 1)
        mode = kwargs.get('mode', 'lines')  #
        line_width = kwargs.get('line_width', None)
        marker_size = kwargs.get('marker_size', None)
        text = kwargs.get('text', f'f(x)')
        self.fig.add_trace(go.Scatter(x=x, y=y,
                                      mode=mode,
                                      name=label,
                                      text=text,
                                      marker_line_width=line_width,
                                      marker_size=marker_size))
        self.count += 1

    def show(self, *args, **kwargs):
        self.annotations.append(dict(xref='paper', yref='paper', x=0.0, y=1.05,  # title
                                     xanchor='left', yanchor='bottom',
                                     text=self.title,
                                     font=dict(family='Arial',
                                               size=30,
                                               color='rgb(37,37,37)'),
                                     showarrow=False))
        #
        self.annotations.append(dict(xref='paper', yref='paper', x=0.5, y=-0.1,  # X axis
                                     xanchor='center', yanchor='top',
                                     text=self.x_label,
                                     font=dict(family='Arial',
                                               size=15,
                                               color='rgb(150,150,150)'),
                                     showarrow=False))

        self.fig.update_layout(
            # title=f'{self.title:}',
            overwrite=False,

            yaxis=dict(
                title=self.y_label,
                showgrid=True,

                zeroline=False,
                showline=True,
                showticklabels=True,),

            xaxis=dict(
                # title=self.x_label,
                showline=True,
                showgrid=True,
                showticklabels=True,
                linecolor='rgb(204, 204, 204)',
                linewidth=2,
                ticks='outside',
                tickfont=dict(
                    family='Arial',
                    size=12,
                    color='rgb(82, 82, 82)'),
                        ),
            annotations=self.annotations
        )
        self.fig.show(*args, **kwargs)