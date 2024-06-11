import justpy as jp

def app():
    wp = jp.QuasarPage()
    h1 = jp.QDiv(a=wp, text="Analysis of Course Reviews", classes="text-h3 text-right q-pa-md")
    p1 =jp.QDiv(a=wp, text="These graphs represents course review analysis", classes="")

    return wp

jp.justpy(app)