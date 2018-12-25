import webbrowser

new = 2
query = raw_input("Enter Search Term: ")
tabUrl = "https://www.google.co.in/search?q="+query+"&source=lnms&tbm=isch"
webbrowser.open(tabUrl)
