from langchain_core.tools import tool

@tool
def get_officer_name(comp_symbol: str) -> str:
    """
    Lấy tên lãnh đạo hội đồng quản trị.
    
    Args:
        comp_symbol: Tên viết tắt của công ty.
    """
    company = Vnstock().stock(symbol=comp_symbol, source='TCBS').company
    return list(company.officers()['officer_name'])
@tool
def get_sub_comp(comp_symbol: str) -> str:
    """
    Lấy tên công ty con thuộc tập đoàn.
    
    Args:
        comp_symbol: Tên viết tắt của công ty.
    """
    company = Vnstock().stock(symbol=comp_symbol, source='TCBS').company
    list_of_sub = list(company.subsidiaries()['sub_company_name'])
    x = ",".join(list_of_sub)
    return f"{{\"sub_comp\": '{x}'}}"

@tool
def get_price_stock(symbol: str, time: str) -> str:
    """
    Kiểm tra giá chứng khoán.
    
    Args:
        symbol: Tên viết tắt của công ty.
        time: Thời gian cần kiểm tra, định dạng YYYY-MM-DD hoặc ISO 8601.
    """
    stock = Vnstock().stock(symbol=symbol, source='VCI')
    df = stock.quote.history(start='2024-01-01', end='2024-06-21', interval='1D')
    row_of_price = df[df['time'] == time].iloc[:, 1:5]
    list_of_price = row_of_price.values.tolist()[0]
    label = ['mở phiên', "cao điểm", "đáy", "đóng phiên"]
    dictionary = dict(zip(label, list_of_price))
    return f"{{\"price\": {dictionary}}}"

@tool
def list_of_securites(symbol: str) -> str:
    """
    Danh sách tất cả các mã chứng khoán niêm yết.
    
    Args:
        symbol: Tên viết tắt của công ty.
    """
    stock = Vnstock().stock(symbol=symbol, source='VCI')
    df = stock.listing.all_symbols()
    return df

@tool
def list_of_stock_according_to_stock_exchange(symbol: str) -> str:
    """
    Liệt kê mã cổ phần theo sàn.
    
    Args:
        symbol: Tên viết tắt của công ty.
    """
    stock = Vnstock().stock(symbol=symbol, source='VCI')
    df = stock.listing.symbols_by_exchange()
    return df

@tool
def list_of_stock_according_to_industry(symbol: str) -> str:
    """
    Liệt kê mã cổ phần theo ngành icb.
    
    Args:
        symbol: Tên viết tắt của công ty.
    """
    stock = Vnstock().stock(symbol=symbol, source='VCI')
    df = stock.listing.symbols_by_industry()
    return df

@tool
def list_of_stock_according_to_group(symbol: str, group_code: str) -> str:
    """
    Liệt kê danh sách mã cổ phần theo nhóm.
    
    Args:
        symbol: Tên viết tắt của công ty.
        group_code: Mã nhóm.
    """
    stock = Vnstock().stock(symbol=symbol, source='VCI')
    df = stock.listing.symbols_by_group(group_code)
    return df

@tool
def list_of_industries_icb(symbol: str) -> str:
    """
    Danh sách mã ngành theo mã icb.
    
    Args:
        symbol: Tên viết tắt của công ty.
    """
    stock = Vnstock().stock(symbol=symbol, source='VCI')
    df = stock.listing.industries_icb()
    return df

@tool
def intraday_quote(symbol: str) -> str:
    """
    Dữ liệu khớp lệnh trong ngày giao dịch realtime hoặc ngày gần nhất (ngoài giờ giao dịch).
    
    Args:
        symbol: Tên viết tắt của công ty.
    """
    stock = Vnstock().stock(symbol=symbol, source='VCI')
    df = stock.quote.intraday(symbol=symbol, show_log=False)
    return df

@tool
def price_step_and_volume(symbol: str) -> str:
    """
    Bước giá và khối lượng giao dịch: realtime.
    
    Args:
        symbol: Tên viết tắt của công ty.
    """
    stock = Vnstock().stock(symbol=symbol, source='VCI')
    df = stock.quote.price_depth(symbol=symbol)
    return df

@tool
def price_board(symbol: str, symbol_list: list) -> str:
    """
    Bảng giá realtime.
    
    Args:
        symbol: Tên viết tắt của công ty.
        symbol_list: Danh sách các mã chứng khoán.
    """
    stock = Vnstock().stock(symbol=symbol, source='VCI')
    df = stock.trading.price_board(symbol_list)
    return df

@tool
def company_overview(symbol: str) -> str:
    """
    Thông tin tổng quan công ty.
    
    Args:
        symbol: Tên viết tắt của công ty.
    """
    company = Vnstock().stock(symbol=symbol, source='TSCB').company
    df = company.overview()
    return df

@tool
def company_profile(symbol: str) -> str:
    """
    Hồ sơ công ty.
    
    Args:
        symbol: Tên viết tắt của công ty.
    """
    company = Vnstock().stock(symbol=symbol, source='TSCB').company
    df = company.profile()
    return df

@tool
def company_shareholders(symbol: str) -> str:
    """
    Cổ đông của công ty.
    
    Args:
        symbol: Tên viết tắt của công ty.
    """
    company = Vnstock().stock(symbol=symbol, source='TSCB').company
    df = company.shareholders()
    return df

@tool
def insider_deals(symbol: str) -> str:
    """
    Giao dịch nội bộ công ty.
    
    Args:
        symbol: Tên viết tắt của công ty.
    """
    company = Vnstock().stock(symbol=symbol, source='TSCB').company
    df = company.insider_deals()
    return df

@tool
def events(symbol: str) -> str:
    """
    Sự kiện của công ty.
    
    Args:
        symbol: Tên viết tắt của công ty.
    """
    company = Vnstock().stock(symbol=symbol, source='TSCB').company
    df = company.events()
    return df

@tool
def news(symbol: str) -> str:
    """
    Tin tức của công ty.
    
    Args:
        symbol: Tên viết tắt của công ty.
    """
    company = Vnstock().stock(symbol=symbol, source='TSCB').company
    df = company.news()
    return df

@tool
def dividends(symbol: str) -> str:
    """
    Cổ tức của công ty.
    
    Args:
        symbol: Tên viết tắt của công ty.
    """
    company = Vnstock().stock(symbol=symbol, source='TSCB').company
    df = company.dividends()
    return df

@tool
def balance_sheet(symbol: str, period: str, yearReport: str) -> str:
    """
    Bảng cân đối kế toán.
    
    Args:
        symbol: Tên viết tắt của công ty.
        period: Chu kì theo quý hoặc năm.
        yearReport: Năm báo cáo.
    """
    stock = Vnstock().stock(symbol=symbol, source='VCI')
    df = stock.finance.balance_sheet(period=period, lang='vi')
    df = df[df['Năm'] == yearReport]
    return df

@tool
def income_statement(symbol: str, period: str, yearReport: str) -> str:
    """
    Bảng báo cáo lãi lỗ.
    
    Args:
        symbol: Tên viết tắt của công ty.
        period: Chu kì theo quý hoặc năm.
        yearReport: Năm báo cáo.
    """
    stock = Vnstock().stock(symbol=symbol, source='VCI')
    df = stock.finance.income_statement(period=period, lang='vi')
    df = df[df['Năm'] == yearReport]
    return df

@tool
def cash_flow(symbol: str, period: str, yearReport: str) -> str:
    """
    Báo cáo lưu chuyển tiền tệ.
    
    Args:
        symbol: Tên viết tắt của công ty.
        period: Chu kì theo quý hoặc năm.
        yearReport: Năm báo cáo.
    """
    stock = Vnstock().stock(symbol=symbol, source='VCI')
    df = stock.finance.cash_flow(period=period, lang='vi')
    df = df[df['Năm'] == yearReport]
    return df

@tool
def ratio(symbol: str, period: str, yearReport: str) -> str:
    """
    Chỉ số tài chính.
    
    Args:
        symbol: Tên viết tắt của công ty.
        period: Chu kì theo quý hoặc năm.
        yearReport: Năm báo cáo.
    """
    stock = Vnstock().stock(symbol=symbol, source='VCI')
    df = stock.finance.ratio(period=period, lang='vi')
    df = df[df['Meta']['Năm'] == yearReport]
    return df

tools = [
    get_officer_name,
    get_sub_comp,
    get_price_stock,
    list_of_securites,
    list_of_stock_according_to_stock_exchange,
    list_of_stock_according_to_industry,
    list_of_stock_according_to_group,
    list_of_industries_icb,
    intraday_quote,
    price_step_and_volume,
    price_board,
    company_overview,
    company_profile,
    company_shareholders,
    insider_deals,
    events,
    news,
    dividends,
    balance_sheet,
    income_statement,
    cash_flow,
    ratio
]