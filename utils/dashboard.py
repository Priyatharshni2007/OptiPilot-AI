import plotly.graph_objects as go



def create_bar():

    fig = go.Figure()

    fig.add_trace(
        go.Bar(
            x=[
                "Time Saving",
                "Cost Reduction",
                "Efficiency"
            ],
            y=[
                80,
                50,
                70
            ]
        )
    )


    fig.update_layout(
        title="Predicted Business Impact"
    )

    return fig
    