def FeatureEngineering(data):
    
    prompt:str = f"""
    Create new features or derive meaningful information from existing features to improve the quality and usefulness of the dataset. : \n {data}
    """
    
    return (prompt)

def OneHotEncoding(data):
    
    prompt:str = f"""
    Look through the dataset and encode categorical variables as you see fit: \n {data}
    """
    
    return (prompt)