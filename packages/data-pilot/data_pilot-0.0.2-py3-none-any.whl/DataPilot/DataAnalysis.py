def DataAnalysis(data):
    
    prompt:str = f"""
    I want you to act as a data analyst and take the data that is being provided to you and provide a well-rounded analysis in return.\n Data that is being provided to you can be of many types for example, it can be data from stock market APIs, or data from CRMs and HRMs etc. \n Data sources can be of many types of databases of web scraping dumbs such as SQL, NoSQL databases. \n Here is the data that you have to analyze : \n {data}
    """
    
    return (prompt)