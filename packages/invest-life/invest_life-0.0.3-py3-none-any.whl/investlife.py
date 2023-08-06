# -*- coding: utf-8 -*-

import requests, json
import pickle

# url
base_url = 'https://investlife.cn/data/'

# token
g_token = None

# 设置token
def set_token(user_token):
    global g_token
    g_token = user_token

def get_stock_list(listed_state = None, fields = None):
    headers = {'Content-Type': 'application/json', 'token': g_token}
    url = base_url + 'get_stock_list'
    param = {'listed_state': listed_state, 'fields': fields}

    res = requests.post(url=url, headers=headers, data=json.dumps(param))

    if res.ok:
        return pickle.loads(res.content)

    raise Exception(res.text)

def get_trading_calendar(secu_market = None, if_trading_day = None, if_week_end = None, if_month_end = None, start_date = None, end_date = None, fields = None):
    headers = {'Content-Type': 'application/json', 'token': g_token}
    url = base_url + 'get_trading_calendar'

    param = {'secu_market': secu_market, 'if_trading_day': if_trading_day, 'if_week_end': if_week_end, 'if_month_end': if_month_end, 'start_date': start_date, 'end_date': end_date, 'fields': fields}

    res = requests.post(url=url, headers=headers, data=json.dumps(param))

    if res.ok:
        return pickle.loads(res.content)

    raise Exception(res.text)

def get_ipo_list(start_date = None, secu_market = None, listed_sector = None, fields = None):
    headers = {'Content-Type': 'application/json', 'token': g_token}
    url = base_url + 'get_ipo_list'

    param = {'start_date': start_date, 'secu_market': secu_market, 'listed_sector': listed_sector, 'fields': fields}

    res = requests.post(url=url, headers=headers, data=json.dumps(param))

    if res.ok:
        return pickle.loads(res.content)

    raise Exception(res.text)

def get_company_profile(en_prod_code = None, fields = None):
    headers = {'Content-Type': 'application/json', 'token': g_token}
    url = base_url + 'get_company_profile'

    param = {'en_prod_code': en_prod_code, 'fields': fields}

    res = requests.post(url=url, headers=headers, data=json.dumps(param))

    if res.ok:
        return pickle.loads(res.content)

    raise Exception(res.text)

def get_stock_Info(en_prod_code = None, trading_date = None, fields = None):
    headers = {'Content-Type': 'application/json', 'token': g_token}
    url = base_url + 'get_stock_Info'

    param = {'en_prod_code': en_prod_code, 'trading_date': trading_date, 'fields': fields}

    res = requests.post(url=url, headers=headers, data=json.dumps(param))

    if res.ok:
        return pickle.loads(res.content)

    raise Exception(res.text)

def get_leader_profile(secu_code = None, position_type = None, fields = None):
    headers = {'Content-Type': 'application/json', 'token': g_token}
    url = base_url + 'get_leader_profile'

    param = {'secu_code': secu_code, 'position_type': position_type, 'fields': fields}

    res = requests.post(url=url, headers=headers, data=json.dumps(param))

    if res.ok:
        return pickle.loads(res.content)

    raise Exception(res.text)

def get_st_stock_list(secu_market = None, secu_category = None, listed_sector = None, fields = None):
    headers = {'Content-Type': 'application/json', 'token': g_token}
    url = base_url + 'get_st_stock_list'

    param = {'secu_market': secu_market, 'secu_category': secu_category, 'listed_sector': listed_sector, 'fields': fields}

    res = requests.post(url=url, headers=headers, data=json.dumps(param))

    if res.ok:
        return pickle.loads(res.content)

    raise Exception(res.text)

def get_shszhk_stock_list(etfcomponent_type = None, fields = None):
    headers = {'Content-Type': 'application/json', 'token': g_token}
    url = base_url + 'get_shszhk_stock_list'

    param = {'etfcomponent_type': etfcomponent_type, 'fields': fields}

    res = requests.post(url=url, headers=headers, data=json.dumps(param))

    if res.ok:
        return pickle.loads(res.content)

    return res.text

def get_stock_quote_daily(en_prod_code = None, trading_date = None, adjust_way = 0, fields = None):
    headers = {'Content-Type': 'application/json', 'token': g_token}
    url = base_url + 'get_stock_quote_daily'

    param = {'en_prod_code': en_prod_code, 'trading_date': trading_date, 'adjust_way': adjust_way, 'fields': fields}

    res = requests.post(url=url, headers=headers, data=json.dumps(param))

    if res.ok:
        return pickle.loads(res.content)

    return res.text

def get_stock_quote_weekly(en_prod_code = None, trading_date = None, adjust_way = 0, fields = None):
    headers = {'Content-Type': 'application/json', 'token': g_token}
    url = base_url + 'get_stock_quote_weekly'

    param = {'en_prod_code': en_prod_code, 'trading_date': trading_date, 'adjust_way': adjust_way, 'fields': fields}

    res = requests.post(url=url, headers=headers, data=json.dumps(param))

    if res.ok:
        return pickle.loads(res.content)

    return res.text

def get_stock_quote_monthly(en_prod_code = None, trading_date = None, adjust_way = 0, fields = None):
    headers = {'Content-Type': 'application/json', 'token': g_token}
    url = base_url + 'get_stock_quote_monthly'

    param = {'en_prod_code': en_prod_code, 'trading_date': trading_date, 'adjust_way': adjust_way, 'fields': fields}

    res = requests.post(url=url, headers=headers, data=json.dumps(param))

    if res.ok:
        return pickle.loads(res.content)

    return res.text

def get_stock_quote_yearly(en_prod_code = None, trading_date = None, adjust_way = 0, fields = None):
    headers = {'Content-Type': 'application/json', 'token': g_token}
    url = base_url + 'get_stock_quote_yearly'

    param = {'en_prod_code': en_prod_code, 'trading_date': trading_date, 'adjust_way': adjust_way, 'fields': fields}

    res = requests.post(url=url, headers=headers, data=json.dumps(param))

    if res.ok:
        return pickle.loads(res.content)

    return res.text

def get_money_flow(en_prod_code = None, trading_date = None, fields = None):
    headers = {'Content-Type': 'application/json', 'token': g_token}
    url = base_url + 'get_money_flow'

    param = {'en_prod_code': en_prod_code, 'trading_date': trading_date, 'fields': fields}

    res = requests.post(url=url, headers=headers, data=json.dumps(param))

    if res.ok:
        return pickle.loads(res.content)

    return res.text

def get_suspension_list(en_prod_code = None, trading_date = None, fields = None):
    headers = {'Content-Type': 'application/json', 'token': g_token}
    url = base_url + 'get_suspension_list'

    param = {'en_prod_code': en_prod_code, 'trading_date': trading_date, 'fields': fields}

    res = requests.post(url=url, headers=headers, data=json.dumps(param))

    if res.ok:
        return pickle.loads(res.content)

    return res.text

def get_shareholder_top10(secu_code = None, start_date = None, end_date = None, fields = None):
    headers = {'Content-Type': 'application/json', 'token': g_token}
    url = base_url + 'get_shareholder_top10'

    param = {'secu_code': secu_code, 'start_date': start_date, 'end_date': end_date, 'fields': fields}

    res = requests.post(url=url, headers=headers, data=json.dumps(param))

    if res.ok:
        return pickle.loads(res.content)

    return res.text

def get_float_shareholder_top10(secu_code = None, start_date = None, end_date = None, fields = None):
    headers = {'Content-Type': 'application/json', 'token': g_token}
    url = base_url + 'get_float_shareholder_top10'

    param = {'secu_code': secu_code, 'start_date': start_date, 'end_date': end_date, 'fields': fields}

    res = requests.post(url=url, headers=headers, data=json.dumps(param))

    if res.ok:
        return pickle.loads(res.content)

    return res.text

def get_lh_daily(trading_day = None, fields = None):
    headers = {'Content-Type': 'application/json', 'token': g_token}
    url = base_url + 'get_lh_daily'

    param = {'trading_day': trading_day, 'fields': fields}

    res = requests.post(url=url, headers=headers, data=json.dumps(param))

    if res.ok:
        return pickle.loads(res.content)

    return res.text

def get_lh_stock(secu_code = None, trading_day = None, fields = None):
    headers = {'Content-Type': 'application/json', 'token': g_token}
    url = base_url + 'get_lh_stock'

    param = {'secu_code': secu_code, 'trading_day': trading_day, 'fields': fields}

    res = requests.post(url=url, headers=headers, data=json.dumps(param))

    if res.ok:
        return pickle.loads(res.content)

    return res.text

def get_stock_quote_minutes(en_prod_code = None, begin_date = None, end_date = None, fields = None):
    headers = {'Content-Type': 'application/json', 'token': g_token}
    url = base_url + 'get_stock_quote_minutes'

    param = {'en_prod_code': en_prod_code, 'begin_date': begin_date, 'end_date': end_date, 'fields': fields}

    res = requests.post(url=url, headers=headers, data=json.dumps(param))

    if res.ok:
        return pickle.loads(res.content)

    return res.text

def get_shszhk_capitalflow(exchange_kind = None, start_date = None, end_date = None, fields = None):
    headers = {'Content-Type': 'application/json', 'token': g_token}
    url = base_url + 'get_shszhk_capitalflow'

    param = {'exchange_kind': exchange_kind, 'start_date': start_date, 'end_date': end_date, 'fields': fields}

    res = requests.post(url=url, headers=headers, data=json.dumps(param))

    if res.ok:
        return pickle.loads(res.content)

    return res.text
    
def get_shszhk_deal_top10(exchange_kind = None, start_date = None, end_date = None, fields = None):
    headers = {'Content-Type': 'application/json', 'token': g_token}
    url = base_url + 'get_shszhk_deal_top10'

    param = {'exchange_kind': exchange_kind, 'start_date': start_date, 'end_date': end_date, 'fields': fields}

    res = requests.post(url=url, headers=headers, data=json.dumps(param))

    if res.ok:
        return pickle.loads(res.content)

    return res.text

def get_shszhk_distribution(exchange_kind = None, start_date = None, end_date = None, fields = None):
    headers = {'Content-Type': 'application/json', 'token': g_token}
    url = base_url + 'get_shszhk_distribution'

    param = {'exchange_kind': exchange_kind, 'start_date': start_date, 'end_date': end_date, 'fields': fields}

    res = requests.post(url=url, headers=headers, data=json.dumps(param))

    if res.ok:
        return pickle.loads(res.content)

    return res.text

def get_shszhk_change_top10(exchange_kind = None, trading_data = None, fields = None):
    headers = {'Content-Type': 'application/json', 'token': g_token}
    url = base_url + 'get_shszhk_change_top10'

    param = {'exchange_kind': exchange_kind, 'trading_data': trading_data, 'fields': fields}

    res = requests.post(url=url, headers=headers, data=json.dumps(param))

    if res.ok:
        return pickle.loads(res.content)

    return res.text

def get_quote_stocklist(fields = None):
    headers = {'Content-Type': 'application/json', 'token': g_token}
    url = base_url + 'get_quote_stocklist'

    param = {'fields': fields}

    res = requests.post(url=url, headers=headers, data=json.dumps(param))

    if res.ok:
        return pickle.loads(res.content)

    return res.text

def get_stock_quote_daily_list(en_prod_code = None, begin_date = None, end_date = None, adjust_way = None):
    headers = {'Content-Type': 'application/json', 'token': g_token}
    url = base_url + 'get_stock_quote_daily_list'

    param = {'en_prod_code': en_prod_code, 'begin_date': begin_date, 'end_date': end_date, 'adjust_way': adjust_way}

    res = requests.post(url=url, headers=headers, data=json.dumps(param))

    if res.ok:
        return pickle.loads(res.content)

    return res.text

def get_index_quote(en_prod_code = None, trading_date = None):
    headers = {'Content-Type': 'application/json', 'token': g_token}
    url = base_url + 'get_index_quote'

    param = {'en_prod_code': en_prod_code, 'trading_date': trading_date}

    res = requests.post(url=url, headers=headers, data=json.dumps(param))

    if res.ok:
        return pickle.loads(res.content)

    return res.text

def get_industry_category(en_prod_code = None, level = 0, fields = None):
    headers = {'Content-Type': 'application/json', 'token': g_token}
    url = base_url + 'get_industry_category'

    param = {'en_prod_code': en_prod_code, 'level': level, 'fields': fields}

    res = requests.post(url=url, headers=headers, data=json.dumps(param))

    if res.ok:
        return pickle.loads(res.content)

    return res.text

def get_index_constituent(index_stock_code = None, fields = None):
    headers = {'Content-Type': 'application/json', 'token': g_token}
    url = base_url + 'get_index_constituent'

    param = {'index_stock_code': index_stock_code, 'fields': fields}

    res = requests.post(url=url, headers=headers, data=json.dumps(param))

    if res.ok:
        return pickle.loads(res.content)

    return res.text

def get_org_hold(secu_code = None, org_type = None, end_date = None, fields = None):
    headers = {'Content-Type': 'application/json', 'token': g_token}
    url = base_url + 'get_org_hold'

    param = {'secu_code': secu_code, 'org_type': org_type, 'end_date': end_date, 'fields': fields}

    res = requests.post(url=url, headers=headers, data=json.dumps(param))

    if res.ok:
        return pickle.loads(res.content)

    return res.text

def get_holder_num(en_prod_code = None, report_date = None, fields = None):
    headers = {'Content-Type': 'application/json', 'token': g_token}
    url = base_url + 'get_holder_num'

    param = {'en_prod_code': en_prod_code, 'report_date': report_date, 'fields': fields}

    res = requests.post(url=url, headers=headers, data=json.dumps(param))

    if res.ok:
        return pickle.loads(res.content)

    return res.text

def get_restricted_schedule(en_prod_code = None, trading_date = None, query_direction = None, fields = None):
    headers = {'Content-Type': 'application/json', 'token': g_token}
    url = base_url + 'get_restricted_schedule'

    param = {'en_prod_code': en_prod_code, 'trading_date': trading_date, 'query_direction': query_direction, 'fields': fields}

    res = requests.post(url=url, headers=headers, data=json.dumps(param))

    if res.ok:
        return pickle.loads(res.content)

    return res.text

def get_holder_pledge(en_prod_code = None, trading_date = None, serial_number = None, fields = None):
    headers = {'Content-Type': 'application/json', 'token': g_token}
    url = base_url + 'get_holder_pledge'

    param = {'en_prod_code': en_prod_code, 'trading_date': trading_date, 'serial_number': serial_number, 'fields': fields}

    res = requests.post(url=url, headers=headers, data=json.dumps(param))

    if res.ok:
        return pickle.loads(res.content)

    return res.text

def get_holder_increase(date_type = None, symbols = None, listed_sector = None, secu_market = None, share_holder_type = None, state_type = None, start_date = None, end_date = None, fields = None):
    headers = {'Content-Type': 'application/json', 'token': g_token}
    url = base_url + 'get_holder_increase'

    param = {'date_type': date_type, 'symbols': symbols, 'listed_sector': listed_sector, 'secu_market': secu_market, 'share_holder_type': share_holder_type, 'state_type': state_type, 'start_date': start_date, 'end_date': end_date, 'fields': fields}

    res = requests.post(url=url, headers=headers, data=json.dumps(param))

    if res.ok:
        return pickle.loads(res.content)

    return res.text

def get_pledge_repo(secu_code = None, end_date = None, fields = None):
    headers = {'Content-Type': 'application/json', 'token': g_token}
    url = base_url + 'get_pledge_repo'

    param = {'secu_code': secu_code, 'end_date': end_date, 'fields': fields}

    res = requests.post(url=url, headers=headers, data=json.dumps(param))

    if res.ok:
        return pickle.loads(res.content)

    return res.text

def get_stock_pledge(secu_code = None, start_date = None, end_date = None, fields = None):
    headers = {'Content-Type': 'application/json', 'token': g_token}
    url = base_url + 'get_stock_pledge'

    param = {'secu_code': secu_code, 'start_date': start_date, 'end_date': end_date, 'fields': fields}

    res = requests.post(url=url, headers=headers, data=json.dumps(param))

    if res.ok:
        return pickle.loads(res.content)

    return res.text

def get_block_trade(secu_code = None, start_date = None, end_date = None, fields = None):
    headers = {'Content-Type': 'application/json', 'token': g_token}
    url = base_url + 'get_block_trade'

    param = {'secu_code': secu_code, 'start_date': start_date, 'end_date': end_date, 'fields': fields}

    res = requests.post(url=url, headers=headers, data=json.dumps(param))

    if res.ok:
        return pickle.loads(res.content)

    return res.text

def get_margin_trading(en_prod_code = None, trading_date = None, fields = None):
    headers = {'Content-Type': 'application/json', 'token': g_token}
    url = base_url + 'get_margin_trading'

    param = {'en_prod_code': en_prod_code, 'trading_date': trading_date, 'fields': fields}

    res = requests.post(url=url, headers=headers, data=json.dumps(param))

    if res.ok:
        return pickle.loads(res.content)

    return res.text

def get_interval_margin_trading(en_prod_code = None, begin_date = None, end_date = None, fields = None):
    headers = {'Content-Type': 'application/json', 'token': g_token}
    url = base_url + 'get_interval_margin_trading'

    param = {'en_prod_code': en_prod_code, 'begin_date': begin_date, 'end_date': end_date, 'fields': fields}

    res = requests.post(url=url, headers=headers, data=json.dumps(param))

    if res.ok:
        return pickle.loads(res.content)

    return res.text

def get_margin_trade_detail(symbols = None, date_type = None, start_date = None, end_date = None, fields = None):
    headers = {'Content-Type': 'application/json', 'token': g_token}
    url = base_url + 'get_margin_trade_detail'

    param = {'symbols': symbols, 'date_type': date_type, 'start_date': start_date, 'end_date': end_date, 'fields': fields}

    res = requests.post(url=url, headers=headers, data=json.dumps(param))

    if res.ok:
        return pickle.loads(res.content)

    return res.text

def get_margin_trade_total(date_type = None, start_date = None, end_date = None, fields = None):
    headers = {'Content-Type': 'application/json', 'token': g_token}
    url = base_url + 'get_margin_trade_total'

    param = {'date_type': date_type, 'start_date': start_date, 'end_date': end_date, 'fields': fields}

    res = requests.post(url=url, headers=headers, data=json.dumps(param))

    if res.ok:
        return pickle.loads(res.content)

    return res.text

def get_stock_dividend(en_prod_code = None, report_date = None, fields = None):
    headers = {'Content-Type': 'application/json', 'token': g_token}
    url = base_url + 'get_stock_dividend'

    param = {'en_prod_code': en_prod_code, 'report_date': report_date, 'fields': fields}

    res = requests.post(url=url, headers=headers, data=json.dumps(param))

    if res.ok:
        return pickle.loads(res.content)

    return res.text

def get_stock_additional(en_prod_code = None, year = None, issue_type = None, fields = None):
    headers = {'Content-Type': 'application/json', 'token': g_token}
    url = base_url + 'get_stock_additional'

    param = {'en_prod_code': en_prod_code, 'year': year, 'issue_type': issue_type, 'fields': fields}

    res = requests.post(url=url, headers=headers, data=json.dumps(param))

    if res.ok:
        return pickle.loads(res.content)

    return res.text

def get_stock_additional_all(en_prod_code = None, trading_date = None, spo_process = None, fields = None):
    headers = {'Content-Type': 'application/json', 'token': g_token}
    url = base_url + 'get_stock_additional_all'

    param = {'en_prod_code': en_prod_code, 'trading_date': trading_date, 'spo_process': spo_process, 'fields': fields}

    res = requests.post(url=url, headers=headers, data=json.dumps(param))

    if res.ok:
        return pickle.loads(res.content)

    return res.text

def get_stock_allotment(en_prod_code = None, year = None, fields = None):
    headers = {'Content-Type': 'application/json', 'token': g_token}
    url = base_url + 'get_stock_allotment'

    param = {'en_prod_code': en_prod_code, 'year': year, 'fields': fields}

    res = requests.post(url=url, headers=headers, data=json.dumps(param))

    if res.ok:
        return pickle.loads(res.content)

    return res.text

def get_stock_asforecastabb(secu_code = None, forcast_type = None, forecast_object = None, egrowth_rate_floor = None, fields = None):
    headers = {'Content-Type': 'application/json', 'token': g_token}
    url = base_url + 'get_stock_asforecastabb'

    param = {'secu_code': secu_code, 'forcast_type': forcast_type, 'forecast_object': forecast_object, 'egrowth_rate_floor': egrowth_rate_floor, 'fields': fields}

    res = requests.post(url=url, headers=headers, data=json.dumps(param))

    if res.ok:
        return pickle.loads(res.content)

    return res.text

def get_stock_asunderweight(secu_code = None, fields = None):
    headers = {'Content-Type': 'application/json', 'token': g_token}
    url = base_url + 'get_stock_asunderweight'

    param = {'secu_code': secu_code, 'fields': fields}

    res = requests.post(url=url, headers=headers, data=json.dumps(param))

    if res.ok:
        return pickle.loads(res.content)

    return res.text

def get_stock_asoverweight(secu_code = None, fields = None):
    headers = {'Content-Type': 'application/json', 'token': g_token}
    url = base_url + 'get_stock_asoverweight'

    param = {'secu_code': secu_code, 'fields': fields}

    res = requests.post(url=url, headers=headers, data=json.dumps(param))

    if res.ok:
        return pickle.loads(res.content)

    return res.text

def get_stock_asrighttransfer(secu_code = None, year = None, tran_mode = None, fields = None):
    headers = {'Content-Type': 'application/json', 'token': g_token}
    url = base_url + 'get_stock_asrighttransfer'

    param = {'secu_code': secu_code, 'year': year, 'tran_mode': tran_mode, 'fields': fields}

    res = requests.post(url=url, headers=headers, data=json.dumps(param))

    if res.ok:
        return pickle.loads(res.content)

    return res.text

def get_stock_asraising(tran_mode = None, fields = None):
    headers = {'Content-Type': 'application/json', 'token': g_token}
    url = base_url + 'get_stock_asraising'

    param = {'tran_mode': tran_mode, 'fields': fields}

    res = requests.post(url=url, headers=headers, data=json.dumps(param))

    if res.ok:
        return pickle.loads(res.content)

    return res.text

def get_stock_share_holders(en_prod_code = None, trading_date = None, unit = 0, fields = None):
    headers = {'Content-Type': 'application/json', 'token': g_token}
    url = base_url + 'get_stock_share_holders'

    param = {'en_prod_code': en_prod_code, 'trading_date': trading_date, 'unit': unit, 'fields': fields}

    res = requests.post(url=url, headers=headers, data=json.dumps(param))

    if res.ok:
        return pickle.loads(res.content)

    return res.text

def get_stock_special_tradedate(secu_code = None, start_date = None, end_date = None, special_trade_type = None, fields = None):
    headers = {'Content-Type': 'application/json', 'token': g_token}
    url = base_url + 'get_stock_special_tradedate'

    param = {'secu_code': secu_code, 'start_date': start_date, 'end_date': end_date, 'special_trade_type': special_trade_type, 'fields': fields}

    res = requests.post(url=url, headers=headers, data=json.dumps(param))

    if res.ok:
        return pickle.loads(res.content)

    return res.text

def get_stock_org_rate(secu_code = None, rate_type = None, start_date = None, end_date = None, fields = None):
    headers = {'Content-Type': 'application/json', 'token': g_token}
    url = base_url + 'get_stock_org_rate'

    param = {'secu_code': secu_code, 'rate_type': rate_type, 'start_date': start_date, 'end_date': end_date, 'fields': fields}

    res = requests.post(url=url, headers=headers, data=json.dumps(param))

    if res.ok:
        return pickle.loads(res.content)

    return res.text

def get_stock_org_rate_sum(date_type = None, secu_code = None, fields = None):
    headers = {'Content-Type': 'application/json', 'token': g_token}
    url = base_url + 'get_stock_org_rate_sum'

    param = {'date_type': date_type, 'secu_code': secu_code, 'fields': fields}

    res = requests.post(url=url, headers=headers, data=json.dumps(param))

    if res.ok:
        return pickle.loads(res.content)

    return res.text

def get_stock_investor_statistics(symbols = None, secu_market = None, listed_sector = None, start_date = None, end_date = None, event_id = None, fields = None):
    headers = {'Content-Type': 'application/json', 'token': g_token}
    url = base_url + 'get_stock_investor_statistics'

    param = {'symbols': symbols, 'secu_market': secu_market, 'listed_sector': listed_sector, 'start_date': start_date, 'end_date': end_date, 'event_id': event_id, 'fields': fields}

    res = requests.post(url=url, headers=headers, data=json.dumps(param))

    if res.ok:
        return pickle.loads(res.content)

    return res.text

def get_stock_investor_detail(symbols = None, secu_market = None, listed_sector = None, date_type = None, start_date = None, end_date = None, event_id = None, fields = None):
    headers = {'Content-Type': 'application/json', 'token': g_token}
    url = base_url + 'get_stock_investor_detail'

    param = {'symbols': symbols, 'secu_market': secu_market, 'listed_sector': listed_sector, 'date_type': date_type, 'start_date': start_date, 'end_date': end_date, 'event_id': event_id, 'fields': fields}

    res = requests.post(url=url, headers=headers, data=json.dumps(param))

    if res.ok:
        return pickle.loads(res.content)

    return res.text

def get_stock_financial_industry_list(secu_code = None, standard = None, first_industry_code = None, fields = None):
    headers = {'Content-Type': 'application/json', 'token': g_token}
    url = base_url + 'get_stock_financial_industry_list'

    param = {'secu_code': secu_code, 'standard': standard, 'first_industry_code': first_industry_code, 'fields': fields}

    res = requests.post(url=url, headers=headers, data=json.dumps(param))

    if res.ok:
        return pickle.loads(res.content)

    return res.text

def get_stock_industry_compare(secu_code = None, end_date = None, sort_field = None, sort_type = None, second_industry_code = None, fields = None):
    headers = {'Content-Type': 'application/json', 'token': g_token}
    url = base_url + 'get_stock_industry_compare'

    param = {'secu_code': secu_code, 'end_date': end_date, 'sort_field': sort_field, 'sort_type': sort_type, 'second_industry_code': second_industry_code, 'fields': fields}

    res = requests.post(url=url, headers=headers, data=json.dumps(param))

    if res.ok:
        return pickle.loads(res.content)

    return res.text

def get_stock_industry_avg(secu_code = None, second_industry_code = None, end_date = None, fields = None):
    headers = {'Content-Type': 'application/json', 'token': g_token}
    url = base_url + 'get_stock_industry_avg'

    param = {'secu_code': secu_code, 'second_industry_code': second_industry_code, 'end_date': end_date, 'fields': fields}

    res = requests.post(url=url, headers=headers, data=json.dumps(param))

    if res.ok:
        return pickle.loads(res.content)

    return res.text

def get_stock_industry_region_list(type = None, fields = None):
    headers = {'Content-Type': 'application/json', 'token': g_token}
    url = base_url + 'get_stock_industry_region_list'

    param = {'type': type, 'fields': fields}

    res = requests.post(url=url, headers=headers, data=json.dumps(param))

    if res.ok:
        return pickle.loads(res.content)

    return res.text

def get_schedule_disclosure(en_prod_code = None, report_date = None, fields = None):
    headers = {'Content-Type': 'application/json', 'token': g_token}
    url = base_url + 'get_schedule_disclosure'

    param = {'en_prod_code': en_prod_code, 'report_date': report_date, 'fields': fields}

    res = requests.post(url=url, headers=headers, data=json.dumps(param))

    if res.ok:
        return pickle.loads(res.content)

    return res.text

def get_stock_key_indicator(secu_code = None, start_date = None, end_date = None, report_types = None, fields = None):
    headers = {'Content-Type': 'application/json', 'token': g_token}
    url = base_url + 'get_stock_key_indicator'

    param = {'secu_code': secu_code, 'start_date': start_date, 'end_date': end_date, 'report_types': report_types, 'fields': fields}

    res = requests.post(url=url, headers=headers, data=json.dumps(param))

    if res.ok:
        return pickle.loads(res.content)

    return res.text

def get_accounting_data(en_prod_code = None, report_date = None, report_type = None, fields = None):
    headers = {'Content-Type': 'application/json', 'token': g_token}
    url = base_url + 'get_accounting_data'

    param = {'en_prod_code': en_prod_code, 'report_date': report_date, 'report_type': report_type, 'fields': fields}

    res = requests.post(url=url, headers=headers, data=json.dumps(param))

    if res.ok:
        return pickle.loads(res.content)

    return res.text

def get_financial_cashflow(secu_code = None, start_date = None, end_date = None, merge_type = None, fields = None):
    headers = {'Content-Type': 'application/json', 'token': g_token}
    url = base_url + 'get_financial_cashflow'

    param = {'secu_code': secu_code, 'start_date': start_date, 'end_date': end_date, 'merge_type': merge_type, 'fields': fields}

    res = requests.post(url=url, headers=headers, data=json.dumps(param))

    if res.ok:
        return pickle.loads(res.content)

    return res.text

def get_financial_income(secu_code = None, start_date = None, end_date = None, merge_type = None, fields = None):
    headers = {'Content-Type': 'application/json', 'token': g_token}
    url = base_url + 'get_financial_income'

    param = {'secu_code': secu_code, 'start_date': start_date, 'end_date': end_date, 'merge_type': merge_type, 'fields': fields}

    res = requests.post(url=url, headers=headers, data=json.dumps(param))

    if res.ok:
        return pickle.loads(res.content)

    return res.text

def get_financial_balance(secu_code = None, start_date = None, end_date = None, merge_type = None, fields = None):
    headers = {'Content-Type': 'application/json', 'token': g_token}
    url = base_url + 'get_financial_balance'

    param = {'secu_code': secu_code, 'start_date': start_date, 'end_date': end_date, 'merge_type': merge_type, 'fields': fields}

    res = requests.post(url=url, headers=headers, data=json.dumps(param))

    if res.ok:
        return pickle.loads(res.content)

    return res.text

def get_financial_gene_qincome(en_prod_code = None, report_date = None, report_type = None, fields = None):
    headers = {'Content-Type': 'application/json', 'token': g_token}
    url = base_url + 'get_financial_gene_qincome'

    param = {'en_prod_code': en_prod_code, 'report_date': report_date, 'report_type': report_type, 'fields': fields}

    res = requests.post(url=url, headers=headers, data=json.dumps(param))

    if res.ok:
        return pickle.loads(res.content)

    return res.text

def get_financial_bank_qincome(en_prod_code = None, report_date = None, report_type = None, fields = None):
    headers = {'Content-Type': 'application/json', 'token': g_token}
    url = base_url + 'get_financial_bank_qincome'

    param = {'en_prod_code': en_prod_code, 'report_date': report_date, 'report_type': report_type, 'fields': fields}

    res = requests.post(url=url, headers=headers, data=json.dumps(param))

    if res.ok:
        return pickle.loads(res.content)

    return res.text

def get_financial_secu_qincome(en_prod_code = None, report_date = None, report_type = None, fields = None):
    headers = {'Content-Type': 'application/json', 'token': g_token}
    url = base_url + 'get_financial_secu_qincome'

    param = {'en_prod_code': en_prod_code, 'report_date': report_date, 'report_type': report_type, 'fields': fields}

    res = requests.post(url=url, headers=headers, data=json.dumps(param))

    if res.ok:
        return pickle.loads(res.content)

    return res.text

def get_financial_insu_qincome(en_prod_code = None, report_date = None, report_type = None, fields = None):
    headers = {'Content-Type': 'application/json', 'token': g_token}
    url = base_url + 'get_financial_insu_qincome'

    param = {'en_prod_code': en_prod_code, 'report_date': report_date, 'report_type': report_type, 'fields': fields}

    res = requests.post(url=url, headers=headers, data=json.dumps(param))

    if res.ok:
        return pickle.loads(res.content)

    return res.text

def get_financial_gene_qcashflow(en_prod_code = None, report_date = None, report_type = None, fields = None):
    headers = {'Content-Type': 'application/json', 'token': g_token}
    url = base_url + 'get_financial_gene_qcashflow'

    param = {'en_prod_code': en_prod_code, 'report_date': report_date, 'report_type': report_type, 'fields': fields}

    res = requests.post(url=url, headers=headers, data=json.dumps(param))

    if res.ok:
        return pickle.loads(res.content)

    return res.text

def get_financial_bank_qcashflow(en_prod_code = None, report_date = None, report_type = None, fields = None):
    headers = {'Content-Type': 'application/json', 'token': g_token}
    url = base_url + 'get_financial_bank_qcashflow'

    param = {'en_prod_code': en_prod_code, 'report_date': report_date, 'report_type': report_type, 'fields': fields}

    res = requests.post(url=url, headers=headers, data=json.dumps(param))

    if res.ok:
        return pickle.loads(res.content)

    return res.text

def get_financial_secu_qcashflow(en_prod_code = None, report_date = None, report_type = None, fields = None):
    headers = {'Content-Type': 'application/json', 'token': g_token}
    url = base_url + 'get_financial_secu_qcashflow'

    param = {'en_prod_code': en_prod_code, 'report_date': report_date, 'report_type': report_type, 'fields': fields}

    res = requests.post(url=url, headers=headers, data=json.dumps(param))

    if res.ok:
        return pickle.loads(res.content)

    return res.text

def get_financial_insu_qcashflow(en_prod_code = None, report_date = None, report_type = None, fields = None):
    headers = {'Content-Type': 'application/json', 'token': g_token}
    url = base_url + 'get_financial_insu_qcashflow'

    param = {'en_prod_code': en_prod_code, 'report_date': report_date, 'report_type': report_type, 'fields': fields}

    res = requests.post(url=url, headers=headers, data=json.dumps(param))

    if res.ok:
        return pickle.loads(res.content)

    return res.text

def get_performance_forecast(en_prod_code = None, report_date = None, forecast_object = None, fields = None):
    headers = {'Content-Type': 'application/json', 'token': g_token}
    url = base_url + 'get_performance_forecast'

    param = {'en_prod_code': en_prod_code, 'report_date': report_date, 'forecast_object': forecast_object, 'fields': fields}

    res = requests.post(url=url, headers=headers, data=json.dumps(param))

    if res.ok:
        return pickle.loads(res.content)

    return res.text

def get_performance_letters(en_prod_code = None, report_date = None, fields = None):
    headers = {'Content-Type': 'application/json', 'token': g_token}
    url = base_url + 'get_performance_letters'

    param = {'en_prod_code': en_prod_code, 'report_date': report_date, 'fields': fields}

    res = requests.post(url=url, headers=headers, data=json.dumps(param))

    if res.ok:
        return pickle.loads(res.content)

    return res.text

def get_performance_letters_q(en_prod_code = None, report_date = None, fields = None):
    headers = {'Content-Type': 'application/json', 'token': g_token}
    url = base_url + 'get_performance_letters_q'

    param = {'en_prod_code': en_prod_code, 'report_date': report_date, 'fields': fields}

    res = requests.post(url=url, headers=headers, data=json.dumps(param))

    if res.ok:
        return pickle.loads(res.content)

    return res.text

def get_main_composition(en_prod_code = None, report_date = None, classification = None, order = None, fields = None):
    headers = {'Content-Type': 'application/json', 'token': g_token}
    url = base_url + 'get_main_composition'

    param = {'en_prod_code': en_prod_code, 'report_date': report_date, 'classification': classification, 'order': order, 'fields': fields}

    res = requests.post(url=url, headers=headers, data=json.dumps(param))

    if res.ok:
        return pickle.loads(res.content)

    return res.text

def get_trading_parties(en_prod_code = None, report_date = None, report_type = None, fields = None):
    headers = {'Content-Type': 'application/json', 'token': g_token}
    url = base_url + 'get_trading_parties'

    param = {'en_prod_code': en_prod_code, 'report_date': report_date, 'report_type': report_type, 'fields': fields}

    res = requests.post(url=url, headers=headers, data=json.dumps(param))

    if res.ok:
        return pickle.loads(res.content)

    return res.text

def get_audit_opinion(en_prod_code = None, report_date = None, fields = None):
    headers = {'Content-Type': 'application/json', 'token': g_token}
    url = base_url + 'get_audit_opinion'

    param = {'en_prod_code': en_prod_code, 'report_date': report_date, 'fields': fields}

    res = requests.post(url=url, headers=headers, data=json.dumps(param))

    if res.ok:
        return pickle.loads(res.content)

    return res.text

def get_per_share_index(en_prod_code = None, report_date = None, report_type = None, fields = None):
    headers = {'Content-Type': 'application/json', 'token': g_token}
    url = base_url + 'get_per_share_index'

    param = {
'en_prod_code': en_prod_code, 'report_date': report_date, 'report_type': report_type, 'fields': fields}

    res = requests.post(url=url, headers=headers, data=json.dumps(param))

    if res.ok:
        return pickle.loads(res.content)

    return res.text

def get_profitability(en_prod_code = None, report_date = None, report_type = None, fields = None):
    headers = {'Content-Type': 'application/json', 'token': g_token}
    url = base_url + 'get_profitability'

    param = {
'en_prod_code': en_prod_code, 'report_date': report_date, 'report_type': report_type, 'fields': fields}

    res = requests.post(url=url, headers=headers, data=json.dumps(param))

    if res.ok:
        return pickle.loads(res.content)

    return res.text

def get_growth_capacity(en_prod_code = None, report_date = None, report_type = None, fields = None):
    headers = {'Content-Type': 'application/json', 'token': g_token}
    url = base_url + 'get_growth_capacity'

    param = {
'en_prod_code': en_prod_code, 'report_date': report_date, 'report_type': report_type, 'fields': fields}

    res = requests.post(url=url, headers=headers, data=json.dumps(param))

    if res.ok:
        return pickle.loads(res.content)

    return res.text

def get_du_pont_analysis(en_prod_code = None, report_date = None, report_type = None, fields = None):
    headers = {'Content-Type': 'application/json', 'token': g_token}
    url = base_url + 'get_du_pont_analysis'

    param = {
'en_prod_code': en_prod_code, 'report_date': report_date, 'report_type': report_type, 'fields': fields}

    res = requests.post(url=url, headers=headers, data=json.dumps(param))

    if res.ok:
        return pickle.loads(res.content)

    return res.text

def get_deri_fin_indicators(en_prod_code = None, report_date = None, report_type = None, fields = None):
    headers = {'Content-Type': 'application/json', 'token': g_token}
    url = base_url + 'get_deri_fin_indicators'

    param = {
'en_prod_code': en_prod_code, 'report_date': report_date, 'report_type': report_type, 'fields': fields}

    res = requests.post(url=url, headers=headers, data=json.dumps(param))

    if res.ok:
        return pickle.loads(res.content)

    return res.text

def get_q_financial_indicator(en_prod_code = None, report_date = None, report_type = None, fields = None):
    headers = {'Content-Type': 'application/json', 'token': g_token}
    url = base_url + 'get_q_financial_indicator'

    param = {
'en_prod_code': en_prod_code, 'report_date': report_date, 'report_type': report_type, 'fields': fields}

    res = requests.post(url=url, headers=headers, data=json.dumps(param))

    if res.ok:
        return pickle.loads(res.content)

    return res.text

def get_valuation_info(en_prod_code = None, trading_date = None, year = None, fields = None):
    headers = {'Content-Type': 'application/json', 'token': g_token}
    url = base_url + 'get_valuation_info'

    param = {
'en_prod_code': en_prod_code, 'trading_date': trading_date, 'year': year, 'fields': fields}

    res = requests.post(url=url, headers=headers, data=json.dumps(param))

    if res.ok:
        return pickle.loads(res.content)

    return res.text

def get_corporation_value(en_prod_code = None, trading_date = None, fields = None):
    headers = {'Content-Type': 'application/json', 'token': g_token}
    url = base_url + 'get_corporation_value'

    param = {
'en_prod_code': en_prod_code, 'trading_date': trading_date, 'fields': fields}

    res = requests.post(url=url, headers=headers, data=json.dumps(param))

    if res.ok:
        return pickle.loads(res.content)

    return res.text

def get_stock_main_composition(secu_code = None, start_date = None, end_date = None, classification = None, fields = None):
    headers = {'Content-Type': 'application/json', 'token': g_token}
    url = base_url + 'get_stock_main_composition'

    param = {'secu_code': secu_code, 'start_date': start_date, 'end_date': end_date, 'classification': classification, 'fields': fields}

    res = requests.post(url=url, headers=headers, data=json.dumps(param))

    if res.ok:
        return pickle.loads(res.content)

    return res.text

def get_stock_main_business_total(secu_code = None, classification = None, fields = None):
    headers = {'Content-Type': 'application/json', 'token': g_token}
    url = base_url + 'get_stock_main_business_total'

    param = {'secu_code': secu_code, 'classification': classification, 'fields': fields}

    res = requests.post(url=url, headers=headers, data=json.dumps(param))

    if res.ok:
        return pickle.loads(res.content)

    return res.text

def get_stock_main_business_indurstry(en_prod_code = None):
    headers = {'Content-Type': 'application/json', 'token': g_token}
    url = base_url + 'get_stock_main_business_indurstry'

    param = {'en_prod_code': en_prod_code}

    res = requests.post(url=url, headers=headers, data=json.dumps(param))

    if res.ok:
        return pickle.loads(res.content)

    return res.text

def get_star_ipodeclare(report_status = None, fields = None):
    headers = {'Content-Type': 'application/json', 'token': g_token}
    url = base_url + 'get_star_ipodeclare'

    param = {'report_status': report_status, 'fields': fields}

    res = requests.post(url=url, headers=headers, data=json.dumps(param))

    if res.ok:
        return pickle.loads(res.content)

    return res.text

def get_star_companyprofile(secu_code = None, fields = None):
    headers = {'Content-Type': 'application/json', 'token': g_token}
    url = base_url + 'get_star_companyprofile'

    param = {'secu_code': secu_code, 'fields': fields}

    res = requests.post(url=url, headers=headers, data=json.dumps(param))

    if res.ok:
        return pickle.loads(res.content)

    return res.text

def get_neeq_basic(en_prod_code = None, fields = None):
    headers = {'Content-Type': 'application/json', 'token': g_token}
    url = base_url + 'get_neeq_basic'

    param = {'en_prod_code': en_prod_code, 'fields': fields}

    res = requests.post(url=url, headers=headers, data=json.dumps(param))

    if res.ok:
        return pickle.loads(res.content)

    return res.text

def get_neeq_company(en_prod_code = None, fields = None):
    headers = {'Content-Type': 'application/json', 'token': g_token}
    url = base_url + 'get_neeq_company'

    param = {'en_prod_code': en_prod_code, 'fields': fields}

    res = requests.post(url=url, headers=headers, data=json.dumps(param))

    if res.ok:
        return pickle.loads(res.content)

    return res.text

def get_neeq_leader(en_prod_code = None, fields = None):
    headers = {'Content-Type': 'application/json', 'token': g_token}
    url = base_url + 'get_neeq_leader'

    param = {'en_prod_code': en_prod_code, 'fields': fields}

    res = requests.post(url=url, headers=headers, data=json.dumps(param))

    if res.ok:
        return pickle.loads(res.content)

    return res.text

def get_neeq_leader_num(en_prod_code = None, end_date = None, fields = None):
    headers = {'Content-Type': 'application/json', 'token': g_token}
    url = base_url + 'get_neeq_leader_num'

    param = {'en_prod_code': en_prod_code, 'end_date': end_date, 'fields': fields}

    res = requests.post(url=url, headers=headers, data=json.dumps(param))

    if res.ok:
        return pickle.loads(res.content)

    return res.text

def get_neeq_industry(en_prod_code = None, level = None, fields = None):
    headers = {'Content-Type': 'application/json', 'token': g_token}
    url = base_url + 'get_neeq_industry'

    param = {'en_prod_code': en_prod_code, 'level': level, 'fields': fields}

    res = requests.post(url=url, headers=headers, data=json.dumps(param))

    if res.ok:
        return pickle.loads(res.content)

    return res.text

def get_neeq_perform_fore(en_prod_code = None, report_date = None, unit = None, fields = None):
    headers = {'Content-Type': 'application/json', 'token': g_token}
    url = base_url + 'get_neeq_perform_fore'

    param = {'en_prod_code': en_prod_code, 'report_date': report_date, 'unit': unit, 'fields': fields}

    res = requests.post(url=url, headers=headers, data=json.dumps(param))

    if res.ok:
        return pickle.loads(res.content)

    return res.text

def get_neeq_dupont_analysis(en_prod_code = None, report_date = None, unit = None, fields = None):
    headers = {'Content-Type': 'application/json', 'token': g_token}
    url = base_url + 'get_neeq_dupont_analysis'

    param = {'en_prod_code': en_prod_code, 'report_date': report_date, 'unit': unit, 'fields': fields}

    res = requests.post(url=url, headers=headers, data=json.dumps(param))

    if res.ok:
        return pickle.loads(res.content)

    return res.text

def get_neeq_share_stru(en_prod_code = None, end_date = None, unit = None, fields = None):
    headers = {'Content-Type': 'application/json', 'token': g_token}
    url = base_url + 'get_neeq_share_stru'

    param = {'en_prod_code': en_prod_code, 'end_date': end_date, 'unit': unit, 'fields': fields}

    res = requests.post(url=url, headers=headers, data=json.dumps(param))

    if res.ok:
        return pickle.loads(res.content)

    return res.text

def get_neeq_per_share_index(en_prod_code = None, report_date = None, unit = None, fields = None):
    headers = {'Content-Type': 'application/json', 'token': g_token}
    url = base_url + 'get_neeq_per_share_index'

    param = {'en_prod_code': en_prod_code, 'report_date': report_date, 'unit': unit, 'fields': fields}

    res = requests.post(url=url, headers=headers, data=json.dumps(param))

    if res.ok:
        return pickle.loads(res.content)

    return res.text

def get_neeq_issue_count(en_prod_code = None, date_range = None, date_type = None, unit = None, fields = None):
    headers = {'Content-Type': 'application/json', 'token': g_token}
    url = base_url + 'get_neeq_issue_count'

    param = {'en_prod_code': en_prod_code, 'date_range': date_range, 'date_type': date_type, 'unit': unit, 'fields': fields}

    res = requests.post(url=url, headers=headers, data=json.dumps(param))

    if res.ok:
        return pickle.loads(res.content)

    return res.text

def get_neeq_holder_num(en_prod_code = None, report_date = None, query_direction = None, unit = None, fields = None):
    headers = {'Content-Type': 'application/json', 'token': g_token}
    url = base_url + 'get_neeq_holder_num'

    param = {'en_prod_code': en_prod_code, 'report_date': report_date, 'query_direction': query_direction, 'unit': unit, 'fields': fields}

    res = requests.post(url=url, headers=headers, data=json.dumps(param))

    if res.ok:
        return pickle.loads(res.content)

    return res.text

def get_neeq_holder_info(en_prod_code = None, end_date = None, serial_number = None, share_query_type = None, unit = None, fields = None):
    headers = {'Content-Type': 'application/json', 'token': g_token}
    url = base_url + 'get_neeq_holder_info'

    param = {'en_prod_code': en_prod_code, 'end_date': end_date, 'serial_number': serial_number, 'share_query_type': share_query_type, 'unit': unit, 'fields': fields}

    res = requests.post(url=url, headers=headers, data=json.dumps(param))

    if res.ok:
        return pickle.loads(res.content)

    return res.text


if __name__ == '__main__':
    set_token('abc')

    data = get_neeq_holder_info()
    # data = get_neeq_holder_num()
    # data = get_neeq_issue_count()
    # data = get_neeq_per_share_index()
    # data = get_neeq_share_stru()
    # data = get_neeq_dupont_analysis()
    # data = get_neeq_industry()
    # data = get_neeq_leader_num()
    # data = get_neeq_leader()
    # data = get_neeq_company()
    # data = get_neeq_basic()
    # data = get_star_companyprofile()
    # data = get_star_ipodeclare()
    # data = get_stock_main_business_indurstry()
    # data = get_stock_main_business_total()
    # data = get_stock_main_composition()
    # data = get_corporation_value()
    # data = get_q_financial_indicator()
    # data = get_deri_fin_indicators()
    # data = get_du_pont_analysis()
    # data = get_growth_capacity()
    # data = get_profitability()
    # data = get_per_share_index()
    # data = get_audit_opinion()
    # data = get_trading_parties()
    # data = get_main_composition()
    # data = get_performance_letters_q()
    # data = get_performance_letters()
    # data = get_performance_forecast()
    # data = get_financial_insu_qcashflow()
    # data = get_financial_secu_qcashflow()
    # data = get_financial_bank_qcashflow()
    # data = get_financial_gene_qcashflow()
    # data = get_financial_insu_qincome()
    # data = get_financial_secu_qincome()
    # data = get_financial_bank_qincome()
    # data = get_financial_gene_qincome()
    # data = get_financial_income()
    # data = get_accounting_data()
    # data = get_stock_key_indicator()
    # data = get_schedule_disclosure()
    # data = get_stock_industry_region_list()
    # data = get_stock_industry_compare()
    # data = get_stock_financial_industry_list()
    # data = get_stock_investor_detail()
    # data = get_stock_investor_statistics()
    # data = get_stock_org_rate()
    # data = get_stock_special_tradedate()
    # data = get_stock_share_holders(en_prod_code = '000001.SZ')
    # data = get_stock_asrighttransfer()
    # data = get_stock_asforecastabb()
    # data = get_stock_allotment(en_prod_code = '000001.SZ')
    # data = get_stock_additional_all(en_prod_code = '000001.SZ')
    # data = get_stock_additional(en_prod_code = '000001.SZ')
    # data = get_stock_dividend(en_prod_code = '000001.SZ')
    # data = get_margin_trade_total()
    # data = get_margin_trade_detail()
    # data = get_interval_margin_trading(en_prod_code = '000001.SZ')
    # data = get_margin_trading()
    # data = get_block_trade(start_date='2022-01-01', end_date='2023-02-01')
    # data = get_stock_pledge()
    # data = get_pledge_repo()
    # data = get_holder_increase(symbols = '000001.SZ')
    # data = get_holder_pledge(en_prod_code = '000001.SZ', trading_date='2023-02-01')
    # data = get_holder_num(en_prod_code = '000001.SZ', report_date='2023-02-01')
    # data = get_org_hold()
    # data = get_index_constituent()
    # data = get_industry_category(en_prod_code = '000001.SZ')
    # data = get_index_quote(en_prod_code = '000001.SZ', trading_date='2023-02-01')
    # data = get_stock_quote_daily_list(en_prod_code = '000001.SZ', begin_date='2023-02-01', end_date='2023-02-01')
    # data = get_quote_stocklist()
    # data = get_shszhk_change_top10()
    # data = get_shszhk_distribution(start_date='2023-02-01', end_date='2023-02-01')
    # data = get_shszhk_deal_top10(start_date='2023-02-01', end_date='2023-02-01')
    # data = get_shszhk_capitalflow(start_date='2023-02-01', end_date='2023-02-01')
    # data = get_stock_quote_minutes(en_prod_code = '000001.SZ', begin_date='2023-02-01', end_date='2023-02-01')
    # data = get_lh_stock()
    # data = get_lh_daily()
    # data = get_float_shareholder_top10(secu_code = '000001.SZ')
    # data = get_shareholder_top10(secu_code = '000001.SZ')
    # data = get_suspension_list(en_prod_code = '000001.SZ')
    # data = get_money_flow(en_prod_code = '000001.SZ')
    # data = get_stock_quote_yearly(en_prod_code = '000001.SZ')
    # data = get_stock_quote_monthly(en_prod_code = '000001.SZ')
    # data = get_stock_quote_weekly()
    # data = get_stock_quote_daily()
    # data = get_shszhk_stock_list()
    # data = get_st_stock_list()
    # data = get_stock_Info()
    # data = get_stock_list()
    # data = get_trading_calendar()
    # data = get_ipo_list()
    # data = get_company_profile()

    print(data)