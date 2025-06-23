def explain_design_decisions():
    return '''
    This solution pulls forward SOFR 1M rates from Pensford, cleans them, and loads them into SQLite for easy API querying.
    The API then allows clients to project loan rates under constraints like floors, ceilings, and spreads.
    We've modularized config/constants for cleaner code and easier updates.
    With more time, we’d improve observability, error handling, and testing.
    '''