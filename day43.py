def amount_of_pages(summary):
    pages = ""
    
    page = 1
    while len(pages) < summary:
        pages += str(page)
        
        page += 1
        
    return page - 1