#!/usr/bin/python
# coding = utf-8
import numpy as np
import pandas as pd
from WindPy import w
def convertInputSecurityType(func):
    def convertedFunc(*args):
        args = tuple((i.strftime("%Y-%m-%d") if hasattr(i,"strftime") else i for i in args))
        if type(args[0])==type(''):
            return func(*args)[1].fillna(np.nan)
        else:
            security = args[0]
            args = args[1:]
            return func(",".join(security),*args)[1].fillna(np.nan)
    return convertedFunc
@convertInputSecurityType
def getMmAvgPtM(security:list,*args,**kwargs):
    """
	获取报告期末投资组合平均剩余期限

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"mmavgptm",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getMmAvgPtMMax(security:list,*args,**kwargs):
    """
	获取报告期内投资组合平均剩余期限最高值

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"mmavgptm_max",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getMmAvgPtMMin(security:list,*args,**kwargs):
    """
	获取报告期内投资组合平均剩余期限最低值

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"mmavgptm_min",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPrtBondByCreditRating(security:list,*args,**kwargs):
    """
	获取按信用评级的债券投资市值

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"prt_bondbycreditrating",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPrtAbsByCreditRating(security:list,*args,**kwargs):
    """
	获取按信用评级的资产支持证券投资市值

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"prt_absbycreditrating",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPrtNcdByCreditRating(security:list,*args,**kwargs):
    """
	获取按信用评级的同业存单投资市值

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"prt_ncdbycreditrating",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPrtBondByCreditRatingToNav(security:list,*args,**kwargs):
    """
	获取按信用评级的债券投资占基金资产净值比

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"prt_bondbycreditratingtonav",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPrtAbsByCreditRatingToNav(security:list,*args,**kwargs):
    """
	获取按信用评级的资产支持证券投资占基金资产净值比

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"prt_absbycreditratingtonav",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPrtNcdByCreditRatingToNav(security:list,*args,**kwargs):
    """
	获取按信用评级的同业存单投资占基金资产净值比

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"prt_ncdbycreditratingtonav",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getInStYyBondVal(security:list,*args,**kwargs):
    """
	获取债券估值(YY)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"inst_yybondval",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getInStYyBondValHis(security:list,*args,**kwargs):
    """
	获取债券估值历史(YY)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"inst_yybondvalhis",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getMrgBal(security:list,*args,**kwargs):
    """
	获取融资融券余额

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"mrg_bal",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getMarginGuaranteedStocksMarketValue(security:list,*args,**kwargs):
    """
	获取融资融券担保股票市值

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"margin_guaranteedstocksmarketvalue",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getMarginOrNot(security:list,*args,**kwargs):
    """
	获取是否融资融券标的

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"marginornot",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getMrgBalIntAvg(security:list,*args,**kwargs):
    """
	获取区间融资融券余额均值

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"mrg_bal_int_avg",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getStmNoteSec1511(security:list,*args,**kwargs):
    """
	获取利息收入:融资融券业务

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"stmnote_sec_1511",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getStmNoteSec1531(security:list,*args,**kwargs):
    """
	获取利息净收入:融资融券业务

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"stmnote_sec_1531",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getHisChange(security:list,*args,**kwargs):
    """
	获取涨跌_期货历史同月

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"His_change",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getHisSwing(security:list,*args,**kwargs):
    """
	获取振幅_期货历史同月

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"His_swing",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getHisClose(security:list,*args,**kwargs):
    """
	获取收盘价_期货历史同月

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"His_close",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getHisOpen(security:list,*args,**kwargs):
    """
	获取开盘价_期货历史同月

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"His_open",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getHisHigh(security:list,*args,**kwargs):
    """
	获取最高价_期货历史同月

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"His_high",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getHisLow(security:list,*args,**kwargs):
    """
	获取最低价_期货历史同月

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"His_low",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getHisSettle(security:list,*args,**kwargs):
    """
	获取结算价_期货历史同月

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"His_settle",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getHisPctChange(security:list,*args,**kwargs):
    """
	获取涨跌幅_期货历史同月

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"His_pctchange",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getHisVolume(security:list,*args,**kwargs):
    """
	获取成交量_期货历史同月

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"His_volume",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getHisTurnover(security:list,*args,**kwargs):
    """
	获取成交额_期货历史同月

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"His_turnover",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getHisOi(security:list,*args,**kwargs):
    """
	获取持仓量_期货历史同月

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"His_oi",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getHisPreSettle(security:list,*args,**kwargs):
    """
	获取前结算价_期货历史同月

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"His_preSettle",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getHisAvgPrice(security:list,*args,**kwargs):
    """
	获取成交均价_期货历史同月

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"His_avgprice",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getHisOiChange(security:list,*args,**kwargs):
    """
	获取持仓变化_期货历史同月

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"His_oichange",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getHisCloseNight(security:list,*args,**kwargs):
    """
	获取收盘价(夜盘)_期货历史同月

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"His_close_night",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getHisChangeSettlement(security:list,*args,**kwargs):
    """
	获取涨跌(结算价)_期货历史同月

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"His_change_settlement",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getHisPctChangeSettlement(security:list,*args,**kwargs):
    """
	获取涨跌幅(结算价)_期货历史同月

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"His_pctchange_settlement",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getProfitNoticeAbstract(security:list,*args,**kwargs):
    """
	获取业绩预告摘要

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"profitnotice_abstract",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getProfitNoticeReason(security:list,*args,**kwargs):
    """
	获取业绩预告变动原因

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"profitnotice_reason",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getProfitNoticeStyle(security:list,*args,**kwargs):
    """
	获取业绩预告类型

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"profitnotice_style",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getProfitNoticeDate(security:list,*args,**kwargs):
    """
	获取业绩预告最新披露日期

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"profitnotice_date",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getProfitNoticeFirstDate(security:list,*args,**kwargs):
    """
	获取业绩预告首次披露日期

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"profitnotice_firstdate",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getProfitNoticeLastRpTDate(security:list,*args,**kwargs):
    """
	获取最新业绩预告报告期

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"profitnotice_lastrptdate",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getQProfitNoticeAbstract(security:list,*args,**kwargs):
    """
	获取单季度.业绩预告摘要(海外)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"qprofitnotice_abstract",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getQProfitNoticeStyle(security:list,*args,**kwargs):
    """
	获取单季度.业绩预告类型(海外)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"qprofitnotice_style",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getQProfitNoticeDate(security:list,*args,**kwargs):
    """
	获取单季度.业绩预告日期(海外)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"qprofitnotice_date",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPerformanceExpressLastDate(security:list,*args,**kwargs):
    """
	获取业绩快报最新披露日期

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"performanceexpress_lastdate",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPerformanceExpressDate(security:list,*args,**kwargs):
    """
	获取业绩快报首次披露日期

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"performanceexpress_date",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPerformanceExpressPerFExIncome(security:list,*args,**kwargs):
    """
	获取业绩快报.营业收入

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"performanceexpress_perfexincome",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPerformanceExpressPerFExprOfIt(security:list,*args,**kwargs):
    """
	获取业绩快报.营业利润

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"performanceexpress_perfexprofit",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPerformanceExpressPerFExTotalProfit(security:list,*args,**kwargs):
    """
	获取业绩快报.利润总额

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"performanceexpress_perfextotalprofit",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPerformanceExpressPerFExNetProfitToShareholder(security:list,*args,**kwargs):
    """
	获取业绩快报.归属母公司股东的净利润

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"performanceexpress_perfexnetprofittoshareholder",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPerformanceExpressNpdEdToShareholder(security:list,*args,**kwargs):
    """
	获取业绩快报.归属于上市公司股东的扣除非经常性损益的净利润

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"performanceexpress_npdedtoshareholder",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPerformanceExpressPerFExEpsDiluted(security:list,*args,**kwargs):
    """
	获取业绩快报.每股收益EPS-基本

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"performanceexpress_perfexepsdiluted",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPerformanceExpressPerFExRoeDiluted(security:list,*args,**kwargs):
    """
	获取业绩快报.净资产收益率ROE-加权

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"performanceexpress_perfexroediluted",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPerformanceExpressPerFExTotalAssets(security:list,*args,**kwargs):
    """
	获取业绩快报.总资产

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"performanceexpress_perfextotalassets",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPerformanceExpressPerFExNetAssets(security:list,*args,**kwargs):
    """
	获取业绩快报.净资产

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"performanceexpress_perfexnetassets",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPerformanceExpressOrYoY(security:list,*args,**kwargs):
    """
	获取业绩快报.同比增长率:营业收入

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"performanceexpress_or_yoy",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPerformanceExpressOpYoY(security:list,*args,**kwargs):
    """
	获取业绩快报.同比增长率:营业利润

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"performanceexpress_op_yoy",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPerformanceExpressEBtYoY(security:list,*args,**kwargs):
    """
	获取业绩快报.同比增长率:利润总额

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"performanceexpress_ebt_yoy",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPerformanceExpressNpYoY(security:list,*args,**kwargs):
    """
	获取业绩快报.同比增长率:归属母公司股东的净利润

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"performanceexpress_np_yoy",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPerformanceExpressNpdEdYoY(security:list,*args,**kwargs):
    """
	获取业绩快报.同比增长率:归属于上市公司股东的扣除非经常性损益的净利润

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"performanceexpress_npded_yoy",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPerformanceExpressEpsYoY(security:list,*args,**kwargs):
    """
	获取业绩快报.同比增长率:基本每股收益

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"performanceexpress_eps_yoy",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPerformanceExpressRoeYoY(security:list,*args,**kwargs):
    """
	获取业绩快报.同比增减:加权平均净资产收益率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"performanceexpress_roe_yoy",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPerformanceExpressIncomeYa(security:list,*args,**kwargs):
    """
	获取业绩快报.去年同期营业收入

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"performanceexpress_income_ya",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPerformanceExpressProfitYa(security:list,*args,**kwargs):
    """
	获取业绩快报.去年同期营业利润

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"performanceexpress_profit_ya",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPerformanceExpressToTProfitYa(security:list,*args,**kwargs):
    """
	获取业绩快报.去年同期利润总额

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"performanceexpress_totprofit_ya",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPerformanceExpressNetProfitYa(security:list,*args,**kwargs):
    """
	获取业绩快报.去年同期净利润

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"performanceexpress_netprofit_ya",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPerformanceExpressNpdEdYa(security:list,*args,**kwargs):
    """
	获取业绩快报.上年同期归属于上市公司股东的扣除非经常性损益的净利润

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"performanceexpress_npded_ya",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPerformanceExpressEpsYa(security:list,*args,**kwargs):
    """
	获取业绩快报.去年同期每股收益

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"performanceexpress_eps_ya",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPerformanceExpressBpS(security:list,*args,**kwargs):
    """
	获取业绩快报.每股净资产

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"performanceexpress_bps",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPerformanceExpressNetAssetsB(security:list,*args,**kwargs):
    """
	获取业绩快报.期初净资产

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"performanceexpress_netassets_b",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPerformanceExpressBpSB(security:list,*args,**kwargs):
    """
	获取业绩快报.期初每股净资产

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"performanceexpress_bps_b",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPerformanceExpressEqYGrowth(security:list,*args,**kwargs):
    """
	获取业绩快报.比年初增长率:归属母公司的股东权益

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"performanceexpress_eqy_growth",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPerformanceExpressBpSGrowth(security:list,*args,**kwargs):
    """
	获取业绩快报.比年初增长率:归属于母公司股东的每股净资产

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"performanceexpress_bps_growth",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPerformanceExpressToTAssetsGrowth(security:list,*args,**kwargs):
    """
	获取业绩快报.比年初增长率:总资产

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"performanceexpress_totassets_growth",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPerformanceExpressLastRpTDate(security:list,*args,**kwargs):
    """
	获取最新业绩快报报告期

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"performanceexpress_lastrptdate",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getRelatedCbYearlyAmount(security:list,*args,**kwargs):
    """
	获取年度可转债发行量

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"relatedcb_yearlyamount",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIssueCoordinator(security:list,*args,**kwargs):
    """
	获取基金发行协调人

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"issue_coordinator",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIssuePrice(security:list,*args,**kwargs):
    """
	获取上市基金发行价格

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"issue_price",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getStmIs82(security:list,*args,**kwargs):
    """
	获取基金分红收益_FUND

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"stm_is_82",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundFundScale(security:list,*args,**kwargs):
    """
	获取基金规模

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_fundscale",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getNetAssetTotal(security:list,*args,**kwargs):
    """
	获取基金规模(合计)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"netasset_total",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIndustryNc(security:list,*args,**kwargs):
    """
	获取所属国民经济行业分类

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"industry_nc",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getStmNoteMGmtBen(security:list,*args,**kwargs):
    """
	获取管理层年度薪酬总额

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"stmnote_mgmt_ben",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getHolderPriceMh(security:list,*args,**kwargs):
    """
	获取管理层增持价格

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"holder_price_mh",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getShareCn(security:list,*args,**kwargs):
    """
	获取中资中介机构持股数量

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"share_CN",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getShareOs(security:list,*args,**kwargs):
    """
	获取国际中介机构持股数量

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"share_OS",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getSharePctCn(security:list,*args,**kwargs):
    """
	获取中资中介机构持股占比

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"share_pct_CN",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getSharePctOs(security:list,*args,**kwargs):
    """
	获取国际中介机构持股占比

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"share_pct_OS",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getShareHk(security:list,*args,**kwargs):
    """
	获取香港本地中介机构持股数量

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"share_HK",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getSharePctHk(security:list,*args,**kwargs):
    """
	获取香港本地中介机构持股占比

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"share_pct_HK",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIrNoIi(security:list,*args,**kwargs):
    """
	获取机构调研家数

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"ir_noii",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIrIRfd(security:list,*args,**kwargs):
    """
	获取机构调研首日

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"ir_irfd",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIrIrlD(security:list,*args,**kwargs):
    """
	获取机构调研最新日

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"ir_irld",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIrNoSoIi(security:list,*args,**kwargs):
    """
	获取投资机构调研次数

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"ir_nosoii",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIrNoIiii(security:list,*args,**kwargs):
    """
	获取投资机构调研家数

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"ir_noiiii",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIrNosOfI(security:list,*args,**kwargs):
    """
	获取外资机构调研次数

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"ir_nosofi",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIrNoIiFi(security:list,*args,**kwargs):
    """
	获取外资机构调研家数

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"ir_noiifi",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getShareLiqAPct(security:list,*args,**kwargs):
    """
	获取流通A股占总股本比例

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"share_liqa_pct",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getShareRestrictedAPct(security:list,*args,**kwargs):
    """
	获取限售A股占总股本比例

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"share_restricteda_pct",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getShareTotalAPct(security:list,*args,**kwargs):
    """
	获取A股合计占总股本比例

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"share_totala_pct",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getShareLiqBPct(security:list,*args,**kwargs):
    """
	获取流通B股占总股本比例

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"share_liqb_pct",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getShareRestrictedBPct(security:list,*args,**kwargs):
    """
	获取限售B股占总股本比例

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"share_restrictedb_pct",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getShareTotalBPct(security:list,*args,**kwargs):
    """
	获取B股合计占总股本比例

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"share_totalb_pct",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getShareOtcAPct(security:list,*args,**kwargs):
    """
	获取三板A股占总股本比例

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"share_otca_pct",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getShareOtcBPct(security:list,*args,**kwargs):
    """
	获取三板B股占总股本比例

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"share_otcb_pct",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getShareTotalOtcPct(security:list,*args,**kwargs):
    """
	获取三板合计占总股本比例

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"share_totalotc_pct",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getShareLiqHPct(security:list,*args,**kwargs):
    """
	获取香港上市股占总股本比例

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"share_liqh_pct",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getShareOverSeaPct(security:list,*args,**kwargs):
    """
	获取海外上市股占总股本比例

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"share_oversea_pct",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getShareTradablePct(security:list,*args,**kwargs):
    """
	获取流通股合计占总股本比例

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"share_tradable_pct",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getShareRestrictedPct(security:list,*args,**kwargs):
    """
	获取限售股合计占总股本比例

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"share_restricted_pct",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getShareFreeFloatsHrPct(security:list,*args,**kwargs):
    """
	获取自由流通股占总股本比例

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"share_freefloatshr_pct",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getShortSellShortIntRestPct(security:list,*args,**kwargs):
    """
	获取未平仓卖空数占总股本比例

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"shortsell_shortintrestpct",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getShareNonTradablePct(security:list,*args,**kwargs):
    """
	获取股改前非流通股占总股本比例

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"share_nontradable_pct",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getSharePledgedA(security:list,*args,**kwargs):
    """
	获取质押股份数量合计

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"share_pledgeda",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getUnitTotal(security:list,*args,**kwargs):
    """
	获取基金份额

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"unit_total",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getUnitFundShareTotal(security:list,*args,**kwargs):
    """
	获取基金份额(合计)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"unit_fundshare_total",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getUnitChange(security:list,*args,**kwargs):
    """
	获取基金份额变化

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"unit_change",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getUnitChangeRate(security:list,*args,**kwargs):
    """
	获取基金份额变化率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"unit_changerate",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getHolderNumber(security:list,*args,**kwargs):
    """
	获取基金份额持有人户数

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"holder_number",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundHolderTotalNumber(security:list,*args,**kwargs):
    """
	获取基金份额持有人户数(合计)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_holder_totalnumber",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getUnitChangeDate(security:list,*args,**kwargs):
    """
	获取基金份额变动日期

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"unit_changedate",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getStmNavChange9(security:list,*args,**kwargs):
    """
	获取本期基金份额交易产生的基金净值变动数

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"stm_navchange_9",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundFundShareTranslationDate(security:list,*args,**kwargs):
    """
	获取ETF基金份额折算日

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_fundsharetranslationdate",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundFundShareTranslationRatio(security:list,*args,**kwargs):
    """
	获取ETF基金份额折算比例

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_fundsharetranslationratio",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getStmNavChange10(security:list,*args,**kwargs):
    """
	获取本期向基金份额持有人分配利润产生的基金净值变动数

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"stm_navchange_10",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getQAnalNavReturn(security:list,*args,**kwargs):
    """
	获取单季度.基金份额净值增长率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"qanal_navreturn",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getQAnalStdNavReturn(security:list,*args,**kwargs):
    """
	获取单季度.基金份额净值增长率标准差

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"qanal_stdnavreturn",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getHolderAvgHolding(security:list,*args,**kwargs):
    """
	获取平均每户持有基金份额

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"holder_avgholding",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getQAnalAccumulatedNavReturn(security:list,*args,**kwargs):
    """
	获取单季度.累计基金份额净值增长率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"qanal_accumulatednavreturn",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getQAnalAvgNetIncomePerUnit(security:list,*args,**kwargs):
    """
	获取单季度.加权平均基金份额本期利润

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"qanal_avgnetincomeperunit",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getQAnalAvgUnitIncome(security:list,*args,**kwargs):
    """
	获取单季度.加权平均基金份额本期净收益

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"qanal_avgunitincome",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getAnalDIsTriButAblePerUnit(security:list,*args,**kwargs):
    """
	获取报告期末可供分配基金份额利润

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"anal_distributableperunit",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getQAnalNav(security:list,*args,**kwargs):
    """
	获取单季度.报告期期末基金份额净值

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"qanal_nav",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getHolderNum(security:list,*args,**kwargs):
    """
	获取股东户数

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"holder_num",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getHolderTotalByInSt(security:list,*args,**kwargs):
    """
	获取机构持股数量合计

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"holder_totalbyinst",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getHolderPctByInSt(security:list,*args,**kwargs):
    """
	获取机构持股比例合计

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"holder_pctbyinst",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getSHClearL1Type(security:list,*args,**kwargs):
    """
	获取上清所债券分类

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"shclearl1type",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getRateOfStdBnd(security:list,*args,**kwargs):
    """
	获取标准券折算比例

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"rateofstdbnd",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getClauseConversion2ToSharePriceAdjustItem(security:list,*args,**kwargs):
    """
	获取转股条款

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"clause_conversion2_tosharepriceadjustitem",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getClauseCallOptionRedeemItem(security:list,*args,**kwargs):
    """
	获取赎回条款

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"clause_calloption_redeemitem",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getClauseCallOptionRedeemClause(security:list,*args,**kwargs):
    """
	获取时点赎回条款全文

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"clause_calloption_redeemclause",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getMassRedemptionProvision(security:list,*args,**kwargs):
    """
	获取巨额赎回条款

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"massredemptionprovision",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getClauseCallOptionIsWithTimeRedemptionClause(security:list,*args,**kwargs):
    """
	获取是否有时点赎回条款

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"clause_calloption_iswithtimeredemptionclause",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getClausePutOptionSellBackItem(security:list,*args,**kwargs):
    """
	获取条件回售条款全文

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"clause_putoption_sellbackitem",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getClausePutOptionTimePutBackClause(security:list,*args,**kwargs):
    """
	获取时点回售条款全文

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"clause_putoption_timeputbackclause",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getClausePutOptionPutBackClause(security:list,*args,**kwargs):
    """
	获取无条件回售条款

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"clause_putoption_putbackclause",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getRatingLatestMonth(security:list,*args,**kwargs):
    """
	获取最新评级月份

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"rating_latestmonth",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getLatestIsSurerCreditRating(security:list,*args,**kwargs):
    """
	获取发行人最新评级

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"latestissurercreditrating",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getRatingOutlooks(security:list,*args,**kwargs):
    """
	获取发行人最新评级展望

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"ratingoutlooks",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getLatestIsSurerCreditRatingDate(security:list,*args,**kwargs):
    """
	获取发行人最新评级日期

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"latestissurercreditratingdate",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getLatestRatingDate(security:list,*args,**kwargs):
    """
	获取发行人最新评级日期(指定机构)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"latestratingdate",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getRateLateIssuerChNg(security:list,*args,**kwargs):
    """
	获取发行人最新评级变动方向

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"rate_lateissuerchng",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getLatestIsSurerCreditRatingType(security:list,*args,**kwargs):
    """
	获取发行人最新评级评级类型

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"latestissurercreditratingtype",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getLatestRatingOfGuarantor(security:list,*args,**kwargs):
    """
	获取担保人最新评级

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"latestratingofguarantor",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getRateLateGuarantorFwd(security:list,*args,**kwargs):
    """
	获取担保人最新评级展望

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"rate_lateguarantorfwd",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getRateLateGuarantorDate(security:list,*args,**kwargs):
    """
	获取担保人最新评级日期

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"rate_lateguarantordate",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getRateLateGuaranTorchNg(security:list,*args,**kwargs):
    """
	获取担保人最新评级变动方向

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"rate_lateguarantorchng",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getRateBond2(security:list,*args,**kwargs):
    """
	获取债券国际评级

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"ratebond2",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIssuer2(security:list,*args,**kwargs):
    """
	获取发行人国际评级

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"issuer2",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getRepoCode(security:list,*args,**kwargs):
    """
	获取回购代码

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"repo_code",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getRepoUBond(security:list,*args,**kwargs):
    """
	获取标的债券

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"repo_ubond",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getCrmUbonDouStandingAmount(security:list,*args,**kwargs):
    """
	获取发行时标的债券余额

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"crm_ubondoustandingamount",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getRepoType(security:list,*args,**kwargs):
    """
	获取回购类型

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"repo_type",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getRepoDays(security:list,*args,**kwargs):
    """
	获取回购天数

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"repo_days",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getCrmCarryDate(security:list,*args,**kwargs):
    """
	获取凭证起始日

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"crm_carrydate",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getCrmSubjectCode(security:list,*args,**kwargs):
    """
	获取标的实体交易代码

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"crm_subjectcode",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getCrmPerformGuarantee(security:list,*args,**kwargs):
    """
	获取履约保障机制

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"crm_performguarantee",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getCrmCreditEvent(security:list,*args,**kwargs):
    """
	获取信用事件

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"crm_creditevent",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getCreditBondCreditStatus(security:list,*args,**kwargs):
    """
	获取债券信用状态

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"credit_bondcreditstatus",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIssuerFirstDefaultDate(security:list,*args,**kwargs):
    """
	获取发行人首次违约日

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"issuerfirstdefaultdate",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getCrmRegisterAgency(security:list,*args,**kwargs):
    """
	获取登记机构

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"crm_registeragency",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getCrmSubject(security:list,*args,**kwargs):
    """
	获取标的实体

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"crm_subject",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getCrmIssuer(security:list,*args,**kwargs):
    """
	获取发布机构

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"crm_issuer",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getCrmBookkeepingDate(security:list,*args,**kwargs):
    """
	获取簿记建档日

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"crm_bookkeepingdate",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getCrmPaymentTerms(security:list,*args,**kwargs):
    """
	获取付费方式

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"crm_paymentterms",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getCrmStartingPrice(security:list,*args,**kwargs):
    """
	获取创设价格

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"crm_startingprice",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getCrmPermissionNumber(security:list,*args,**kwargs):
    """
	获取创设批准文件编号

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"crm_permissionnumber",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getCrmDateOfRecord(security:list,*args,**kwargs):
    """
	获取凭证登记日

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"crm_dateofrecord",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundThirdPartyFundType(security:list,*args,**kwargs):
    """
	获取第三方基金分类

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_thirdpartyfundtype",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundProdTypeOcWind(security:list,*args,**kwargs):
    """
	获取Wind封闭式开放式基金分类

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_prodtypeoc_wind",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundFundManagerOfTradeDate(security:list,*args,**kwargs):
    """
	获取基金经理

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_fundmanageroftradedate",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundFundManager(security:list,*args,**kwargs):
    """
	获取基金经理(现任)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_fundmanager",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundPRedFundManager(security:list,*args,**kwargs):
    """
	获取基金经理(历任)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_predfundmanager",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundInceptionFundManager(security:list,*args,**kwargs):
    """
	获取基金经理(成立)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_inceptionfundmanager",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundManagerManagerWorkingYears(security:list,*args,**kwargs):
    """
	获取基金经理年限

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_manager_managerworkingyears",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundAverageWorkingYears(security:list,*args,**kwargs):
    """
	获取基金经理平均年限

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_averageworkingyears",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundMaxWorkingYears(security:list,*args,**kwargs):
    """
	获取基金经理最大年限

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_maxworkingyears",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundManagerIndexReturn(security:list,*args,**kwargs):
    """
	获取基金经理指数区间回报(算术平均)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_managerindex_return",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundManagerIndexStDev(security:list,*args,**kwargs):
    """
	获取基金经理指数收益标准差(算术平均)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_managerindex_stdev",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundManagerIndexStDevYearly(security:list,*args,**kwargs):
    """
	获取基金经理指数年化波动率(算术平均)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_managerindex_stdevyearly",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundManagerIndexMaxDownside(security:list,*args,**kwargs):
    """
	获取基金经理指数最大回撤(算术平均)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_managerindex_maxdownside",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundManagerIndexWeightReturn(security:list,*args,**kwargs):
    """
	获取基金经理指数区间回报(规模加权)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_managerindex_weight_return",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundManagerIndexWeightStDev(security:list,*args,**kwargs):
    """
	获取基金经理指数收益标准差(规模加权)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_managerindex_weight_stdev",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundManagerIndexWeightStDevYearly(security:list,*args,**kwargs):
    """
	获取基金经理指数年化波动率(规模加权)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_managerindex_weight_stdevyearly",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundManagerIndexWeightMaxDownside(security:list,*args,**kwargs):
    """
	获取基金经理指数最大回撤(规模加权)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_managerindex_weight_maxdownside",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundCorpFundManagersNo(security:list,*args,**kwargs):
    """
	获取基金经理数

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_corp_fundmanagersno",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundCorpFundManagerMaturity(security:list,*args,**kwargs):
    """
	获取基金经理成熟度

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_corp_fundmanagermaturity",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundManagerProxyForManager(security:list,*args,**kwargs):
    """
	获取代管基金经理说明

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_manager_proxyformanager",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundManagerIndexBeta(security:list,*args,**kwargs):
    """
	获取Beta(基金经理指数,算术平均)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_managerindex_beta",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundManagerIndexWeightBeta(security:list,*args,**kwargs):
    """
	获取Beta(基金经理指数,规模加权)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_managerindex_weight_beta",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundManagerIndexAlpha(security:list,*args,**kwargs):
    """
	获取Alpha(基金经理指数,算术平均)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_managerindex_alpha",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundManagerIndexWeightAlpha(security:list,*args,**kwargs):
    """
	获取Alpha(基金经理指数,规模加权)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_managerindex_weight_alpha",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundManagerIndexSharpe(security:list,*args,**kwargs):
    """
	获取Sharpe(基金经理指数,算术平均)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_managerindex_sharpe",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundManagerIndexWeightSharpe(security:list,*args,**kwargs):
    """
	获取Sharpe(基金经理指数,规模加权)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_managerindex_weight_sharpe",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundManagerIndexTreyNor(security:list,*args,**kwargs):
    """
	获取Treynor(基金经理指数,算术平均)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_managerindex_treynor",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundManagerIndexWeightTreyNor(security:list,*args,**kwargs):
    """
	获取Treynor(基金经理指数,规模加权)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_managerindex_weight_treynor",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundManagerLongestFundManager(security:list,*args,**kwargs):
    """
	获取任职期限最长的现任基金经理

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_manager_longestfundmanager",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIrFcs(security:list,*args,**kwargs):
    """
	获取基金公司调研次数

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"ir_fcs",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIrNoFci(security:list,*args,**kwargs):
    """
	获取基金公司调研家数

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"ir_nofci",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundReItsFmS(security:list,*args,**kwargs):
    """
	获取网下基金公司或其资管子公司配售数量

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund__reitsfms",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundReItsFMm(security:list,*args,**kwargs):
    """
	获取网下基金公司或其资管子公司配售金额

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund__reitsfmm",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundReItsFMr(security:list,*args,**kwargs):
    """
	获取网下基金公司或其资管子公司配售份额占比

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund__reitsfmr",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundReItsFmAs(security:list,*args,**kwargs):
    """
	获取网下基金公司或其资管计划配售数量

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund__reitsfmas",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundReItsFmAm(security:list,*args,**kwargs):
    """
	获取网下基金公司或其资管机构配售金额

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund__reitsfmam",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundReItsFMar(security:list,*args,**kwargs):
    """
	获取网下基金公司或其资管计划配售份额占比

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund__reitsfmar",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPrtStockValueHoldingIndustryMktValue2(security:list,*args,**kwargs):
    """
	获取所属基金公司重仓行业市值

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"prt_stockvalue_holdingindustrymktvalue2",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIrTmRfc(security:list,*args,**kwargs):
    """
	获取调研最多的基金公司

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"ir_tmrfc",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFtDate(security:list,*args,**kwargs):
    """
	获取开始交易日

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"ftdate",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFtDateNew(security:list,*args,**kwargs):
    """
	获取开始交易日(支持历史)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"ftdate_new",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getLastTradeDate(security:list,*args,**kwargs):
    """
	获取最后交易日

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"lasttrade_date",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getLtDateNew(security:list,*args,**kwargs):
    """
	获取最后交易日(支持历史)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"ltdate_new",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getLtDated(security:list,*args,**kwargs):
    """
	获取最后交易日说明

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"ltdated",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getLastTradingDate(security:list,*args,**kwargs):
    """
	获取最后交易日期

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"lasttradingdate",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getDivLastTrDDateShareB(security:list,*args,**kwargs):
    """
	获取B股最后交易日

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"div_lasttrddateshareb",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getLastTradingDay(security:list,*args,**kwargs):
    """
	获取(废弃)最后交易日

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"lasttradingday",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getRightsIssueRegDateShareB(security:list,*args,**kwargs):
    """
	获取股权登记日(B股最后交易日)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"rightsissue_regdateshareb",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getLastDeliveryDate(security:list,*args,**kwargs):
    """
	获取最后交割日

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"lastdelivery_date",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getLdDateNew(security:list,*args,**kwargs):
    """
	获取最后交割日(支持历史)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"lddate_new",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getDlMonth(security:list,*args,**kwargs):
    """
	获取交割月份

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"dlmonth",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getLPrice(security:list,*args,**kwargs):
    """
	获取挂牌基准价

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"lprice",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getTransactionFee(security:list,*args,**kwargs):
    """
	获取期货交易手续费

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"transactionfee",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getDeliveryFee(security:list,*args,**kwargs):
    """
	获取期货交割手续费

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"deliveryfee",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getTodayPositionFee(security:list,*args,**kwargs):
    """
	获取期货平今手续费

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"todaypositionfee",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getScCode(security:list,*args,**kwargs):
    """
	获取交易品种

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"sccode",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getMargin(security:list,*args,**kwargs):
    """
	获取交易保证金

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"margin",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFtMargins(security:list,*args,**kwargs):
    """
	获取最初交易保证金

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"ftmargins",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getStmNoteSec1853(security:list,*args,**kwargs):
    """
	获取权益乘数(剔除客户交易保证金)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"stmnote_sec_1853",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getLongMargin(security:list,*args,**kwargs):
    """
	获取期货多头保证金(支持历史)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"long_margin",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getShortMargin(security:list,*args,**kwargs):
    """
	获取期货空头保证金(支持历史)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"short_margin",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPunIt(security:list,*args,**kwargs):
    """
	获取报价单位

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"punit",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getChangeLt(security:list,*args,**kwargs):
    """
	获取涨跌幅限制

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"changelt",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getChangeLtNew(security:list,*args,**kwargs):
    """
	获取涨跌幅限制(支持历史)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"changelt_new",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getMfPrice(security:list,*args,**kwargs):
    """
	获取最小变动价位

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"mfprice",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getMfPrice1(security:list,*args,**kwargs):
    """
	获取最小变动价位(支持历史)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"mfprice1",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getContractIssueDate(security:list,*args,**kwargs):
    """
	获取标准合约上市日

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"contract_issuedate",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getExeRatio(security:list,*args,**kwargs):
    """
	获取合约乘数

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"exe_ratio",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getCdMonths(security:list,*args,**kwargs):
    """
	获取合约月份说明

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"cdmonths",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getTHours(security:list,*args,**kwargs):
    """
	获取最新交易时间说明

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"thours",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getDDate(security:list,*args,**kwargs):
    """
	获取交割日期说明

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"ddate",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getTradeHisCode(security:list,*args,**kwargs):
    """
	获取月合约代码

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"trade_hiscode",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIndustryFu(security:list,*args,**kwargs):
    """
	获取期货合约所属行业

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"industry_fu",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getOptionsTradeCode(security:list,*args,**kwargs):
    """
	获取期权代码(指定行权价)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"options_tradecode",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getAtmCode(security:list,*args,**kwargs):
    """
	获取平值期权代码

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"atmcode",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getTradeCode(security:list,*args,**kwargs):
    """
	获取期权交易代码

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"tradecode",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getUsCode(security:list,*args,**kwargs):
    """
	获取标的代码

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"us_code",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getUsName(security:list,*args,**kwargs):
    """
	获取标的简称

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"us_name",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getUsType(security:list,*args,**kwargs):
    """
	获取基础资产/标的类型

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"us_type",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getExeMode(security:list,*args,**kwargs):
    """
	获取行权方式

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"exe_mode",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getExeType(security:list,*args,**kwargs):
    """
	获取行权类型

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"exe_type",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getExePrice(security:list,*args,**kwargs):
    """
	获取行权价格

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"exe_price",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getHolderPriceStockBasedCompensation(security:list,*args,**kwargs):
    """
	获取股权激励行权价格

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"holder_price_stockbasedcompensation",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getMainTMargin(security:list,*args,**kwargs):
    """
	获取期权维持保证金(支持历史)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"maint_margin",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getTotalTm(security:list,*args,**kwargs):
    """
	获取总存续期

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"totaltm",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getStartDate(security:list,*args,**kwargs):
    """
	获取起始交易日期

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"startdate",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getExeStartDate(security:list,*args,**kwargs):
    """
	获取起始行权日期

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"exe_startdate",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getExeEnddate(security:list,*args,**kwargs):
    """
	获取最后行权日期

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"exe_enddate",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getSettlementMethod(security:list,*args,**kwargs):
    """
	获取交割方式

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"settlementmethod",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPreClose(security:list,*args,**kwargs):
    """
	获取前收盘价

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"pre_close",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPreClosePer(security:list,*args,**kwargs):
    """
	获取区间前收盘价

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"pre_close_per",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getUsPreClose(security:list,*args,**kwargs):
    """
	获取标的前收盘价

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"us_preclose",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getCbPqStockPreClose(security:list,*args,**kwargs):
    """
	获取正股区间前收盘价

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"cb_pq_stockpreclose",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getOpen(security:list,*args,**kwargs):
    """
	获取开盘价

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"open",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getOpen3(security:list,*args,**kwargs):
    """
	获取开盘价(不前推)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"open3",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getOpenPer(security:list,*args,**kwargs):
    """
	获取区间开盘价

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"open_per",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getUsOpen(security:list,*args,**kwargs):
    """
	获取标的开盘价

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"us_open",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getCbPqStockOpen(security:list,*args,**kwargs):
    """
	获取正股区间开盘价

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"cb_pq_stockopen",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIpoOpen(security:list,*args,**kwargs):
    """
	获取上市首日开盘价

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"ipo_open",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getHigh(security:list,*args,**kwargs):
    """
	获取最高价

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"high",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getHigh3(security:list,*args,**kwargs):
    """
	获取最高价(不前推)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"high3",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getHighPer(security:list,*args,**kwargs):
    """
	获取区间最高价

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"high_per",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getHighDatePer(security:list,*args,**kwargs):
    """
	获取区间最高价日

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"high_date_per",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getUsHigh(security:list,*args,**kwargs):
    """
	获取标的最高价

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"us_high",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPctChgLowestPer(security:list,*args,**kwargs):
    """
	获取区间自最高价的最大跌幅

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"pct_chg_lowest_per",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getCbPqStockHigh(security:list,*args,**kwargs):
    """
	获取正股区间最高价

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"cb_pq_stockhigh",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIpoHigh(security:list,*args,**kwargs):
    """
	获取上市首日最高价

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"ipo_high",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPohQe(security:list,*args,**kwargs):
    """
	获取被剔除的最高价申报量占比

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"pohqe",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPctChgLowPer(security:list,*args,**kwargs):
    """
	获取最新价较区间最高价跌幅(回撤)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"pct_chg_low_per",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getTechLnHighLow20D(security:list,*args,**kwargs):
    """
	获取LN(最近一个月最高价/最近一个月最低价)_PIT

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"tech_lnhighlow20d",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getLow(security:list,*args,**kwargs):
    """
	获取最低价

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"low",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getLow3(security:list,*args,**kwargs):
    """
	获取最低价(不前推)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"low3",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getLowPer(security:list,*args,**kwargs):
    """
	获取区间最低价

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"low_per",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getLowDatePer(security:list,*args,**kwargs):
    """
	获取区间最低价日

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"low_date_per",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getUsLow(security:list,*args,**kwargs):
    """
	获取标的最低价

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"us_low",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPctChgHighestPer(security:list,*args,**kwargs):
    """
	获取区间自最低价的最大涨幅

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"pct_chg_highest_per",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getCbPqStockLow(security:list,*args,**kwargs):
    """
	获取正股区间最低价

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"cb_pq_stocklow",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIpoLow(security:list,*args,**kwargs):
    """
	获取上市首日最低价

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"ipo_low",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getEstPctChange(security:list,*args,**kwargs):
    """
	获取预测涨跌幅(评级日,最低价)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"est_pctchange",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getClose(security:list,*args,**kwargs):
    """
	获取收盘价

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"close",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getClose2(security:list,*args,**kwargs):
    """
	获取收盘价(支持定点复权)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"close2",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getClose3(security:list,*args,**kwargs):
    """
	获取收盘价(不前推)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"close3",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getCloseFx(security:list,*args,**kwargs):
    """
	获取收盘价(23:30)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"close_FX",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getCloseUsd(security:list,*args,**kwargs):
    """
	获取收盘价(美元)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"close_usd",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getCloseNight(security:list,*args,**kwargs):
    """
	获取收盘价(夜盘)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"close_night",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getRiskStDevClose(security:list,*args,**kwargs):
    """
	获取收盘价标准差

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"risk_stdevclose",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getDirtyPrice(security:list,*args,**kwargs):
    """
	获取收盘价(全价)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"dirtyprice",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getCleanPrice(security:list,*args,**kwargs):
    """
	获取收盘价(净价)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"cleanprice",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getDuration(security:list,*args,**kwargs):
    """
	获取收盘价久期

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"duration",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getModifiedDuration(security:list,*args,**kwargs):
    """
	获取收盘价修正久期

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"modifiedduration",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getConvexity(security:list,*args,**kwargs):
    """
	获取收盘价凸性

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"convexity",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getClosePer(security:list,*args,**kwargs):
    """
	获取区间收盘价

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"close_per",*args,**kwargs,usedf=True)
@convertInputSecurityType
def get1StQuartIle(security:list,*args,**kwargs):
    """
	获取N日收盘价1/4分位数

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"1stquartile",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getMedian(security:list,*args,**kwargs):
    """
	获取N日收盘价中位数

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"median",*args,**kwargs,usedf=True)
@convertInputSecurityType
def get3RdQuartIle(security:list,*args,**kwargs):
    """
	获取N日收盘价3/4分位数

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"3rdquartile",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getUsClose(security:list,*args,**kwargs):
    """
	获取标的收盘价

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"us_close",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getTechTrix5(security:list,*args,**kwargs):
    """
	获取5日收盘价三重指数平滑移动平均指标_PIT

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"tech_trix5",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getNQOriginClose(security:list,*args,**kwargs):
    """
	获取推N日收盘价(债券)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"nq_originclose",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getNQClose(security:list,*args,**kwargs):
    """
	获取推N日收盘价(当日结算价)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"nq_close",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getTechTrix10(security:list,*args,**kwargs):
    """
	获取10日收盘价三重指数平滑移动平均指标_PIT

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"tech_trix10",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPctChangeClose(security:list,*args,**kwargs):
    """
	获取涨跌幅(收盘价)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"pctchange_close",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getCbPqStockClose(security:list,*args,**kwargs):
    """
	获取正股区间收盘价

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"cb_pq_stockclose",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getMaxClosePer(security:list,*args,**kwargs):
    """
	获取区间最高收盘价

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"max_close_per",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getMinClosePer(security:list,*args,**kwargs):
    """
	获取区间最低收盘价

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"min_close_per",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getMaxCloseDatePer(security:list,*args,**kwargs):
    """
	获取区间最高收盘价日

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"max_close_date_per",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getMinCloseDatePer(security:list,*args,**kwargs):
    """
	获取区间最低收盘价日

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"min_close_date_per",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getAvgClosePer(security:list,*args,**kwargs):
    """
	获取N日日均收盘价(算术平均)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"avgclose_per",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIpoClose(security:list,*args,**kwargs):
    """
	获取上市首日收盘价

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"ipo_close",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIpoLimitUpOpenDateClose(security:list,*args,**kwargs):
    """
	获取新股开板日收盘价

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"ipo_limitupopendate_close",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getTechBBic(security:list,*args,**kwargs):
    """
	获取BBI除以收盘价_PIT

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"tech_bbic",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getCloseFixedIncome(security:list,*args,**kwargs):
    """
	获取上证固收平台收盘价

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"close_fixedincome",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getCbPqStockHighClose(security:list,*args,**kwargs):
    """
	获取正股区间最高收盘价

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"cb_pq_stockhighclose",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getCbPqStockLowClose(security:list,*args,**kwargs):
    """
	获取正股区间最低收盘价

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"cb_pq_stocklowclose",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getVolume(security:list,*args,**kwargs):
    """
	获取成交量

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"volume",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getVolumEBTIn(security:list,*args,**kwargs):
    """
	获取成交量(含大宗交易)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"volume_btin",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getOiVolumeC(security:list,*args,**kwargs):
    """
	获取成交量比上交易日增减

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"oi_volumec",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getOiVName(security:list,*args,**kwargs):
    """
	获取成交量进榜会员名称

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"oi_vname",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getVolumeRatio(security:list,*args,**kwargs):
    """
	获取成交量认沽认购比率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"volumeratio",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getTechVemA5(security:list,*args,**kwargs):
    """
	获取成交量的5日指数移动平均_PIT

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"tech_vema5",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getTechVemA10(security:list,*args,**kwargs):
    """
	获取成交量的10日指数移动平均_PIT

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"tech_vema10",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getTechVemA12(security:list,*args,**kwargs):
    """
	获取成交量的12日指数移动平均_PIT

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"tech_vema12",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getTechVemA26(security:list,*args,**kwargs):
    """
	获取成交量的26日指数移动平均_PIT

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"tech_vema26",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getTechVmaCd(security:list,*args,**kwargs):
    """
	获取成交量量指数平滑异同移动平均线_PIT

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"tech_vmacd",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getTechVr(security:list,*args,**kwargs):
    """
	获取成交量比率_PIT

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"tech_vr",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getTechVosC(security:list,*args,**kwargs):
    """
	获取成交量震荡_PIT

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"tech_vosc",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getTechPvI(security:list,*args,**kwargs):
    """
	获取正成交量指标_PIT

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"tech_pvi",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getTechNVi(security:list,*args,**kwargs):
    """
	获取负成交量指标_PIT

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"tech_nvi",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getVolumeAHt(security:list,*args,**kwargs):
    """
	获取盘后成交量

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"volume_aht",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getVolPer(security:list,*args,**kwargs):
    """
	获取区间成交量

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"vol_per",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPqBlockTradeVolume(security:list,*args,**kwargs):
    """
	获取区间成交量(含大宗交易)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"pq_blocktradevolume",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getVolNd(security:list,*args,**kwargs):
    """
	获取N日成交量

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"vol_nd",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getUsVolume(security:list,*args,**kwargs):
    """
	获取标的成交量

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"us_volume",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getOiVolume(security:list,*args,**kwargs):
    """
	获取会员成交量

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"oi_volume",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getOptionVolume(security:list,*args,**kwargs):
    """
	获取品种成交量

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"optionvolume",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getCallVolume(security:list,*args,**kwargs):
    """
	获取认购成交量

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"callvolume",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPutVolume(security:list,*args,**kwargs):
    """
	获取认沽成交量

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"putvolume",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getTechVsTd10(security:list,*args,**kwargs):
    """
	获取10日成交量标准差_PIT

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"tech_vstd10",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getTechVsTd20(security:list,*args,**kwargs):
    """
	获取20日成交量标准差_PIT

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"tech_vstd20",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getCbPqStockVol(security:list,*args,**kwargs):
    """
	获取正股区间成交量

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"cb_pq_stockvol",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getAvgVolPer(security:list,*args,**kwargs):
    """
	获取区间日均成交量

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"avg_vol_per",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPqVolumeAHt(security:list,*args,**kwargs):
    """
	获取区间盘后成交量

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"pq_volume_aht",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getShortSellVolumePct(security:list,*args,**kwargs):
    """
	获取卖空量占成交量比率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"shortsell_VolumePct",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getVsTd(security:list,*args,**kwargs):
    """
	获取VSTD成交量标准差

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"VSTD",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIpoListDayVolume(security:list,*args,**kwargs):
    """
	获取上市首日成交量

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"ipo_listdayvolume",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getOpenAuctionVolume(security:list,*args,**kwargs):
    """
	获取开盘集合竞价成交量

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"open_auction_volume",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getVolumeFixedIncome(security:list,*args,**kwargs):
    """
	获取上证固收平台成交量

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"volume_fixedincome",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getAmt(security:list,*args,**kwargs):
    """
	获取成交额

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"amt",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getAmountBtIn(security:list,*args,**kwargs):
    """
	获取成交额(含大宗交易)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"amount_btin",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getTechAmount1M60(security:list,*args,**kwargs):
    """
	获取成交额惯性_PIT

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"tech_amount1m60",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getAmountAHt(security:list,*args,**kwargs):
    """
	获取盘后成交额

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"amount_aht",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getAmtPer(security:list,*args,**kwargs):
    """
	获取区间成交额

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"amt_per",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPqBlockTradeAmounts(security:list,*args,**kwargs):
    """
	获取区间成交额(含大宗交易)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"pq_blocktradeamounts",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getAmtNd(security:list,*args,**kwargs):
    """
	获取N日成交额

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"amt_nd",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getUsAmount(security:list,*args,**kwargs):
    """
	获取标的成交额

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"us_amount",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getOptionAmount(security:list,*args,**kwargs):
    """
	获取品种成交额

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"optionamount",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getCallAmount(security:list,*args,**kwargs):
    """
	获取认购成交额

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"callamount",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPutAmount(security:list,*args,**kwargs):
    """
	获取认沽成交额

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"putamount",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getCbPqStockAmNt(security:list,*args,**kwargs):
    """
	获取正股区间成交额

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"cb_pq_stockamnt",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getAvgAmtPer(security:list,*args,**kwargs):
    """
	获取区间日均成交额

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"avg_amt_per",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPqAmountAHt(security:list,*args,**kwargs):
    """
	获取区间盘后成交额

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"pq_amount_aht",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIpoVolume(security:list,*args,**kwargs):
    """
	获取上市首日成交额

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"ipo_volume",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getOpenAuctionAmount(security:list,*args,**kwargs):
    """
	获取开盘集合竞价成交额

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"open_auction_amount",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getDealNum(security:list,*args,**kwargs):
    """
	获取成交笔数

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"dealnum",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getDealNumFixedIncome(security:list,*args,**kwargs):
    """
	获取上证固收平台成交笔数

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"dealnum_fixedincome",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getChg(security:list,*args,**kwargs):
    """
	获取涨跌

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"chg",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPctChg(security:list,*args,**kwargs):
    """
	获取涨跌幅

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"pct_chg",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPctChgB(security:list,*args,**kwargs):
    """
	获取涨跌幅(债券)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"pct_chg_b",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getChgSettlement(security:list,*args,**kwargs):
    """
	获取涨跌(结算价)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"chg_settlement",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPctChgSettlement(security:list,*args,**kwargs):
    """
	获取涨跌幅(结算价)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"pct_chg_settlement",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getMaxUpOrDown(security:list,*args,**kwargs):
    """
	获取涨跌停状态

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"maxupordown",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getDQChangeCnBd(security:list,*args,**kwargs):
    """
	获取涨跌(中债)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"dq_change_cnbd",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getDQPctChangeCnBd(security:list,*args,**kwargs):
    """
	获取涨跌幅(中债)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"dq_pctchange_cnbd",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getChgPer(security:list,*args,**kwargs):
    """
	获取区间涨跌

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"chg_per",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPctChgPer(security:list,*args,**kwargs):
    """
	获取区间涨跌幅

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"pct_chg_per",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPctChgPer2(security:list,*args,**kwargs):
    """
	获取区间涨跌幅(包含上市首日涨跌幅)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"pct_chg_per2",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPctChgNd(security:list,*args,**kwargs):
    """
	获取N日涨跌幅

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"pct_chg_nd",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFsPqChangeSettlement(security:list,*args,**kwargs):
    """
	获取区间涨跌(结算价)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fs_pq_change_settlement",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFsPqPctChangeSettlement(security:list,*args,**kwargs):
    """
	获取区间涨跌幅(结算价)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fs_pq_pctchange_settlement",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWestReturn(security:list,*args,**kwargs):
    """
	获取估算涨跌幅

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"west_return",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWestReturnError(security:list,*args,**kwargs):
    """
	获取估算涨跌幅误差

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"west_return_error",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getUsChange(security:list,*args,**kwargs):
    """
	获取标的涨跌

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"us_change",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getUsPctChange(security:list,*args,**kwargs):
    """
	获取标的涨跌幅

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"us_pctchange",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPctChg5D(security:list,*args,**kwargs):
    """
	获取近5日涨跌幅

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"pct_chg_5d",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPctChg1M(security:list,*args,**kwargs):
    """
	获取近1月涨跌幅

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"pct_chg_1m",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPctChg3M(security:list,*args,**kwargs):
    """
	获取近3月涨跌幅

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"pct_chg_3m",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPctChg6M(security:list,*args,**kwargs):
    """
	获取近6月涨跌幅

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"pct_chg_6m",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPctChg1Y(security:list,*args,**kwargs):
    """
	获取近1年涨跌幅

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"pct_chg_1y",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPrtHeavilyHeldStocksPerChange(security:list,*args,**kwargs):
    """
	获取重仓股涨跌幅

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"prt_heavilyheldstocksperchange",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundAbnormalNavFluctuation(security:list,*args,**kwargs):
    """
	获取净值异常涨跌幅说明

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_abnormalnavfluctuation",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getCbPqStockChg(security:list,*args,**kwargs):
    """
	获取正股区间涨跌

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"cb_pq_stockchg",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getCbPqStockPctChg(security:list,*args,**kwargs):
    """
	获取正股区间涨跌幅

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"cb_pq_stockpctchg",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getAvgPctChgNd(security:list,*args,**kwargs):
    """
	获取N日日均涨跌幅

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"avg_pct_chg_nd",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPctChg10D(security:list,*args,**kwargs):
    """
	获取近10日涨跌幅

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"pct_chg_10d",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIpoPctChange(security:list,*args,**kwargs):
    """
	获取上市首日涨跌幅

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"ipo_pctchange",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPrtHeavilyHeldBondsPerChange(security:list,*args,**kwargs):
    """
	获取重仓债券涨跌幅

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"prt_heavilyheldbondsperchange",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPrtHeavilyHeldFundPerChange(security:list,*args,**kwargs):
    """
	获取重仓基金涨跌幅

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"prt_heavilyheldfundperchange",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getRelIpoChg(security:list,*args,**kwargs):
    """
	获取相对发行价涨跌

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"rel_ipo_chg",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getRelIpoPctChg(security:list,*args,**kwargs):
    """
	获取相对发行价涨跌幅

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"rel_ipo_pct_chg",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIpoNpcTChange(security:list,*args,**kwargs):
    """
	获取上市后N日涨跌幅

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"ipo_npctchange",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIpoLimitUpOpenDatePctChange(security:list,*args,**kwargs):
    """
	获取新股开板日涨跌幅

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"ipo_limitupopendate_pctchange",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getRelPctChange(security:list,*args,**kwargs):
    """
	获取区间相对指数涨跌幅

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"relpctchange",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPqRelPctChange(security:list,*args,**kwargs):
    """
	获取相对大盘区间涨跌幅

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"pq_relpctchange",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getNQRelPctChange(security:list,*args,**kwargs):
    """
	获取相对大盘N日涨跌幅

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"nq_relpctchange",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPqRelPctChangeYTd(security:list,*args,**kwargs):
    """
	获取年迄今相对指数涨跌幅

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"pq_relpctchange_ytd",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPqRelPctChange5D(security:list,*args,**kwargs):
    """
	获取近5日相对指数涨跌幅

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"pq_relpctchange_5d",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPqRelPctChange1M(security:list,*args,**kwargs):
    """
	获取近1月相对指数涨跌幅

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"pq_relpctchange_1m",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPqRelPctChange3M(security:list,*args,**kwargs):
    """
	获取近3月相对指数涨跌幅

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"pq_relpctchange_3m",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPqRelPctChange6M(security:list,*args,**kwargs):
    """
	获取近6月相对指数涨跌幅

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"pq_relpctchange_6m",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPqRelPctChange1Y(security:list,*args,**kwargs):
    """
	获取近1年相对指数涨跌幅

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"pq_relpctchange_1y",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPqRelPctChangeMTd(security:list,*args,**kwargs):
    """
	获取本月至今相对指数涨跌幅

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"pq_relpctchange_mtd",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPqRelRelPctChangeMTd(security:list,*args,**kwargs):
    """
	获取季度至今相对指数涨跌幅

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"pq_relrelpctchange_mtd",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPqRelPctChange10D(security:list,*args,**kwargs):
    """
	获取近10日相对指数涨跌幅

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"pq_relpctchange_10d",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getSwing(security:list,*args,**kwargs):
    """
	获取振幅

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"swing",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getSwingPer(security:list,*args,**kwargs):
    """
	获取区间振幅

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"swing_per",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getSwingNd(security:list,*args,**kwargs):
    """
	获取N日振幅

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"swing_nd",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getUsSwing(security:list,*args,**kwargs):
    """
	获取标的振幅

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"us_swing",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getCbPqStockSwing(security:list,*args,**kwargs):
    """
	获取正股区间振幅

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"cb_pq_stockswing",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getAvgSwingPer(security:list,*args,**kwargs):
    """
	获取区间日均振幅

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"avg_swing_per",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getVWap(security:list,*args,**kwargs):
    """
	获取均价

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"vwap",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getUsAvgPrice(security:list,*args,**kwargs):
    """
	获取标的均价

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"us_avgprice",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIpoPrePrice(security:list,*args,**kwargs):
    """
	获取发行前均价

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"ipo_preprice",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getCbPqStockAvg(security:list,*args,**kwargs):
    """
	获取正股区间均价

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"cb_pq_stockavg",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getVWapPer(security:list,*args,**kwargs):
    """
	获取区间成交均价

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"vwap_per",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPqAvgPrice2(security:list,*args,**kwargs):
    """
	获取区间成交均价(可复权)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"pq_avgprice2",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getNQAvgPrice(security:list,*args,**kwargs):
    """
	获取N日成交均价

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"nq_avgprice",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getClauseResetReferencePriceIsAnVerAge(security:list,*args,**kwargs):
    """
	获取是否为算术平均价

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"clause_reset_referencepriceisanverage",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIpoAvgPrice(security:list,*args,**kwargs):
    """
	获取上市首日成交均价

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"ipo_avgprice",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getAvgPriceFixedIncome(security:list,*args,**kwargs):
    """
	获取上证固收平台平均价

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"avgprice_fixedincome",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIpoLimitUpOpenDateAvgPrice(security:list,*args,**kwargs):
    """
	获取新股开板日成交均价

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"ipo_limitupopendate_avgprice",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getAdjFactor(security:list,*args,**kwargs):
    """
	获取复权因子

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"adjfactor",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getNavAdjFactor(security:list,*args,**kwargs):
    """
	获取基金净值复权因子

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"NAV_adjfactor",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getTurn(security:list,*args,**kwargs):
    """
	获取换手率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"turn",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFreeTurn(security:list,*args,**kwargs):
    """
	获取换手率(基准.自由流通股本)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"free_turn",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getTechTurnoverRateVolatility20(security:list,*args,**kwargs):
    """
	获取换手率相对波动率_PIT

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"tech_turnoverratevolatility20",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getTurnPer(security:list,*args,**kwargs):
    """
	获取区间换手率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"turn_per",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getTurnFreePer(security:list,*args,**kwargs):
    """
	获取区间换手率(基准.自由流通股本)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"turn_free_per",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getTurnNd(security:list,*args,**kwargs):
    """
	获取N日换手率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"turn_nd",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getUsTurn(security:list,*args,**kwargs):
    """
	获取标的换手率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"us_turn",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getTechSToQ(security:list,*args,**kwargs):
    """
	获取3个月换手率对数平均_PIT

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"tech_stoq",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getCbPqStockTurnover(security:list,*args,**kwargs):
    """
	获取正股区间换手率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"cb_pq_stockturnover",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPqAvgTurn2(security:list,*args,**kwargs):
    """
	获取区间日均换手率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"pq_avgturn2",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getAvgTurnPer(security:list,*args,**kwargs):
    """
	获取区间日均换手率(剔除无成交日期)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"avg_turn_per",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getAvgTurnFreePer(security:list,*args,**kwargs):
    """
	获取区间日均换手率(基准.自由流通股本)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"avg_turn_free_per",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getAvgTurnNd(security:list,*args,**kwargs):
    """
	获取N日日均换手率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"avg_turn_nd",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIpoTurn(security:list,*args,**kwargs):
    """
	获取上市首日换手率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"ipo_turn",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getTechTurnoverRate5(security:list,*args,**kwargs):
    """
	获取5日平均换手率_PIT

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"tech_turnoverrate5",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getTechSToA(security:list,*args,**kwargs):
    """
	获取12个月换手率对数平均_PIT

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"tech_stoa",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getTechTurn5DTurn120(security:list,*args,**kwargs):
    """
	获取5日平均换手率/120日平均换手率_PIT

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"tech_turn5dturn120",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIpoNTurn(security:list,*args,**kwargs):
    """
	获取上市后N日换手率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"ipo_nturn",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getTechTurnoverRate10(security:list,*args,**kwargs):
    """
	获取10日平均换手率_PIT

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"tech_turnoverrate10",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getTechTurnoverRate20(security:list,*args,**kwargs):
    """
	获取20日平均换手率_PIT

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"tech_turnoverrate20",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getTechTurnoverRate60(security:list,*args,**kwargs):
    """
	获取60日平均换手率_PIT

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"tech_turnoverrate60",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getTechTurn10DTurn120(security:list,*args,**kwargs):
    """
	获取10日平均换手率/120日平均换手率_PIT

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"tech_turn10dturn120",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getTechTurn20DTurn120(security:list,*args,**kwargs):
    """
	获取20日平均换手率/120日平均换手率_PIT

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"tech_turn20dturn120",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getCbPqStockAveTurnover(security:list,*args,**kwargs):
    """
	获取正股区间平均换手率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"cb_pq_stockaveturnover",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getTechTurnoverRate120(security:list,*args,**kwargs):
    """
	获取120日平均换手率_PIT

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"tech_turnoverrate120",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getTechTurnoverRate240(security:list,*args,**kwargs):
    """
	获取240日平均换手率_PIT

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"tech_turnoverrate240",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getStyleRpTTurn(security:list,*args,**kwargs):
    """
	获取基金报告期持仓换手率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"style_rpt_turn",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getOi(security:list,*args,**kwargs):
    """
	获取持仓量

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"oi",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getOiChg(security:list,*args,**kwargs):
    """
	获取持仓量变化

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"oi_chg",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getOiIndex(security:list,*args,**kwargs):
    """
	获取持仓量(商品指数)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"oi_index",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getOiChange(security:list,*args,**kwargs):
    """
	获取持仓量变化(商品指数)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"oichange",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getOi3(security:list,*args,**kwargs):
    """
	获取持仓量(不前推)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"oi3",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getOiRatio(security:list,*args,**kwargs):
    """
	获取持仓量认沽认购比率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"oiratio",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getOiPer(security:list,*args,**kwargs):
    """
	获取区间持仓量

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"oi_per",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getOptionOi(security:list,*args,**kwargs):
    """
	获取品种持仓量

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"optionoi",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getCallOi(security:list,*args,**kwargs):
    """
	获取认购持仓量

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"calloi",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPutOi(security:list,*args,**kwargs):
    """
	获取认沽持仓量

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"putoi",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getAvgOiPer(security:list,*args,**kwargs):
    """
	获取区间日均持仓量

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"avg_oi_per",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getOiAmountNoMargin(security:list,*args,**kwargs):
    """
	获取持仓额(不计保证金)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"oiamount_nomargin",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getOiAmount(security:list,*args,**kwargs):
    """
	获取持仓额

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"oiamount",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPreSettle(security:list,*args,**kwargs):
    """
	获取前结算价

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"pre_settle",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPreSettlePer(security:list,*args,**kwargs):
    """
	获取区间前结算价

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"pre_settle_per",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getSettle(security:list,*args,**kwargs):
    """
	获取结算价

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"settle",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getSettle3(security:list,*args,**kwargs):
    """
	获取结算价(不前推)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"settle3",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getSettlePer(security:list,*args,**kwargs):
    """
	获取区间结算价

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"settle_per",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWeightModiDura(security:list,*args,**kwargs):
    """
	获取加权平均结算价修正久期(中债)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"weight_modidura",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWeightSprDura(security:list,*args,**kwargs):
    """
	获取加权平均结算价利差久期(中债)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"weight_sprdura",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWeightInterestDuration(security:list,*args,**kwargs):
    """
	获取加权平均结算价利率久期(中债)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"weight_interestduration",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWeightVoBp(security:list,*args,**kwargs):
    """
	获取加权平均结算价基点价值(中债)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"weight_vobp",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWeightCNvXTy(security:list,*args,**kwargs):
    """
	获取加权平均结算价凸性(中债)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"weight_cnvxty",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWeightSPrcNxt(security:list,*args,**kwargs):
    """
	获取加权平均结算价利差凸性(中债)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"weight_sprcnxt",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWeightInterestCNvXTy(security:list,*args,**kwargs):
    """
	获取加权平均结算价利率凸性(中债)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"weight_interestcnvxty",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getLowSettlePer(security:list,*args,**kwargs):
    """
	获取区间最低结算价

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"low_settle_per",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getHighSettlePer(security:list,*args,**kwargs):
    """
	获取区间最高结算价

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"high_settle_per",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFsPqHighSwingDate(security:list,*args,**kwargs):
    """
	获取区间最高结算价日

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fs_pq_highswing_date",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFsPqLowSwingDate(security:list,*args,**kwargs):
    """
	获取区间最低结算价日

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fs_pq_lowswing_date",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getLasTradeDayS(security:list,*args,**kwargs):
    """
	获取最近交易日期

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"lastradeday_s",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFirsTradeDayS(security:list,*args,**kwargs):
    """
	获取最早交易日期

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"firstradeday_s",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getLastTradeDay(security:list,*args,**kwargs):
    """
	获取市场最近交易日

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"last_trade_day",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getTradeStatus(security:list,*args,**kwargs):
    """
	获取交易状态

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"trade_status",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getValMvArd(security:list,*args,**kwargs):
    """
	获取总市值

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"val_mv_ARD",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getEv(security:list,*args,**kwargs):
    """
	获取总市值1

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"ev",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getMktCapArd(security:list,*args,**kwargs):
    """
	获取总市值2

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"mkt_cap_ard",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getEv3(security:list,*args,**kwargs):
    """
	获取总市值1(币种可选)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"ev3",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getMktCap(security:list,*args,**kwargs):
    """
	获取总市值(不可回测)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"mkt_cap",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getMktCapCsrC(security:list,*args,**kwargs):
    """
	获取总市值(证监会算法)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"mkt_cap_CSRC",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getValMvToeBitDaTtM(security:list,*args,**kwargs):
    """
	获取总市值/EBITDA(TTM反推法)_PIT

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"val_mvtoebitda_ttm",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getValPeBitDaInDuSwTtM(security:list,*args,**kwargs):
    """
	获取总市值/息税折旧及摊销前利润TTM行业相对值_PIT

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"val_pebitdaindu_sw_ttm",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getMvRef(security:list,*args,**kwargs):
    """
	获取参考总市值

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"mv_ref",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getValMv(security:list,*args,**kwargs):
    """
	获取指数总市值

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"val_mv",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getMamV(security:list,*args,**kwargs):
    """
	获取备考总市值(并购后)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"mamv",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getEquityToDebt2(security:list,*args,**kwargs):
    """
	获取当日总市值/负债总计

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"equitytodebt2",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getAvgMvPer(security:list,*args,**kwargs):
    """
	获取区间日均总市值

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"avg_MV_per",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getValAvgPeBitDaSw(security:list,*args,**kwargs):
    """
	获取所属申万一级行业的总市值/息税折旧及摊销前利润TTM均值_PIT

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"val_avgpebitda_sw",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getValStdPeBitDaSw(security:list,*args,**kwargs):
    """
	获取所属申万一级行业的总市值/息税折旧及摊销前利润TTM标准差_PIT

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"val_stdpebitda_sw",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getMarginMarketValueRatio(security:list,*args,**kwargs):
    """
	获取担保证券市值占该证券总市值比重

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"margin_marketvalueratio",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getValMvC(security:list,*args,**kwargs):
    """
	获取流通市值

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"val_mvc",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getMktCapFloat(security:list,*args,**kwargs):
    """
	获取流通市值(含限售股)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"mkt_cap_float",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getMktFreeShares(security:list,*args,**kwargs):
    """
	获取自由流通市值

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"mkt_freeshares",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getValFloatMv(security:list,*args,**kwargs):
    """
	获取自由流通市值_PIT

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"val_floatmv",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getValLnFloatMv(security:list,*args,**kwargs):
    """
	获取对数流通市值_PIT

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"val_lnfloatmv",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPqAvgMvNonRestricted(security:list,*args,**kwargs):
    """
	获取区间日均流通市值

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"pq_avgmv_nonrestricted",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getSUspDays(security:list,*args,**kwargs):
    """
	获取连续停牌天数

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"susp_days",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getSUspReason(security:list,*args,**kwargs):
    """
	获取停牌原因

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"susp_reason",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getMaxUp(security:list,*args,**kwargs):
    """
	获取涨停价

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"maxup",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getMaxDown(security:list,*args,**kwargs):
    """
	获取跌停价

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"maxdown",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getDiscount(security:list,*args,**kwargs):
    """
	获取贴水

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"discount",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getDiscountRatio(security:list,*args,**kwargs):
    """
	获取贴水率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"discount_ratio",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getAvgDiscountPer(security:list,*args,**kwargs):
    """
	获取区间均贴水

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"avg_discount_per",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getAvgDiscountRatioPer(security:list,*args,**kwargs):
    """
	获取区间均贴水率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"avg_discount_ratio_per",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIndexWeight(security:list,*args,**kwargs):
    """
	获取所属指数权重

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"indexweight",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getDirectionGold(security:list,*args,**kwargs):
    """
	获取交收方向(黄金现货)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"direction_gold",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getDQuantityGold(security:list,*args,**kwargs):
    """
	获取交收量(黄金现货)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"dquantity_gold",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getOpenAuctionPrice(security:list,*args,**kwargs):
    """
	获取开盘集合竞价成交价

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"open_auction_price",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPctChgHighPer(security:list,*args,**kwargs):
    """
	获取区间收盘最大涨幅

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"pct_chg_high_per",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getTradeDaysPer(security:list,*args,**kwargs):
    """
	获取区间交易天数

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"trade_days_per",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getLimitUpDaysPer(security:list,*args,**kwargs):
    """
	获取区间涨停天数

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"limitupdays_per",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getLimitDownDaysPer(security:list,*args,**kwargs):
    """
	获取区间跌停天数

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"limitdowndays_per",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPqUpDaysPer(security:list,*args,**kwargs):
    """
	获取区间上涨天数

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"pq_updays_per",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPqDownDaysPer(security:list,*args,**kwargs):
    """
	获取区间下跌天数

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"pq_downdays_per",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getQuoteDaysPer(security:list,*args,**kwargs):
    """
	获取区间报价天数

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"quote_days_per",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getOiChgPer(security:list,*args,**kwargs):
    """
	获取区间持仓变化

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"oi_chg_per",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getMfAmtOpenPer(security:list,*args,**kwargs):
    """
	获取区间开盘净主动买入额

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"mf_amt_open_per",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getMfAmtClosePer(security:list,*args,**kwargs):
    """
	获取区间尾盘净主动买入额

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"mf_amt_close_per",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getMfVolPer(security:list,*args,**kwargs):
    """
	获取区间净主动买入量

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"mf_vol_per",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getMfVolRatioPer(security:list,*args,**kwargs):
    """
	获取区间净主动买入量占比

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"mf_vol_ratio_per",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getMfAmtPer(security:list,*args,**kwargs):
    """
	获取区间净主动买入额

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"mf_amt_per",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getMfAmtRatioPer(security:list,*args,**kwargs):
    """
	获取区间净主动买入率(金额)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"mf_amt_ratio_per",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getMfdInFlowDays(security:list,*args,**kwargs):
    """
	获取区间主力净流入天数

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"mfd_inflowdays",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getMfBuyAmt(security:list,*args,**kwargs):
    """
	获取区间流入额

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"mf_buy_amt",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getMfBuyVol(security:list,*args,**kwargs):
    """
	获取区间流入量

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"mf_buy_vol",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getMfSellAmt(security:list,*args,**kwargs):
    """
	获取区间流出额

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"mf_sell_amt",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getMfSellVol(security:list,*args,**kwargs):
    """
	获取区间流出量

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"mf_sell_vol",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPqBlockTradeNum(security:list,*args,**kwargs):
    """
	获取区间大宗交易上榜次数

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"pq_blocktradenum",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPqBlockTradeAmount(security:list,*args,**kwargs):
    """
	获取区间大宗交易成交总额

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"pq_blocktradeamount",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPqAbnormalTradeNum(security:list,*args,**kwargs):
    """
	获取区间龙虎榜上榜次数

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"pq_abnormaltradenum",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPqAbnormalTradeLp(security:list,*args,**kwargs):
    """
	获取区间龙虎榜买入额

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"pq_abnormaltrade_lp",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getTradeDay(security:list,*args,**kwargs):
    """
	获取指定日相近交易日期

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"tradeday",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPeriodMfNetInFlow(security:list,*args,**kwargs):
    """
	获取区间净流入额

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"periodmf_netinflow",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getMrgLongAmt(security:list,*args,**kwargs):
    """
	获取融资买入额

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"mrg_long_amt",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getMrgLongAmtInt(security:list,*args,**kwargs):
    """
	获取区间融资买入额

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"mrg_long_amt_int",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getMrgLongRepay(security:list,*args,**kwargs):
    """
	获取融资偿还额

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"mrg_long_repay",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getMrgLongRepayInt(security:list,*args,**kwargs):
    """
	获取区间融资偿还额

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"mrg_long_repay_int",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getMrgLongBal(security:list,*args,**kwargs):
    """
	获取融资余额

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"mrg_long_bal",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getMrgLongBalIntAvg(security:list,*args,**kwargs):
    """
	获取区间融资余额均值

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"mrg_long_bal_int_avg",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getMmRepurchase1(security:list,*args,**kwargs):
    """
	获取报告期内债券回购融资余额

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"mmrepurchase1",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getMmRepurchase2(security:list,*args,**kwargs):
    """
	获取报告期末债券回购融资余额

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"mmrepurchase2",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getMmRepurchase1ToNav(security:list,*args,**kwargs):
    """
	获取报告期内债券回购融资余额占基金资产净值比例

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"mmrepurchase1tonav",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getMmRepurchase2ToNav(security:list,*args,**kwargs):
    """
	获取报告期末债券回购融资余额占基金资产净值比例

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"mmrepurchase2tonav",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getMrgShortVol(security:list,*args,**kwargs):
    """
	获取融券卖出量

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"mrg_short_vol",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getMrgShortVolInt(security:list,*args,**kwargs):
    """
	获取区间融券卖出量

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"mrg_short_vol_int",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getMrgShortVolRepay(security:list,*args,**kwargs):
    """
	获取融券偿还量

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"mrg_short_vol_repay",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getMrgShortVolRepayInt(security:list,*args,**kwargs):
    """
	获取区间融券偿还量

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"mrg_short_vol_repay_int",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getMarginSaleTradingAmount(security:list,*args,**kwargs):
    """
	获取融券卖出额

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"margin_saletradingamount",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getMarginShortAmountInt(security:list,*args,**kwargs):
    """
	获取区间融券卖出额

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"margin_shortamountint",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getMarginSaleRepayAmount(security:list,*args,**kwargs):
    """
	获取融券偿还额

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"margin_salerepayamount",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getMarginShortAmountRepayInt(security:list,*args,**kwargs):
    """
	获取区间融券偿还额

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"margin_shortamountrepayint",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getMrgShortVolBal(security:list,*args,**kwargs):
    """
	获取融券余量

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"mrg_short_vol_bal",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getMrgShortVolBalIntAvg(security:list,*args,**kwargs):
    """
	获取区间融券余量均值

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"mrg_short_vol_bal_int_avg",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getMrgShortBal(security:list,*args,**kwargs):
    """
	获取融券余额

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"mrg_short_bal",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getMrgShortBalIntAvg(security:list,*args,**kwargs):
    """
	获取区间融券余额均值

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"mrg_short_bal_int_avg",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getShortSellTurnover(security:list,*args,**kwargs):
    """
	获取全日卖空金额

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"shortsell_Turnover",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getShortSellTurnoverPct(security:list,*args,**kwargs):
    """
	获取卖空金额占市场卖空总额比率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"shortsell_TurnoverPct",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getShortSellVolume(security:list,*args,**kwargs):
    """
	获取全日卖空股数

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"shortsell_Volume",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getShortSellVolumeToHShares(security:list,*args,**kwargs):
    """
	获取卖空量占香港流通股百分比

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"shortsell_VolumeToHshares",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getShareShortShares(security:list,*args,**kwargs):
    """
	获取未平仓卖空数

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"share_shortshares",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getShareShortAmount(security:list,*args,**kwargs):
    """
	获取未平仓卖空金额

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"share_shortamount",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getShortSellDaysToCover(security:list,*args,**kwargs):
    """
	获取空头回补天数

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"shortsell_daystocover",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getMfdBuyAmtD(security:list,*args,**kwargs):
    """
	获取流入额

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"mfd_buyamt_d",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getMfNetInFlow(security:list,*args,**kwargs):
    """
	获取净流入额

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"mf_netinflow",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getMfdInFlowM(security:list,*args,**kwargs):
    """
	获取主力净流入额

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"mfd_inflow_m",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getMfdInFlowProportionM(security:list,*args,**kwargs):
    """
	获取主力净流入额占比

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"mfd_inflowproportion_m",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getMfdInFlowOpenM(security:list,*args,**kwargs):
    """
	获取开盘主力净流入额

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"mfd_inflow_open_m",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getMfdInFlowCloseM(security:list,*args,**kwargs):
    """
	获取尾盘主力净流入额

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"mfd_inflow_close_m",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getMfdInFlowProportionOpenM(security:list,*args,**kwargs):
    """
	获取开盘主力净流入额占比

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"mfd_inflowproportion_open_m",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getMfdInFlowProportionCloseM(security:list,*args,**kwargs):
    """
	获取尾盘主力净流入额占比

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"mfd_inflowproportion_close_m",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getMfdSellAmtD(security:list,*args,**kwargs):
    """
	获取流出额

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"mfd_sellamt_d",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getMfdBuyVolD(security:list,*args,**kwargs):
    """
	获取流入量

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"mfd_buyvol_d",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getMfdBuyVolM(security:list,*args,**kwargs):
    """
	获取主力净流入量

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"mfd_buyvol_m",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getMfdVolInFlowProportionM(security:list,*args,**kwargs):
    """
	获取主力净流入量占比

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"mfd_volinflowproportion_m",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getMfdBuyVolOpenM(security:list,*args,**kwargs):
    """
	获取开盘主力净流入量

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"mfd_buyvol_open_m",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getMfdBuyVolCloseM(security:list,*args,**kwargs):
    """
	获取尾盘主力净流入量

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"mfd_buyvol_close_m",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getMfdVolInFlowProportionOpenM(security:list,*args,**kwargs):
    """
	获取开盘主力净流入量占比

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"mfd_volinflowproportion_open_m",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getMfdVolInFlowProportionCloseM(security:list,*args,**kwargs):
    """
	获取尾盘主力净流入量占比

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"mfd_volinflowproportion_close_m",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getMfdSellVolD(security:list,*args,**kwargs):
    """
	获取流出量

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"mfd_sellvol_d",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getMfdNetBuyAmt(security:list,*args,**kwargs):
    """
	获取净买入额

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"mfd_netbuyamt",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getMfpSnInFlow(security:list,*args,**kwargs):
    """
	获取沪深港股通区间净买入额

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"mfp_sn_inflow",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getMfdNetBuyVol(security:list,*args,**kwargs):
    """
	获取净买入量

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"mfd_netbuyvol",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getMfpSnInFlowAmt(security:list,*args,**kwargs):
    """
	获取沪深港股通区间净买入量

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"mfp_sn_inflowamt",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getMfpSnInFlowAmt2(security:list,*args,**kwargs):
    """
	获取沪深港股通区间净买入量(调整)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"mfp_sn_inflowamt2",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getMfdBuyOrD(security:list,*args,**kwargs):
    """
	获取流入单数

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"mfd_buyord",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getMfdSelLord(security:list,*args,**kwargs):
    """
	获取流出单数

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"mfd_sellord",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getMfdBuyAmtA(security:list,*args,**kwargs):
    """
	获取主动买入额

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"mfd_buyamt_a",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getMfdBuyAmtAt(security:list,*args,**kwargs):
    """
	获取主动买入额(全单)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"mfd_buyamt_at",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getMfdNetBuyAmtA(security:list,*args,**kwargs):
    """
	获取净主动买入额

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"mfd_netbuyamt_a",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getMfAmt(security:list,*args,**kwargs):
    """
	获取净主动买入额(全单)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"mf_amt",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getMfdInFlowProportionA(security:list,*args,**kwargs):
    """
	获取净主动买入额占比

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"mfd_inflowproportion_a",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getMfAmtOpen(security:list,*args,**kwargs):
    """
	获取开盘净主动买入额

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"mf_amt_open",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getMfAmtClose(security:list,*args,**kwargs):
    """
	获取尾盘净主动买入额

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"mf_amt_close",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getMfdInFlowProportionOpenA(security:list,*args,**kwargs):
    """
	获取开盘净主动买入额占比

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"mfd_inflowproportion_open_a",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getMfdInFlowProportionCloseA(security:list,*args,**kwargs):
    """
	获取尾盘净主动买入额占比

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"mfd_inflowproportion_close_a",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getMfdSellAmtA(security:list,*args,**kwargs):
    """
	获取主动卖出额

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"mfd_sellamt_a",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getMfdSellAmtAt(security:list,*args,**kwargs):
    """
	获取主动卖出额(全单)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"mfd_sellamt_at",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getMfdBuyVolA(security:list,*args,**kwargs):
    """
	获取主动买入量

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"mfd_buyvol_a",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getMfdBuyVolAt(security:list,*args,**kwargs):
    """
	获取主动买入量(全单)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"mfd_buyvol_at",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getMfdNetBuyVolA(security:list,*args,**kwargs):
    """
	获取净主动买入量

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"mfd_netbuyvol_a",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getMfVol(security:list,*args,**kwargs):
    """
	获取净主动买入量(全单)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"mf_vol",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getMfVolRatio(security:list,*args,**kwargs):
    """
	获取净主动买入量占比

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"mf_vol_ratio",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getMfdVolInFlowProportionOpenA(security:list,*args,**kwargs):
    """
	获取开盘净主动买入量占比

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"mfd_volinflowproportion_open_a",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getMfdVolInFlowProportionCloseA(security:list,*args,**kwargs):
    """
	获取尾盘净主动买入量占比

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"mfd_volinflowproportion_close_a",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getMfdInFlowVolumeOpenA(security:list,*args,**kwargs):
    """
	获取开盘资金净主动买入量

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"mfd_inflowvolume_open_a",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getMfdInFlowVolumeCloseA(security:list,*args,**kwargs):
    """
	获取尾盘资金净主动买入量

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"mfd_inflowvolume_close_a",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getMfdSellVolA(security:list,*args,**kwargs):
    """
	获取主动卖出量

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"mfd_sellvol_a",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getMfdSellVolAt(security:list,*args,**kwargs):
    """
	获取主动卖出量(全单)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"mfd_sellvol_at",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getMfAmtRatio(security:list,*args,**kwargs):
    """
	获取净主动买入率(金额)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"mf_amt_ratio",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getMfdInFlowRateOpenA(security:list,*args,**kwargs):
    """
	获取开盘净主动买入率(金额)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"mfd_inflowrate_open_a",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getMfdInFlowRateCloseA(security:list,*args,**kwargs):
    """
	获取尾盘净主动买入率(金额)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"mfd_inflowrate_close_a",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getMfdVolInFlowRateA(security:list,*args,**kwargs):
    """
	获取净主动买入率(量)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"mfd_volinflowrate_a",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getMfdVolInFlowRateOpenA(security:list,*args,**kwargs):
    """
	获取开盘净主动买入率(量)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"mfd_volinflowrate_open_a",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getMfdVolInFlowRateCloseA(security:list,*args,**kwargs):
    """
	获取尾盘净主动买入率(量)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"mfd_volinflowrate_close_a",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getMfdInFlowRateM(security:list,*args,**kwargs):
    """
	获取主力净流入率(金额)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"mfd_inflowrate_m",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getMfdInFlowRateOpenM(security:list,*args,**kwargs):
    """
	获取开盘主力净流入率(金额)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"mfd_inflowrate_open_m",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getMfdInFlowRateCloseM(security:list,*args,**kwargs):
    """
	获取尾盘主力净流入率(金额)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"mfd_inflowrate_close_m",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getMfdVolInFlowRateM(security:list,*args,**kwargs):
    """
	获取主力净流入率(量)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"mfd_volinflowrate_m",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getMfdVolInFlowRateOpenM(security:list,*args,**kwargs):
    """
	获取开盘主力净流入率(量)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"mfd_volinflowrate_open_m",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getMfdVolInFlowRateCloseM(security:list,*args,**kwargs):
    """
	获取尾盘主力净流入率(量)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"mfd_volinflowrate_close_m",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getMfdSnBuyAmt(security:list,*args,**kwargs):
    """
	获取沪深港股通买入金额

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"mfd_sn_buyamt",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getMfdSnSellAmt(security:list,*args,**kwargs):
    """
	获取沪深港股通卖出金额

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"mfd_sn_sellamt",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getMfdSnInFlow(security:list,*args,**kwargs):
    """
	获取沪深港股通净买入金额

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"mfd_sn_inflow",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getMfpSnInFlowDays(security:list,*args,**kwargs):
    """
	获取沪深港股通区间净流入天数

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"mfp_sn_inflowdays",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getMfpSnOutflowDays(security:list,*args,**kwargs):
    """
	获取沪深港股通区间净流出天数

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"mfp_sn_outflowdays",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getMfnSnInFlowDays(security:list,*args,**kwargs):
    """
	获取沪深港股通持续净流入天数

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"mfn_sn_inflowdays",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getMfnSnOutflowDays(security:list,*args,**kwargs):
    """
	获取沪深港股通持续净卖出天数

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"mfn_sn_outflowdays",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getInSHdQFIiEx(security:list,*args,**kwargs):
    """
	获取外资买卖超

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"inshd_qfii_ex",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getInSHdQFIiExMv(security:list,*args,**kwargs):
    """
	获取外资买卖超市值

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"inshd_qfii_exmv",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getInSHdFundEx(security:list,*args,**kwargs):
    """
	获取投信买卖超

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"inshd_fund_ex",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getInSHdFundExMv(security:list,*args,**kwargs):
    """
	获取投信买卖超市值

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"inshd_fund_exmv",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getInSHdDlrEx(security:list,*args,**kwargs):
    """
	获取自营买卖超

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"inshd_dlr_ex",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getInSHdDlrExMv(security:list,*args,**kwargs):
    """
	获取自营买卖超市值

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"inshd_dlr_exmv",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getInSHdTtlEx(security:list,*args,**kwargs):
    """
	获取合计买卖超

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"inshd_ttl_ex",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getInSHdTtlExMv(security:list,*args,**kwargs):
    """
	获取合计买卖超市值

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"inshd_ttl_exmv",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getInSHdQFIiBuy(security:list,*args,**kwargs):
    """
	获取外资买进数量

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"inshd_qfii_buy",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getInSHdQFIiSell(security:list,*args,**kwargs):
    """
	获取外资卖出数量

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"inshd_qfii_sell",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getInSHdFundBuy(security:list,*args,**kwargs):
    """
	获取投信买进数量

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"inshd_fund_buy",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getInSHdFundSell(security:list,*args,**kwargs):
    """
	获取投信卖出数量

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"inshd_fund_sell",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getInSHdDlrBuy(security:list,*args,**kwargs):
    """
	获取自营商买进数量

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"inshd_dlr_buy",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getInSHdDlrSell(security:list,*args,**kwargs):
    """
	获取自营商卖出数量

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"inshd_dlr_sell",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getReturn(security:list,*args,**kwargs):
    """
	获取区间回报

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"return",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundQSimilarProductSimilarRanking(security:list,*args,**kwargs):
    """
	获取规模同类排名(券商集合理财)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_qsimilarproductsimilarranking",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundScaleRanking(security:list,*args,**kwargs):
    """
	获取规模同类排名

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_scaleranking",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getRiskDownsideRiskRanking(security:list,*args,**kwargs):
    """
	获取下行风险同类排名

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"risk_downsideriskranking",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getRiskTimeRanking(security:list,*args,**kwargs):
    """
	获取选时能力同类排名

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"risk_timeranking",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getRiskStockRanking(security:list,*args,**kwargs):
    """
	获取选股能力同类排名

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"risk_stockranking",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getRiskInfoRatioRanking(security:list,*args,**kwargs):
    """
	获取信息比率同类排名

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"risk_inforatioranking",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getRiskTrackErrorRanking(security:list,*args,**kwargs):
    """
	获取跟踪误差同类排名

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"risk_trackerrorranking",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getRiskAnnualVolRanking(security:list,*args,**kwargs):
    """
	获取年化波动率同类排名

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"risk_annualvolranking",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getStyleAvgPositionTimeRanking(security:list,*args,**kwargs):
    """
	获取平均持仓时间同类排名

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"style_avgpositiontimeranking",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getStStock(security:list,*args,**kwargs):
    """
	获取注册仓单数量

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"st_stock",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getEv1(security:list,*args,**kwargs):
    """
	获取企业价值(含货币资金)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"ev1",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getEv2(security:list,*args,**kwargs):
    """
	获取企业价值(剔除货币资金)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"ev2",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getValTaToEv(security:list,*args,**kwargs):
    """
	获取资产总计/企业价值_PIT

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"val_tatoev",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getValOrToEvTtM(security:list,*args,**kwargs):
    """
	获取营业收入(TTM)/企业价值_PIT

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"val_ortoev_ttm",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getCalcAccrued(security:list,*args,**kwargs):
    """
	获取应计利息(债券计算器)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"calc_accrued",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPtMTradeDay(security:list,*args,**kwargs):
    """
	获取剩余存续期(交易日)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"ptmtradeday",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPtMDay(security:list,*args,**kwargs):
    """
	获取剩余存续期(日历日)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"ptmday",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getTheoryValue(security:list,*args,**kwargs):
    """
	获取理论价格

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"theoryvalue",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIntrInCtValue(security:list,*args,**kwargs):
    """
	获取内在价值

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"intrinctvalue",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getTimeValue(security:list,*args,**kwargs):
    """
	获取时间价值

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"timevalue",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getUnderlyingHisVol30D(security:list,*args,**kwargs):
    """
	获取标的30日历史波动率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"underlyinghisvol_30d",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getUsHisVol(security:list,*args,**kwargs):
    """
	获取标的60日历史波动率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"us_hisvol",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getUnderlyingHisVol90D(security:list,*args,**kwargs):
    """
	获取标的90日历史波动率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"underlyinghisvol_90d",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getUsImpliedVol(security:list,*args,**kwargs):
    """
	获取期权隐含波动率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"us_impliedvol",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getVolatilityRatio(security:list,*args,**kwargs):
    """
	获取历史波动率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"volatilityratio",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIv1M1300(security:list,*args,**kwargs):
    """
	获取1个月130%价值状态隐含波动率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"iv_1m1300",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIv1M1200(security:list,*args,**kwargs):
    """
	获取1个月120%价值状态隐含波动率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"iv_1m1200",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIv1M1100(security:list,*args,**kwargs):
    """
	获取1个月110%价值状态隐含波动率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"iv_1m1100",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIv1M1050(security:list,*args,**kwargs):
    """
	获取1个月105%价值状态隐含波动率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"iv_1m1050",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIv1M1025(security:list,*args,**kwargs):
    """
	获取1个月102.5%价值状态隐含波动率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"iv_1m1025",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIv1M1000(security:list,*args,**kwargs):
    """
	获取1个月100%价值状态隐含波动率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"iv_1m1000",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIv1M975(security:list,*args,**kwargs):
    """
	获取1个月97.5%价值状态隐含波动率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"iv_1m975",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIv1M950(security:list,*args,**kwargs):
    """
	获取1个月95%价值状态隐含波动率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"iv_1m950",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIv1M900(security:list,*args,**kwargs):
    """
	获取1个月90%价值状态隐含波动率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"iv_1m900",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIv1M800(security:list,*args,**kwargs):
    """
	获取1个月80%价值状态隐含波动率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"iv_1m800",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIv1M600(security:list,*args,**kwargs):
    """
	获取1个月60%价值状态隐含波动率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"iv_1m600",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIv2M1300(security:list,*args,**kwargs):
    """
	获取2个月130%价值状态隐含波动率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"iv_2m1300",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIv2M1200(security:list,*args,**kwargs):
    """
	获取2个月120%价值状态隐含波动率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"iv_2m1200",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIv2M1100(security:list,*args,**kwargs):
    """
	获取2个月110%价值状态隐含波动率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"iv_2m1100",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIv2M1050(security:list,*args,**kwargs):
    """
	获取2个月105%价值状态隐含波动率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"iv_2m1050",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIv2M1025(security:list,*args,**kwargs):
    """
	获取2个月102.5%价值状态隐含波动率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"iv_2m1025",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIv2M1000(security:list,*args,**kwargs):
    """
	获取2个月100%价值状态隐含波动率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"iv_2m1000",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIv2M975(security:list,*args,**kwargs):
    """
	获取2个月97.5%价值状态隐含波动率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"iv_2m975",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIv2M950(security:list,*args,**kwargs):
    """
	获取2个月95%价值状态隐含波动率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"iv_2m950",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIv2M900(security:list,*args,**kwargs):
    """
	获取2个月90%价值状态隐含波动率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"iv_2m900",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIv2M800(security:list,*args,**kwargs):
    """
	获取2个月80%价值状态隐含波动率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"iv_2m800",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIv2M600(security:list,*args,**kwargs):
    """
	获取2个月60%价值状态隐含波动率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"iv_2m600",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIv3M1300(security:list,*args,**kwargs):
    """
	获取3个月130%价值状态隐含波动率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"iv_3m1300",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIv3M1200(security:list,*args,**kwargs):
    """
	获取3个月120%价值状态隐含波动率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"iv_3m1200",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIv3M1100(security:list,*args,**kwargs):
    """
	获取3个月110%价值状态隐含波动率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"iv_3m1100",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIv3M1050(security:list,*args,**kwargs):
    """
	获取3个月105%价值状态隐含波动率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"iv_3m1050",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIv3M1025(security:list,*args,**kwargs):
    """
	获取3个月102.5%价值状态隐含波动率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"iv_3m1025",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIv3M1000(security:list,*args,**kwargs):
    """
	获取3个月100%价值状态隐含波动率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"iv_3m1000",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIv3M975(security:list,*args,**kwargs):
    """
	获取3个月97.5%价值状态隐含波动率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"iv_3m975",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIv3M950(security:list,*args,**kwargs):
    """
	获取3个月95%价值状态隐含波动率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"iv_3m950",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIv3M900(security:list,*args,**kwargs):
    """
	获取3个月90%价值状态隐含波动率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"iv_3m900",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIv3M800(security:list,*args,**kwargs):
    """
	获取3个月80%价值状态隐含波动率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"iv_3m800",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIv3M600(security:list,*args,**kwargs):
    """
	获取3个月60%价值状态隐含波动率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"iv_3m600",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIv6M1300(security:list,*args,**kwargs):
    """
	获取6个月130%价值状态隐含波动率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"iv_6m1300",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIv6M1200(security:list,*args,**kwargs):
    """
	获取6个月120%价值状态隐含波动率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"iv_6m1200",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIv6M1100(security:list,*args,**kwargs):
    """
	获取6个月110%价值状态隐含波动率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"iv_6m1100",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIv6M1050(security:list,*args,**kwargs):
    """
	获取6个月105%价值状态隐含波动率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"iv_6m1050",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIv6M1025(security:list,*args,**kwargs):
    """
	获取6个月102.5%价值状态隐含波动率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"iv_6m1025",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIv6M1000(security:list,*args,**kwargs):
    """
	获取6个月100%价值状态隐含波动率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"iv_6m1000",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIv6M975(security:list,*args,**kwargs):
    """
	获取6个月97.5%价值状态隐含波动率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"iv_6m975",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIv6M950(security:list,*args,**kwargs):
    """
	获取6个月95%价值状态隐含波动率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"iv_6m950",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIv6M900(security:list,*args,**kwargs):
    """
	获取6个月90%价值状态隐含波动率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"iv_6m900",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIv6M800(security:list,*args,**kwargs):
    """
	获取6个月80%价值状态隐含波动率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"iv_6m800",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIv6M600(security:list,*args,**kwargs):
    """
	获取6个月60%价值状态隐含波动率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"iv_6m600",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIv9M1300(security:list,*args,**kwargs):
    """
	获取9个月130%价值状态隐含波动率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"iv_9m1300",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIv9M1200(security:list,*args,**kwargs):
    """
	获取9个月120%价值状态隐含波动率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"iv_9m1200",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIv9M1100(security:list,*args,**kwargs):
    """
	获取9个月110%价值状态隐含波动率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"iv_9m1100",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIv9M1050(security:list,*args,**kwargs):
    """
	获取9个月105%价值状态隐含波动率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"iv_9m1050",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIv9M1025(security:list,*args,**kwargs):
    """
	获取9个月102.5%价值状态隐含波动率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"iv_9m1025",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIv9M1000(security:list,*args,**kwargs):
    """
	获取9个月100%价值状态隐含波动率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"iv_9m1000",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIv9M975(security:list,*args,**kwargs):
    """
	获取9个月97.5%价值状态隐含波动率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"iv_9m975",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIv9M950(security:list,*args,**kwargs):
    """
	获取9个月95%价值状态隐含波动率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"iv_9m950",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIv9M900(security:list,*args,**kwargs):
    """
	获取9个月90%价值状态隐含波动率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"iv_9m900",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIv9M800(security:list,*args,**kwargs):
    """
	获取9个月80%价值状态隐含波动率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"iv_9m800",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIv9M600(security:list,*args,**kwargs):
    """
	获取9个月60%价值状态隐含波动率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"iv_9m600",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIv1Y1300(security:list,*args,**kwargs):
    """
	获取1年130%价值状态隐含波动率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"iv_1y1300",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIv1Y1200(security:list,*args,**kwargs):
    """
	获取1年120%价值状态隐含波动率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"iv_1y1200",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIv1Y1100(security:list,*args,**kwargs):
    """
	获取1年110%价值状态隐含波动率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"iv_1y1100",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIv1Y1050(security:list,*args,**kwargs):
    """
	获取1年105%价值状态隐含波动率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"iv_1y1050",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIv1Y1025(security:list,*args,**kwargs):
    """
	获取1年102.5%价值状态隐含波动率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"iv_1y1025",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIv1Y1000(security:list,*args,**kwargs):
    """
	获取1年100%价值状态隐含波动率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"iv_1y1000",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIv1Y975(security:list,*args,**kwargs):
    """
	获取1年97.5%价值状态隐含波动率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"iv_1y975",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIv1Y950(security:list,*args,**kwargs):
    """
	获取1年95%价值状态隐含波动率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"iv_1y950",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIv1Y900(security:list,*args,**kwargs):
    """
	获取1年90%价值状态隐含波动率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"iv_1y900",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIv1Y800(security:list,*args,**kwargs):
    """
	获取1年80%价值状态隐含波动率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"iv_1y800",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIv1Y600(security:list,*args,**kwargs):
    """
	获取1年60%价值状态隐含波动率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"iv_1y600",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWestNetProfitFtm(security:list,*args,**kwargs):
    """
	获取一致预测净利润(未来12个月)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"west_netprofit_FTM",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWestNetProfitFtmChg1M(security:list,*args,**kwargs):
    """
	获取一致预测净利润(未来12个月)的变化_1M_PIT

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"west_netprofit_ftm_chg_1m",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWestNetProfitFtmChg3M(security:list,*args,**kwargs):
    """
	获取一致预测净利润(未来12个月)的变化_3M_PIT

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"west_netprofit_ftm_chg_3m",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWestNetProfitFtmChg6M(security:list,*args,**kwargs):
    """
	获取一致预测净利润(未来12个月)的变化_6M_PIT

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"west_netprofit_ftm_chg_6m",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWestNetProfitFtm1M(security:list,*args,**kwargs):
    """
	获取一致预测净利润(未来12个月)的变化率_1M_PIT

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"west_netprofit_ftm_1m",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWestNetProfitFtm3M(security:list,*args,**kwargs):
    """
	获取一致预测净利润(未来12个月)的变化率_3M_PIT

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"west_netprofit_ftm_3m",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWestNetProfitFtm6M(security:list,*args,**kwargs):
    """
	获取一致预测净利润(未来12个月)的变化率_6M_PIT

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"west_netprofit_ftm_6m",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWestNetProfitDiff(security:list,*args,**kwargs):
    """
	获取一致预测净利润(未来12个月)与归属于母公司净利润(TTM)的差_PIT

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"west_netprofitdiff",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWestRoeFtm(security:list,*args,**kwargs):
    """
	获取一致预测净利润(未来12个月)/归属于母公司的股东权益_PIT

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"west_roe_ftm",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWestNetProfitYoY(security:list,*args,**kwargs):
    """
	获取一致预测净利润同比

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"west_netprofit_YOY",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWestAvgNpYoY(security:list,*args,**kwargs):
    """
	获取一致预测净利润同比(FY2比FY1)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"west_avgnp_yoy",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWestNetProfitCAgr(security:list,*args,**kwargs):
    """
	获取一致预测净利润2年复合增长率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"west_netprofit_CAGR",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWestNProc1W(security:list,*args,**kwargs):
    """
	获取一致预测净利润1周变化率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"west_nproc_1w",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWestNProc4W(security:list,*args,**kwargs):
    """
	获取一致预测净利润4周变化率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"west_nproc_4w",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWestNProc13W(security:list,*args,**kwargs):
    """
	获取一致预测净利润13周变化率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"west_nproc_13w",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWestNProc26W(security:list,*args,**kwargs):
    """
	获取一致预测净利润26周变化率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"west_nproc_26w",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWestEpsFtm(security:list,*args,**kwargs):
    """
	获取一致预测每股收益(未来12个月)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"west_eps_FTM",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWestEpsFtmChg1M(security:list,*args,**kwargs):
    """
	获取一致预测每股收益(未来12个月)的变化_1M_PIT

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"west_eps_ftm_chg_1m",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWestEpsFtmChg3M(security:list,*args,**kwargs):
    """
	获取一致预测每股收益(未来12个月)的变化_3M_PIT

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"west_eps_ftm_chg_3m",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWestEpsFtmChg6M(security:list,*args,**kwargs):
    """
	获取一致预测每股收益(未来12个月)的变化_6M_PIT

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"west_eps_ftm_chg_6m",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWestEpsFtm1M(security:list,*args,**kwargs):
    """
	获取一致预测每股收益(未来12个月)的变化率_1M_PIT

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"west_eps_ftm_1m",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWestEpsFtm3M(security:list,*args,**kwargs):
    """
	获取一致预测每股收益(未来12个月)的变化率_3M_PIT

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"west_eps_ftm_3m",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWestEpsFtm6M(security:list,*args,**kwargs):
    """
	获取一致预测每股收益(未来12个月)的变化率_6M_PIT

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"west_eps_ftm_6m",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWestEpsFtmGrowth(security:list,*args,**kwargs):
    """
	获取一致预测每股收益(未来12个月)与EPS(TTM)的变化率_PIT

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"west_eps_ftmgrowth",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWestSalesFtm(security:list,*args,**kwargs):
    """
	获取一致预测营业收入(未来12个月)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"west_sales_FTM",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWestSalesFtmChg1M(security:list,*args,**kwargs):
    """
	获取一致预测营业收入(未来12个月)的变化_1M_PIT

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"west_sales_ftm_chg_1m",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWestSalesFtmChg3M(security:list,*args,**kwargs):
    """
	获取一致预测营业收入(未来12个月)的变化_3M_PIT

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"west_sales_ftm_chg_3m",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWestSalesFtmChg6M(security:list,*args,**kwargs):
    """
	获取一致预测营业收入(未来12个月)的变化_6M_PIT

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"west_sales_ftm_chg_6m",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWestSalesFtm1M(security:list,*args,**kwargs):
    """
	获取一致预测营业收入(未来12个月)的变化率_1M_PIT

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"west_sales_ftm_1m",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWestSalesFtm3M(security:list,*args,**kwargs):
    """
	获取一致预测营业收入(未来12个月)的变化率_3M_PIT

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"west_sales_ftm_3m",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWestSalesFtm6M(security:list,*args,**kwargs):
    """
	获取一致预测营业收入(未来12个月)的变化率_6M_PIT

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"west_sales_ftm_6m",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWestSalesYoY(security:list,*args,**kwargs):
    """
	获取一致预测营业收入同比

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"west_sales_YOY",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWestSalesCAgr(security:list,*args,**kwargs):
    """
	获取一致预测营业收入2年复合增长率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"west_sales_CAGR",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWestAvgCpSFtm(security:list,*args,**kwargs):
    """
	获取一致预测每股现金流(未来12个月)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"west_avgcps_FTM",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWestAvGebItFtm(security:list,*args,**kwargs):
    """
	获取一致预测息税前利润(未来12个月)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"west_avgebit_FTM",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWestAvGebItYoY(security:list,*args,**kwargs):
    """
	获取一致预测息税前利润同比

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"west_avgebit_YOY",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWestAvGebItCAgr(security:list,*args,**kwargs):
    """
	获取一致预测息税前利润年复合增长率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"west_avgebit_CAGR",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWestAvGebItDaFtm(security:list,*args,**kwargs):
    """
	获取一致预测息税折旧摊销前利润(未来12个月)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"west_avgebitda_FTM",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWestAvGebItDaYoY(security:list,*args,**kwargs):
    """
	获取一致预测息税折旧摊销前利润同比

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"west_avgebitda_YOY",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWestAvGebItDaCAgr(security:list,*args,**kwargs):
    """
	获取一致预测息税折旧摊销前利润2年复合增长率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"west_avgebitda_CAGR",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWestAvGebTFtm(security:list,*args,**kwargs):
    """
	获取一致预测利润总额(未来12个月)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"west_avgebt_FTM",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWestAvGebTYoY(security:list,*args,**kwargs):
    """
	获取一致预测利润总额同比

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"west_avgebt_YOY",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWestAvGebTCAgr(security:list,*args,**kwargs):
    """
	获取一致预测利润总额2年复合增长率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"west_avgebt_CAGR",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWestAvgOperatingProfitFtm(security:list,*args,**kwargs):
    """
	获取一致预测营业利润(未来12个月)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"west_avgoperatingprofit_FTM",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWestAvgOperatingProfitYoY(security:list,*args,**kwargs):
    """
	获取一致预测营业利润同比

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"west_avgoperatingprofit_YOY",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWestAvgOperatingProfitCAgr(security:list,*args,**kwargs):
    """
	获取一致预测营业利润2年复合增长率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"west_avgoperatingprofit_CAGR",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWestAvgOcFtm(security:list,*args,**kwargs):
    """
	获取一致预测营业成本(未来12个月)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"west_avgoc_FTM",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWestAvgOcYoY(security:list,*args,**kwargs):
    """
	获取一致预测营业成本同比

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"west_avgoc_YOY",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWestAvgOcCAgr(security:list,*args,**kwargs):
    """
	获取一致预测营业成本2年复合增长率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"west_avgoc_CAGR",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getEstInStNum(security:list,*args,**kwargs):
    """
	获取每股收益预测机构家数

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"est_instnum",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWestInStNum(security:list,*args,**kwargs):
    """
	获取每股收益预测机构家数(可选类型)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"west_instnum",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getEstEps(security:list,*args,**kwargs):
    """
	获取预测每股收益平均值

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"est_eps",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getEstEps1(security:list,*args,**kwargs):
    """
	获取预测每股收益平均值(币种转换)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"est_eps1",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWestEps(security:list,*args,**kwargs):
    """
	获取预测每股收益平均值(可选类型)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"west_eps",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWestEps1(security:list,*args,**kwargs):
    """
	获取预测每股收益平均值(可选类型,币种转换)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"west_eps1",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getEstMaxEps(security:list,*args,**kwargs):
    """
	获取预测每股收益最大值

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"est_maxeps",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getEstMaxEps1(security:list,*args,**kwargs):
    """
	获取预测每股收益最大值(币种转换)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"est_maxeps1",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWestMaxEps(security:list,*args,**kwargs):
    """
	获取预测每股收益最大值(可选类型)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"west_maxeps",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWestMaxEps1(security:list,*args,**kwargs):
    """
	获取预测每股收益最大值(可选类型,币种转换)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"west_maxeps1",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getEstMinePs(security:list,*args,**kwargs):
    """
	获取预测每股收益最小值

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"est_mineps",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getEstMinePs1(security:list,*args,**kwargs):
    """
	获取预测每股收益最小值(币种转换)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"est_mineps1",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWestMinePs(security:list,*args,**kwargs):
    """
	获取预测每股收益最小值(可选类型)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"west_mineps",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWestMinePs1(security:list,*args,**kwargs):
    """
	获取预测每股收益最小值(可选类型,币种转换)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"west_mineps1",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getEstMedianEps(security:list,*args,**kwargs):
    """
	获取预测每股收益中值

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"est_medianeps",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getEstMedianEps1(security:list,*args,**kwargs):
    """
	获取预测每股收益中值(币种转换)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"est_medianeps1",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWestMedianEps(security:list,*args,**kwargs):
    """
	获取预测每股收益中值(可选类型)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"west_medianeps",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWestMedianEps1(security:list,*args,**kwargs):
    """
	获取预测每股收益中值(可选类型,币种转换)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"west_medianeps1",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getEstStdEps(security:list,*args,**kwargs):
    """
	获取预测每股收益标准差

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"est_stdeps",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getEstStdEps1(security:list,*args,**kwargs):
    """
	获取预测每股收益标准差(币种转换)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"est_stdeps1",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWestStdEps(security:list,*args,**kwargs):
    """
	获取预测每股收益标准差(可选类型)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"west_stdeps",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWestStdEps1(security:list,*args,**kwargs):
    """
	获取预测每股收益标准差(可选类型,币种转换)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"west_stdeps1",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getEstSales(security:list,*args,**kwargs):
    """
	获取预测营业收入平均值

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"est_sales",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getEstSales1(security:list,*args,**kwargs):
    """
	获取预测营业收入平均值(币种转换)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"est_sales1",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWestSales(security:list,*args,**kwargs):
    """
	获取预测营业收入平均值(可选类型)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"west_sales",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWestSales1(security:list,*args,**kwargs):
    """
	获取预测营业收入平均值(可选类型,币种转换)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"west_sales1",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getEstMaxSales(security:list,*args,**kwargs):
    """
	获取预测营业收入最大值

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"est_maxsales",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getEstMaxSales1(security:list,*args,**kwargs):
    """
	获取预测营业收入最大值(币种转换)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"est_maxsales1",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWestMaxSales(security:list,*args,**kwargs):
    """
	获取预测营业收入最大值(可选类型)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"west_maxsales",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWestMaxSales1(security:list,*args,**kwargs):
    """
	获取预测营业收入最大值(可选类型,币种转换)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"west_maxsales1",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getEstMinSales(security:list,*args,**kwargs):
    """
	获取预测营业收入最小值

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"est_minsales",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getEstMinSales1(security:list,*args,**kwargs):
    """
	获取预测营业收入最小值(币种转换)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"est_minsales1",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWestMinSales(security:list,*args,**kwargs):
    """
	获取预测营业收入最小值(可选类型)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"west_minsales",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWestMinSales1(security:list,*args,**kwargs):
    """
	获取预测营业收入最小值(可选类型,币种转换)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"west_minsales1",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getEstMedianSales(security:list,*args,**kwargs):
    """
	获取预测营业收入中值

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"est_mediansales",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getEstMedianSales1(security:list,*args,**kwargs):
    """
	获取预测营业收入中值(币种转换)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"est_mediansales1",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWestMedianSales(security:list,*args,**kwargs):
    """
	获取预测营业收入中值(可选类型)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"west_mediansales",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWestMedianSales1(security:list,*args,**kwargs):
    """
	获取预测营业收入中值(可选类型,币种转换)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"west_mediansales1",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getEstStdSales(security:list,*args,**kwargs):
    """
	获取预测营业收入标准差

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"est_stdsales",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getEstStdSales1(security:list,*args,**kwargs):
    """
	获取预测营业收入标准差(币种转换)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"est_stdsales1",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWestStdSales(security:list,*args,**kwargs):
    """
	获取预测营业收入标准差(可选类型)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"west_stdsales",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWestStdSales1(security:list,*args,**kwargs):
    """
	获取预测营业收入标准差(可选类型,币种转换)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"west_stdsales1",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getEstNetProfit(security:list,*args,**kwargs):
    """
	获取预测净利润平均值

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"est_netprofit",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getEstNetProfit1(security:list,*args,**kwargs):
    """
	获取预测净利润平均值(币种转换)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"est_netprofit1",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWestNetProfit(security:list,*args,**kwargs):
    """
	获取预测净利润平均值(可选类型)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"west_netprofit",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWestNetProfit1(security:list,*args,**kwargs):
    """
	获取预测净利润平均值(可选类型,币种转换)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"west_netprofit1",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getEstMaxNetProfit(security:list,*args,**kwargs):
    """
	获取预测净利润最大值

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"est_maxnetprofit",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getEstMaxNetProfit1(security:list,*args,**kwargs):
    """
	获取预测净利润最大值(币种转换)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"est_maxnetprofit1",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWestMaxNetProfit(security:list,*args,**kwargs):
    """
	获取预测净利润最大值(可选类型)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"west_maxnetprofit",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWestMaxNetProfit1(security:list,*args,**kwargs):
    """
	获取预测净利润最大值(可选类型,币种转换)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"west_maxnetprofit1",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getEstMinNetProfit(security:list,*args,**kwargs):
    """
	获取预测净利润最小值

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"est_minnetprofit",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getEstMinNetProfit1(security:list,*args,**kwargs):
    """
	获取预测净利润最小值(币种转换)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"est_minnetprofit1",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWestMinNetProfit(security:list,*args,**kwargs):
    """
	获取预测净利润最小值(可选类型)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"west_minnetprofit",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWestMinNetProfit1(security:list,*args,**kwargs):
    """
	获取预测净利润最小值(可选类型,币种转换)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"west_minnetprofit1",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getEstMedianNetProfit(security:list,*args,**kwargs):
    """
	获取预测净利润中值

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"est_mediannetprofit",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getEstMedianNetProfit1(security:list,*args,**kwargs):
    """
	获取预测净利润中值(币种转换)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"est_mediannetprofit1",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWestMedianNetProfit(security:list,*args,**kwargs):
    """
	获取预测净利润中值(可选类型)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"west_mediannetprofit",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWestMedianNetProfit1(security:list,*args,**kwargs):
    """
	获取预测净利润中值(可选类型,币种转换)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"west_mediannetprofit1",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getEstStdNetProfit(security:list,*args,**kwargs):
    """
	获取预测净利润标准差

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"est_stdnetprofit",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getEstStdNetProfit1(security:list,*args,**kwargs):
    """
	获取预测净利润标准差(币种转换)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"est_stdnetprofit1",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWestStdNetProfit(security:list,*args,**kwargs):
    """
	获取预测净利润标准差(可选类型)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"west_stdnetprofit",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWestStdNetProfit1(security:list,*args,**kwargs):
    """
	获取预测净利润标准差(可选类型,币种转换)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"west_stdnetprofit1",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getEstAvGebT(security:list,*args,**kwargs):
    """
	获取预测利润总额平均值

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"est_avgebt",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getEstAvGebT1(security:list,*args,**kwargs):
    """
	获取预测利润总额平均值(币种转换)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"est_avgebt1",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWestAvGebT(security:list,*args,**kwargs):
    """
	获取预测利润总额平均值(可选类型)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"west_avgebt",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWestAvGebT1(security:list,*args,**kwargs):
    """
	获取预测利润总额平均值(可选类型,币种转换)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"west_avgebt1",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getEstMaxEBt(security:list,*args,**kwargs):
    """
	获取预测利润总额最大值

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"est_maxebt",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getEstMaxEBt1(security:list,*args,**kwargs):
    """
	获取预测利润总额最大值(币种转换)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"est_maxebt1",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWestMaxEBt(security:list,*args,**kwargs):
    """
	获取预测利润总额最大值(可选类型)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"west_maxebt",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWestMaxEBt1(security:list,*args,**kwargs):
    """
	获取预测利润总额最大值(可选类型,币种转换)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"west_maxebt1",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getEstMinEBT(security:list,*args,**kwargs):
    """
	获取预测利润总额最小值

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"est_minebt",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getEstMinEBT1(security:list,*args,**kwargs):
    """
	获取预测利润总额最小值(币种转换)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"est_minebt1",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWestMinEBT(security:list,*args,**kwargs):
    """
	获取预测利润总额最小值(可选类型)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"west_minebt",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWestMinEBT1(security:list,*args,**kwargs):
    """
	获取预测利润总额最小值(可选类型,币种转换)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"west_minebt1",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getEstMedianEBt(security:list,*args,**kwargs):
    """
	获取预测利润总额中值

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"est_medianebt",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getEstMedianEBt1(security:list,*args,**kwargs):
    """
	获取预测利润总额中值(币种转换)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"est_medianebt1",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWestMedianEBt(security:list,*args,**kwargs):
    """
	获取预测利润总额中值(可选类型)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"west_medianebt",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWestMedianEBt1(security:list,*args,**kwargs):
    """
	获取预测利润总额中值(可选类型,币种转换)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"west_medianebt1",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getEstStDebt(security:list,*args,**kwargs):
    """
	获取预测利润总额标准差

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"est_stdebt",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getEstStDebt1(security:list,*args,**kwargs):
    """
	获取预测利润总额标准差(币种转换)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"est_stdebt1",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWestStDebt(security:list,*args,**kwargs):
    """
	获取预测利润总额标准差(可选类型)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"west_stdebt",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWestStDebt1(security:list,*args,**kwargs):
    """
	获取预测利润总额标准差(可选类型,币种转换)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"west_stdebt1",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getEstAvgOperatingProfit(security:list,*args,**kwargs):
    """
	获取预测营业利润平均值

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"est_avgoperatingprofit",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getEstAvgOperatingProfit1(security:list,*args,**kwargs):
    """
	获取预测营业利润平均值(币种转换)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"est_avgoperatingprofit1",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWestAvgOperatingProfit(security:list,*args,**kwargs):
    """
	获取预测营业利润平均值(可选类型)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"west_avgoperatingprofit",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWestAvgOperatingProfit1(security:list,*args,**kwargs):
    """
	获取预测营业利润平均值(可选类型,币种转换)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"west_avgoperatingprofit1",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getEstMaxOperatingProfit(security:list,*args,**kwargs):
    """
	获取预测营业利润最大值

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"est_maxoperatingprofit",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getEstMaxOperatingProfit1(security:list,*args,**kwargs):
    """
	获取预测营业利润最大值(币种转换)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"est_maxoperatingprofit1",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWestMaxOperatingProfit(security:list,*args,**kwargs):
    """
	获取预测营业利润最大值(可选类型)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"west_maxoperatingprofit",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWestMaxOperatingProfit1(security:list,*args,**kwargs):
    """
	获取预测营业利润最大值(可选类型,币种转换)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"west_maxoperatingprofit1",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getEstMinOperatingProfit(security:list,*args,**kwargs):
    """
	获取预测营业利润最小值

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"est_minoperatingprofit",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getEstMinOperatingProfit1(security:list,*args,**kwargs):
    """
	获取预测营业利润最小值(币种转换)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"est_minoperatingprofit1",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWestMinOperatingProfit(security:list,*args,**kwargs):
    """
	获取预测营业利润最小值(可选类型)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"west_minoperatingprofit",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWestMinOperatingProfit1(security:list,*args,**kwargs):
    """
	获取预测营业利润最小值(可选类型,币种转换)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"west_minoperatingprofit1",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getEstMedianOperatingProfit(security:list,*args,**kwargs):
    """
	获取预测营业利润中值

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"est_medianoperatingprofit",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getEstMedianOperatingProfit1(security:list,*args,**kwargs):
    """
	获取预测营业利润中值(币种转换)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"est_medianoperatingprofit1",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWestMedianOperatingProfit(security:list,*args,**kwargs):
    """
	获取预测营业利润中值(可选类型)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"west_medianoperatingprofit",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWestMedianOperatingProfit1(security:list,*args,**kwargs):
    """
	获取预测营业利润中值(可选类型,币种转换)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"west_medianoperatingprofit1",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getEstStdOperatingProfit(security:list,*args,**kwargs):
    """
	获取预测营业利润标准差

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"est_stdoperatingprofit",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getEstStdOperatingProfit1(security:list,*args,**kwargs):
    """
	获取预测营业利润标准差(币种转换)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"est_stdoperatingprofit1",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWestStdOperatingProfit(security:list,*args,**kwargs):
    """
	获取预测营业利润标准差(可选类型)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"west_stdoperatingprofit",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWestStdOperatingProfit1(security:list,*args,**kwargs):
    """
	获取预测营业利润标准差(可选类型,币种转换)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"west_stdoperatingprofit1",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getEstSalesUpgrade(security:list,*args,**kwargs):
    """
	获取营业收入调高家数

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"est_sales_upgrade",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWestSalesUpgrade(security:list,*args,**kwargs):
    """
	获取营业收入调高家数(可选类型)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"west_sales_upgrade",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getEstSalesDowngrade(security:list,*args,**kwargs):
    """
	获取营业收入调低家数

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"est_sales_downgrade",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWestSalesDowngrade(security:list,*args,**kwargs):
    """
	获取营业收入调低家数(可选类型)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"west_sales_downgrade",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getEstSalesMaintain(security:list,*args,**kwargs):
    """
	获取营业收入维持家数

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"est_sales_maintain",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWestSalesMaintain(security:list,*args,**kwargs):
    """
	获取营业收入维持家数(可选类型)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"west_sales_maintain",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getEstNetProfitUpgrade(security:list,*args,**kwargs):
    """
	获取净利润调高家数

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"est_netprofit_upgrade",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWestNetProfitUpgrade(security:list,*args,**kwargs):
    """
	获取净利润调高家数(可选类型)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"west_netprofit_upgrade",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getEstNetProfitDowngrade(security:list,*args,**kwargs):
    """
	获取净利润调低家数

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"est_netprofit_downgrade",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWestNetProfitDowngrade(security:list,*args,**kwargs):
    """
	获取净利润调低家数(可选类型)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"west_netprofit_downgrade",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getEstNetProfitMaintain(security:list,*args,**kwargs):
    """
	获取净利润维持家数

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"est_netprofit_maintain",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWestNetProfitMaintain(security:list,*args,**kwargs):
    """
	获取净利润维持家数(可选类型)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"west_netprofit_maintain",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getEstYoYNetProfit(security:list,*args,**kwargs):
    """
	获取预测净利润增长率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"est_yoynetprofit",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWestYoYNetProfit(security:list,*args,**kwargs):
    """
	获取预测净利润增长率(可选类型)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"west_yoynetprofit",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getEstYoYSales(security:list,*args,**kwargs):
    """
	获取预测营业收入增长率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"est_yoysales",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWestYoYSales(security:list,*args,**kwargs):
    """
	获取预测营业收入增长率(可选类型)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"west_yoysales",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getRatingAvg(security:list,*args,**kwargs):
    """
	获取综合评级(数值)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"rating_avg",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWRatingAvgData(security:list,*args,**kwargs):
    """
	获取综合评级(数值)(可选类型)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"wrating_avg_data",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getRatingAvgChN(security:list,*args,**kwargs):
    """
	获取综合评级(中文)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"rating_avgchn",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWRatingAvgCn(security:list,*args,**kwargs):
    """
	获取综合评级(中文)(可选类型)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"wrating_avg_cn",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getRatingAvGeng(security:list,*args,**kwargs):
    """
	获取综合评级(英文)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"rating_avgeng",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWRatingAvgEn(security:list,*args,**kwargs):
    """
	获取综合评级(英文)(可选类型)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"wrating_avg_en",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getRatingInStNum(security:list,*args,**kwargs):
    """
	获取评级机构家数

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"rating_instnum",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWRatingInStNum(security:list,*args,**kwargs):
    """
	获取评级机构家数(可选类型)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"wrating_instnum",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getRatingUpgrade(security:list,*args,**kwargs):
    """
	获取评级调高家数

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"rating_upgrade",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWRatingUpgrade(security:list,*args,**kwargs):
    """
	获取评级调高家数(可选类型)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"wrating_upgrade",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getRatingDowngrade(security:list,*args,**kwargs):
    """
	获取评级调低家数

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"rating_downgrade",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWRatingDowngrade(security:list,*args,**kwargs):
    """
	获取评级调低家数(可选类型)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"wrating_downgrade",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getRatingMaintain(security:list,*args,**kwargs):
    """
	获取评级维持家数

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"rating_maintain",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWRatingMaintain(security:list,*args,**kwargs):
    """
	获取评级维持家数(可选类型)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"wrating_maintain",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getRatingNumOfBuy(security:list,*args,**kwargs):
    """
	获取评级买入家数

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"rating_numofbuy",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWRatingNumOfBuy(security:list,*args,**kwargs):
    """
	获取评级买入家数(可选类型)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"wrating_numofbuy",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getRatingNumOfOutperform(security:list,*args,**kwargs):
    """
	获取评级增持家数

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"rating_numofoutperform",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWRatingNumOfOutperform(security:list,*args,**kwargs):
    """
	获取评级增持家数(可选类型)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"wrating_numofoutperform",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getRatingNumOfHold(security:list,*args,**kwargs):
    """
	获取评级中性家数

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"rating_numofhold",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWRatingNumOfHold(security:list,*args,**kwargs):
    """
	获取评级中性家数(可选类型)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"wrating_numofhold",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getRatingNumOfUnderPerform(security:list,*args,**kwargs):
    """
	获取评级减持家数

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"rating_numofunderperform",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWRatingNumOfUnderPerform(security:list,*args,**kwargs):
    """
	获取评级减持家数(可选类型)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"wrating_numofunderperform",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getRatingNumOfSell(security:list,*args,**kwargs):
    """
	获取评级卖出家数

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"rating_numofsell",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWRatingNumOfSell(security:list,*args,**kwargs):
    """
	获取评级卖出家数(可选类型)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"wrating_numofsell",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWRatingTargetPrice(security:list,*args,**kwargs):
    """
	获取一致预测目标价

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"wrating_targetprice",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getTargetPriceAvg(security:list,*args,**kwargs):
    """
	获取一致预测目标价(可选类型)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"targetprice_avg",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWestFReturn(security:list,*args,**kwargs):
    """
	获取一致预测目标价上升空间_PIT

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"west_freturn",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getEstEventDate(security:list,*args,**kwargs):
    """
	获取大事日期(大事后预测)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"est_event_date",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWestInStNumSales(security:list,*args,**kwargs):
    """
	获取营业收入预测机构家数(可选类型)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"west_instnum_sales",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWestInStNumNp(security:list,*args,**kwargs):
    """
	获取净利润预测机构家数(可选类型)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"west_instnum_np",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWestInStNumCpS(security:list,*args,**kwargs):
    """
	获取每股现金流预测机构家数(可选类型)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"west_instnum_cps",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWestInStNumDps(security:list,*args,**kwargs):
    """
	获取每股股利预测机构家数(可选类型)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"west_instnum_dps",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWestInStNumEbIt(security:list,*args,**kwargs):
    """
	获取息税前利润预测机构家数(可选类型)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"west_instnum_ebit",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWestInStNumEbItDa(security:list,*args,**kwargs):
    """
	获取息税折旧摊销前利润预测机构家数(可选类型)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"west_instnum_ebitda",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWestInStNumBpS(security:list,*args,**kwargs):
    """
	获取每股净资产预测机构家数(可选类型)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"west_instnum_bps",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWestInStNumEBt(security:list,*args,**kwargs):
    """
	获取利润总额预测机构家数(可选类型)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"west_instnum_ebt",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWestInStNumRoa(security:list,*args,**kwargs):
    """
	获取总资产收益率预测机构家数(可选类型)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"west_instnum_roa",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWestInStNumRoe(security:list,*args,**kwargs):
    """
	获取净资产收益率预测机构家数(可选类型)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"west_instnum_roe",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWestInStNumOp(security:list,*args,**kwargs):
    """
	获取营业利润预测机构家数(可选类型)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"west_instnum_op",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWestAvgOc(security:list,*args,**kwargs):
    """
	获取预测营业成本平均值(可选类型)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"west_avgoc",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWestMaxOc(security:list,*args,**kwargs):
    """
	获取预测营业成本最大值(可选类型)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"west_maxoc",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWestMinoC(security:list,*args,**kwargs):
    """
	获取预测营业成本最小值(可选类型)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"west_minoc",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWestMediaOc(security:list,*args,**kwargs):
    """
	获取预测营业成本中值(可选类型)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"west_mediaoc",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWestSToC(security:list,*args,**kwargs):
    """
	获取预测营业成本标准差(可选类型)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"west_stoc",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWestAvgShares(security:list,*args,**kwargs):
    """
	获取预测基准股本综合值(可选类型)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"west_avgshares",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getErrWi(security:list,*args,**kwargs):
    """
	获取盈利修正比例(可选类型)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"err_wi",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getEstCAgrNp(security:list,*args,**kwargs):
    """
	获取未来3年净利润复合年增长率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"est_cagr_np",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getEstCAgrSales(security:list,*args,**kwargs):
    """
	获取未来3年营业总收入复合年增长率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"est_cagr_sales",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWestInStNumGm(security:list,*args,**kwargs):
    """
	获取销售毛利率预测机构家数(可选类型)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"west_instnum_gm",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWestAvgOc1(security:list,*args,**kwargs):
    """
	获取预测营业成本平均值(可选类型,币种转换)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"west_avgoc1",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWestMaxOc1(security:list,*args,**kwargs):
    """
	获取预测营业成本最大值(可选类型,币种转换)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"west_maxoc1",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWestMinoC1(security:list,*args,**kwargs):
    """
	获取预测营业成本最小值(可选类型,币种转换)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"west_minoc1",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWestMediaOc1(security:list,*args,**kwargs):
    """
	获取预测营业成本中值(可选类型,币种转换)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"west_mediaoc1",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWestSToC1(security:list,*args,**kwargs):
    """
	获取预测营业成本标准差(可选类型,币种转换)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"west_stoc1",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getEstPreLowPriceInSt(security:list,*args,**kwargs):
    """
	获取前次最低目标价

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"est_prelowprice_inst",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getEstPreHighPriceInSt(security:list,*args,**kwargs):
    """
	获取前次最高目标价

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"est_prehighprice_inst",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getEstLowPriceInSt(security:list,*args,**kwargs):
    """
	获取本次最低目标价

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"est_lowprice_inst",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getEstHighPriceInSt(security:list,*args,**kwargs):
    """
	获取本次最高目标价

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"est_highprice_inst",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getEstOrGratingInSt(security:list,*args,**kwargs):
    """
	获取机构投资评级(原始)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"est_orgrating_inst",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getEstScoreRatingInSt(security:list,*args,**kwargs):
    """
	获取机构投资评级(标准化得分)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"est_scorerating_inst",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getEstStdRatingInSt(security:list,*args,**kwargs):
    """
	获取机构投资评级(标准化评级)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"est_stdrating_inst",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getEstNewRatingTimeInSt(security:list,*args,**kwargs):
    """
	获取机构最近评级时间

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"est_newratingtime_inst",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getEstEstNewTimeInSt(security:list,*args,**kwargs):
    """
	获取机构最近预测时间

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"est_estnewtime_inst",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getEstSalesInSt(security:list,*args,**kwargs):
    """
	获取机构预测营业收入

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"est_sales_inst",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getEstNetProfitInSt(security:list,*args,**kwargs):
    """
	获取机构预测净利润

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"est_netprofit_inst",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getEstEpsInSt(security:list,*args,**kwargs):
    """
	获取机构预测每股收益

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"est_eps_inst",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getEstFrStRatingTimeInSt(security:list,*args,**kwargs):
    """
	获取机构首次评级时间

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"est_frstratingtime_inst",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getEstRatingAnalyst(security:list,*args,**kwargs):
    """
	获取评级研究员

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"est_ratinganalyst",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getEstEstAnalyst(security:list,*args,**kwargs):
    """
	获取预测研究员

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"est_estanalyst",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getEstRpTAbstractInSt(security:list,*args,**kwargs):
    """
	获取内容

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"est_rptabstract_inst",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getEstRpTTitleInSt(security:list,*args,**kwargs):
    """
	获取报告标题

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"est_rpttitle_inst",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getProfitNoticeChange(security:list,*args,**kwargs):
    """
	获取预告净利润变动幅度(%)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"profitnotice_change",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getProfitNoticeLaSteps(security:list,*args,**kwargs):
    """
	获取去年同期每股收益

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"profitnotice_lasteps",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getStmNoteProfitApr3(security:list,*args,**kwargs):
    """
	获取可分配利润

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"stmnote_profitapr_3",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getProfitNoticeLastYearDeductedProfit(security:list,*args,**kwargs):
    """
	获取上年同期扣非净利润

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"profitnotice_lastyeardeductedprofit",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getProfitNoticeLastYearIncome(security:list,*args,**kwargs):
    """
	获取上年同期营业收入

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"profitnotice_lastyearincome",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getProfitNoticeLastYearDeductedSales(security:list,*args,**kwargs):
    """
	获取上年同期扣除后营业收入

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"profitnotice_lastyeardeductedsales",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getProfitNoticeBasicEarnMax(security:list,*args,**kwargs):
    """
	获取预告基本每股收益下限

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"profitnotice_basicearnmax",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getProfitNoticeBasicEarnMin(security:list,*args,**kwargs):
    """
	获取预告基本每股收益上限

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"profitnotice_basicearnmin",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getProfitNoticeDeductedEarnMin(security:list,*args,**kwargs):
    """
	获取预告扣非后基本每股收益下限

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"profitnotice_deductedearnmin",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getProfitNoticeDeductedEarnMax(security:list,*args,**kwargs):
    """
	获取预告扣非后基本每股收益上限

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"profitnotice_deductedearnmax",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getProfitNoticeLastYearDeductedEarn(security:list,*args,**kwargs):
    """
	获取上年同期扣非后基本每股收益

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"profitnotice_lastyeardeductedearn",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getProfitNoticeNetProfitMax(security:list,*args,**kwargs):
    """
	获取预告净利润上限

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"profitnotice_netprofitmax",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getQProfitNoticeNetProfitMax(security:list,*args,**kwargs):
    """
	获取单季度.预告净利润上限(海外)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"qprofitnotice_netprofitmax",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getProfitNoticeNetProfitMin(security:list,*args,**kwargs):
    """
	获取预告净利润下限

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"profitnotice_netprofitmin",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getQProfitNoticeNetProfitMin(security:list,*args,**kwargs):
    """
	获取单季度.预告净利润下限(海外)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"qprofitnotice_netprofitmin",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getProfitNoticeChangeMax(security:list,*args,**kwargs):
    """
	获取预告净利润同比增长上限

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"profitnotice_changemax",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getQProfitNoticeChangeMax(security:list,*args,**kwargs):
    """
	获取单季度.预告净利润同比增长上限(海外)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"qprofitnotice_changemax",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getProfitNoticeChangeMin(security:list,*args,**kwargs):
    """
	获取预告净利润同比增长下限

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"profitnotice_changemin",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getQProfitNoticeChangeMin(security:list,*args,**kwargs):
    """
	获取单季度.预告净利润同比增长下限(海外)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"qprofitnotice_changemin",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getProfitNoticeDeductedProfitMax(security:list,*args,**kwargs):
    """
	获取预告扣非净利润上限

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"profitnotice_deductedprofitmax",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getProfitNoticeDeductedProfitMin(security:list,*args,**kwargs):
    """
	获取预告扣非净利润下限

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"profitnotice_deductedprofitmin",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getProfitNoticeDeductedProfitYoYMax(security:list,*args,**kwargs):
    """
	获取预告扣非净利润同比增长上限

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"profitnotice_deductedprofityoymax",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getProfitNoticeDeductedProfitYoYMin(security:list,*args,**kwargs):
    """
	获取预告扣非净利润同比增长下限

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"profitnotice_deductedprofityoymin",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getProfitNoticeIncomeMax(security:list,*args,**kwargs):
    """
	获取预告营业收入上限

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"profitnotice_incomemax",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getProfitNoticeIncomeMin(security:list,*args,**kwargs):
    """
	获取预告营业收入下限

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"profitnotice_incomemin",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getProfitNoticeDeductedSalesMax(security:list,*args,**kwargs):
    """
	获取预告扣除后营业收入上限

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"profitnotice_deductedsalesmax",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getProfitNoticeDeductedSalesMin(security:list,*args,**kwargs):
    """
	获取预告扣除后营业收入下限

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"profitnotice_deductedsalesmin",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getProfitNoticeNetSalesMax(security:list,*args,**kwargs):
    """
	获取预告净营收上限(海外)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"profitnotice_netsalesmax",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getQProfitNoticeNetSalesMax(security:list,*args,**kwargs):
    """
	获取单季度.预告净营收上限(海外)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"qprofitnotice_netsalesmax",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getProfitNoticeNetSalesMin(security:list,*args,**kwargs):
    """
	获取预告净营收下限(海外)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"profitnotice_netsalesmin",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getQProfitNoticeNetSalesMin(security:list,*args,**kwargs):
    """
	获取单季度.预告净营收下限(海外)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"qprofitnotice_netsalesmin",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getProfitNoticeNetSalesYoYMax(security:list,*args,**kwargs):
    """
	获取预告净营收同比增长上限(海外)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"profitnotice_netsalesyoymax",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getQProfitNoticeNetSalesYoYMax(security:list,*args,**kwargs):
    """
	获取单季度.预告净营收同比增长上限(海外)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"qprofitnotice_netsalesyoymax",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getProfitNoticeNetSalesYoYMin(security:list,*args,**kwargs):
    """
	获取预告净营收同比增长下限(海外)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"profitnotice_netsalesyoymin",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getQProfitNoticeNetSalesYoYMin(security:list,*args,**kwargs):
    """
	获取单季度.预告净营收同比增长下限(海外)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"qprofitnotice_netsalesyoymin",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getProfitNoticeSalesMax(security:list,*args,**kwargs):
    """
	获取预告总营收上限(海外)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"profitnotice_salesmax",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getQProfitNoticeSalesMax(security:list,*args,**kwargs):
    """
	获取单季度.预告总营收上限(海外)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"qprofitnotice_salesmax",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getProfitNoticeSalesMin(security:list,*args,**kwargs):
    """
	获取预告总营收下限(海外)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"profitnotice_salesmin",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getQProfitNoticeSalesMin(security:list,*args,**kwargs):
    """
	获取单季度.预告总营收下限(海外)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"qprofitnotice_salesmin",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getProfitNoticeSalesYoYMax(security:list,*args,**kwargs):
    """
	获取预告总营收同比增长上限(海外)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"profitnotice_salesyoymax",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getQProfitNoticeSalesYoYMax(security:list,*args,**kwargs):
    """
	获取单季度.预告总营收同比增长上限(海外)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"qprofitnotice_salesyoymax",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getProfitNoticeSalesYoYMin(security:list,*args,**kwargs):
    """
	获取预告总营收同比增长下限(海外)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"profitnotice_salesyoymin",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getQProfitNoticeSalesYoYMin(security:list,*args,**kwargs):
    """
	获取单季度.预告总营收同比增长下限(海外)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"qprofitnotice_salesyoymin",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getOCFToInterest(security:list,*args,**kwargs):
    """
	获取现金流量利息保障倍数

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"ocftointerest",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFaCfpSTtM(security:list,*args,**kwargs):
    """
	获取每股现金流量净额(TTM)_PIT

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fa_cfps_ttm",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getCfpS(security:list,*args,**kwargs):
    """
	获取每股现金流量净额

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"cfps",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWgsDCfpS(security:list,*args,**kwargs):
    """
	获取每股现金流量净额_GSD

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"wgsd_cfps",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWgsDCashBalChgCf(security:list,*args,**kwargs):
    """
	获取其他现金流量调整_GSD

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"wgsd_cash_bal_chg_cf",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFcFf(security:list,*args,**kwargs):
    """
	获取企业自由现金流量FCFF

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fcff",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFcFe(security:list,*args,**kwargs):
    """
	获取股权自由现金流量FCFE

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fcfe",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWgsDFcFe2(security:list,*args,**kwargs):
    """
	获取股权自由现金流量FCFE_GSD

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"wgsd_fcfe2",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWgsDFcFf2(security:list,*args,**kwargs):
    """
	获取企业自由现金流量_GSD

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"wgsd_fcff2",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFaFcFf(security:list,*args,**kwargs):
    """
	获取企业自由现金流量_PIT

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fa_fcff",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFaFcFe(security:list,*args,**kwargs):
    """
	获取股权自由现金流量_PIT

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fa_fcfe",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFaNcGrTtM(security:list,*args,**kwargs):
    """
	获取增长率-净现金流量(TTM)_PIT

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fa_ncgr_ttm",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFcFFps(security:list,*args,**kwargs):
    """
	获取每股企业自由现金流量

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fcffps",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFcFEps(security:list,*args,**kwargs):
    """
	获取每股股东自由现金流量

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fcfeps",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWgsDFcFFps2(security:list,*args,**kwargs):
    """
	获取每股企业自由现金流量_GSD

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"wgsd_fcffps2",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWgsDFcFEps2(security:list,*args,**kwargs):
    """
	获取每股股东自由现金流量_GSD

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"wgsd_fcfeps2",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWgsDQfaCashBalChgCf(security:list,*args,**kwargs):
    """
	获取单季度.其他现金流量调整_GSD

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"wgsd_qfa_cash_bal_chg_cf",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFaFcFFps(security:list,*args,**kwargs):
    """
	获取每股企业自由现金流量_PIT

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fa_fcffps",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFaFcFEps(security:list,*args,**kwargs):
    """
	获取每股股东自由现金流量_PIT

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fa_fcfeps",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFaOCFToInterestDebtTtM(security:list,*args,**kwargs):
    """
	获取经营活动产生现金流量净额/带息债务(TTM)_PIT

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fa_ocftointerestdebt_ttm",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFaOCFToNetDebtTtM(security:list,*args,**kwargs):
    """
	获取经营活动产生现金流量净额/净债务(TTM)_PIT

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fa_ocftonetdebt_ttm",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getOCFToOr(security:list,*args,**kwargs):
    """
	获取经营活动产生的现金流量净额/营业收入

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"ocftoor",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getOCFToOperateIncome(security:list,*args,**kwargs):
    """
	获取经营活动产生的现金流量净额/经营活动净收益

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"ocftooperateincome",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getOCFTOCF(security:list,*args,**kwargs):
    """
	获取经营活动产生的现金流量净额占比

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"ocftocf",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getICfTOCF(security:list,*args,**kwargs):
    """
	获取投资活动产生的现金流量净额占比

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"icftocf",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFcFTOCF(security:list,*args,**kwargs):
    """
	获取筹资活动产生的现金流量净额占比

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fcftocf",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getOCFToDebt(security:list,*args,**kwargs):
    """
	获取经营活动产生的现金流量净额/负债合计

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"ocftodebt",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getOCFToInterestDebt(security:list,*args,**kwargs):
    """
	获取经营活动产生的现金流量净额/带息债务

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"ocftointerestdebt",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getOCFToShortDebt(security:list,*args,**kwargs):
    """
	获取经营活动产生的现金流量净额/流动负债

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"ocftoshortdebt",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getOCFToLongDebt(security:list,*args,**kwargs):
    """
	获取经营活动产生的现金流量净额/非流动负债

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"ocftolongdebt",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getOCFToNetDebt(security:list,*args,**kwargs):
    """
	获取经营活动产生的现金流量净额/净债务

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"ocftonetdebt",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getYoyOCF(security:list,*args,**kwargs):
    """
	获取经营活动产生的现金流量净额(同比增长率)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"yoyocf",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getGrowthOCF(security:list,*args,**kwargs):
    """
	获取经营活动产生的现金流量净额(N年,增长率)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"growth_ocf",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getOCFToOrTtM2(security:list,*args,**kwargs):
    """
	获取经营活动产生的现金流量净额/营业收入(TTM)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"ocftoor_ttm2",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getOCFToOperateIncomeTtM2(security:list,*args,**kwargs):
    """
	获取经营活动产生的现金流量净额/经营活动净收益(TTM)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"ocftooperateincome_ttm2",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getOperateCashFlowToOpTtM(security:list,*args,**kwargs):
    """
	获取经营活动产生的现金流量净额/营业利润(TTM)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"operatecashflowtoop_ttm",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWgsDOCFToSales(security:list,*args,**kwargs):
    """
	获取经营活动产生的现金流量净额/营业收入_GSD

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"wgsd_ocftosales",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWgsDOCFToOperateIncome(security:list,*args,**kwargs):
    """
	获取经营活动产生的现金流量净额/经营活动净收益_GSD

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"wgsd_ocftooperateincome",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWgsDOCFToLiqDebt(security:list,*args,**kwargs):
    """
	获取经营活动产生的现金流量净额/流动负债_GSD

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"wgsd_ocftoliqdebt",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWgsDOCFToDebt(security:list,*args,**kwargs):
    """
	获取经营活动产生的现金流量净额/负债合计_GSD

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"wgsd_ocftodebt",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWgsDOCFToInterestDebt(security:list,*args,**kwargs):
    """
	获取经营活动产生的现金流量净额/带息债务_GSD

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"wgsd_ocftointerestdebt",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWgsDOCFToNetDebt(security:list,*args,**kwargs):
    """
	获取经营活动产生的现金流量净额/净债务_GSD

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"wgsd_ocftonetdebt",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWgsDYoyOCF(security:list,*args,**kwargs):
    """
	获取经营活动产生的现金流量净额(同比增长率)_GSD

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"wgsd_yoyocf",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWgsDGrowthOCF(security:list,*args,**kwargs):
    """
	获取经营活动产生的现金流量净额(N年,增长率)_GSD

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"wgsd_growth_ocf",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getOCFToOperateIncomeTtM3(security:list,*args,**kwargs):
    """
	获取经营活动产生的现金流量净额/经营活动净收益(TTM)_GSD

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"ocftooperateincome_ttm3",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getOperateCashFlowToOpTtM2(security:list,*args,**kwargs):
    """
	获取经营活动产生的现金流量净额/营业利润(TTM)_GSD

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"operatecashflowtoop_ttm2",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getOCFToSalesTtM2(security:list,*args,**kwargs):
    """
	获取经营活动产生的现金流量净额/营业收入(TTM)_GSD

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"ocftosales_ttm2",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWgsDOperCf(security:list,*args,**kwargs):
    """
	获取经营活动产生的现金流量净额_GSD

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"wgsd_oper_cf",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWgsDInvestCf(security:list,*args,**kwargs):
    """
	获取投资活动产生的现金流量净额_GSD

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"wgsd_invest_cf",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWgsDFinCf(security:list,*args,**kwargs):
    """
	获取筹资活动产生的现金流量净额_GSD

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"wgsd_fin_cf",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getCfOperActNetting(security:list,*args,**kwargs):
    """
	获取经营活动产生的现金流量净额差额(合计平衡项目)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"cf_oper_act_netting",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getStm07CsReItsOperNetCash(security:list,*args,**kwargs):
    """
	获取经营活动产生的现金流量净额

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"stm07_cs_reits_opernetcash",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getCfInvActNetting(security:list,*args,**kwargs):
    """
	获取投资活动产生的现金流量净额差额(合计平衡项目)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"cf_inv_act_netting",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getStm07CsReItsInvestNetCash(security:list,*args,**kwargs):
    """
	获取投资活动产生的现金流量净额

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"stm07_cs_reits_investnetcash",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getCfFncActNetting(security:list,*args,**kwargs):
    """
	获取筹资活动产生的现金流量净额差额(合计平衡项目)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"cf_fnc_act_netting",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getStm07CsReItsFinanceNetCash(security:list,*args,**kwargs):
    """
	获取筹资活动产生的现金流量净额

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"stm07_cs_reits_financenetcash",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFaOCFToOr(security:list,*args,**kwargs):
    """
	获取经营活动产生的现金流量净额/营业收入_PIT

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fa_ocftoor",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFaOCFToOrTtM(security:list,*args,**kwargs):
    """
	获取经营活动产生的现金流量净额/营业收入(TTM)_PIT

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fa_ocftoor_ttm",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFaOCFTooAITtM(security:list,*args,**kwargs):
    """
	获取经营活动产生的现金流量净额/经营活动净收益(TTM)_PIT

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fa_ocftooai_ttm",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFaOCFToOpTtM(security:list,*args,**kwargs):
    """
	获取经营活动产生的现金流量净额/营业利润(TTM)_PIT

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fa_ocftoop_ttm",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFaOCFToDebt(security:list,*args,**kwargs):
    """
	获取经营活动产生的现金流量净额/负债合计_PIT

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fa_ocftodebt",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getOCFToOrTtM(security:list,*args,**kwargs):
    """
	获取经营活动产生的现金流量净额/营业收入(TTM,只有最新数据)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"ocftoor_ttm",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getOCFToOperateIncomeTtM(security:list,*args,**kwargs):
    """
	获取经营活动产生的现金流量净额/经营活动净收益(TTM,只有最新数据)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"ocftooperateincome_ttm",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getImNetCashFlowsOperActGap(security:list,*args,**kwargs):
    """
	获取间接法-经营活动现金流量净额差额(特殊报表科目)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"im_net_cash_flows_oper_act_gap",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getImNetCashFlowsOperActGapDetail(security:list,*args,**kwargs):
    """
	获取间接法-经营活动现金流量净额差额说明(特殊报表科目)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"im_net_cash_flows_oper_act_gap_detail",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getImNetCashFlowsOperActNetting(security:list,*args,**kwargs):
    """
	获取间接法-经营活动现金流量净额差额(合计平衡项目)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"im_net_cash_flows_oper_act_netting",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFaOcFpsTtM(security:list,*args,**kwargs):
    """
	获取每股经营活动产生的现金流量净额(TTM)_PIT

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fa_ocfps_ttm",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getOcFps(security:list,*args,**kwargs):
    """
	获取每股经营活动产生的现金流量净额

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"ocfps",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getYoyOCFpS(security:list,*args,**kwargs):
    """
	获取每股经营活动产生的现金流量净额(同比增长率)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"yoyocfps",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWgsDYoyOCFpS(security:list,*args,**kwargs):
    """
	获取每股经营活动产生的现金流量净额(同比增长率)_GSD

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"wgsd_yoyocfps",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWgsDInvestOThCf(security:list,*args,**kwargs):
    """
	获取其他投资活动产生的现金流量净额_GSD

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"wgsd_invest_oth_cf",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWgsDFinOThCf(security:list,*args,**kwargs):
    """
	获取其他筹资活动产生的现金流量净额_GSD

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"wgsd_fin_oth_cf",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getQfaOCFToSales(security:list,*args,**kwargs):
    """
	获取单季度.经营活动产生的现金流量净额/营业收入

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"qfa_ocftosales",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getQfaOCFToOr(security:list,*args,**kwargs):
    """
	获取单季度.经营活动产生的现金流量净额/经营活动净收益

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"qfa_ocftoor",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getOCFTOCFQfa(security:list,*args,**kwargs):
    """
	获取单季度.经营活动产生的现金流量净额占比

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"ocftocf_qfa",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getICfTOCFQfa(security:list,*args,**kwargs):
    """
	获取单季度.投资活动产生的现金流量净额占比

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"icftocf_qfa",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFcFTOCFQfa(security:list,*args,**kwargs):
    """
	获取单季度.筹资活动产生的现金流量净额占比

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fcftocf_qfa",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWgsDQfaOperCf(security:list,*args,**kwargs):
    """
	获取单季度.经营活动产生的现金流量净额_GSD

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"wgsd_qfa_oper_cf",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWgsDQfaInvestCf(security:list,*args,**kwargs):
    """
	获取单季度.投资活动产生的现金流量净额_GSD

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"wgsd_qfa_invest_cf",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWgsDQfaFinCf(security:list,*args,**kwargs):
    """
	获取单季度.筹资活动产生的现金流量净额_GSD

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"wgsd_qfa_fin_cf",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getImNetCashFlowsOperAct(security:list,*args,**kwargs):
    """
	获取间接法-经营活动产生的现金流量净额

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"im_net_cash_flows_oper_act",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getQfaNetCashFlowsOperAct(security:list,*args,**kwargs):
    """
	获取单季度.经营活动产生的现金流量净额

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"qfa_net_cash_flows_oper_act",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getQfaNetCashFlowsInvAct(security:list,*args,**kwargs):
    """
	获取单季度.投资活动产生的现金流量净额

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"qfa_net_cash_flows_inv_act",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getQfaNetCashFlowsFncAct(security:list,*args,**kwargs):
    """
	获取单季度.筹资活动产生的现金流量净额

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"qfa_net_cash_flows_fnc_act",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFaCFogRTtM(security:list,*args,**kwargs):
    """
	获取增长率-经营活动产生的现金流量净额(TTM)_PIT

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fa_cfogr_ttm",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFaCffGrTtM(security:list,*args,**kwargs):
    """
	获取增长率-筹资活动产生的现金流量净额(TTM)_PIT

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fa_cffgr_ttm",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFaCFigRTtM(security:list,*args,**kwargs):
    """
	获取增长率-投资活动产生的现金流量净额(TTM)_PIT

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fa_cfigr_ttm",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWgsDQfaInvestOThCf(security:list,*args,**kwargs):
    """
	获取单季度.其他投资活动产生的现金流量净额_GSD

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"wgsd_qfa_invest_oth_cf",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWgsDQfaFinOThCf(security:list,*args,**kwargs):
    """
	获取单季度.其他筹资活动产生的现金流量净额_GSD

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"wgsd_qfa_fin_oth_cf",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getQfaImNetCashFlowsOperAct(security:list,*args,**kwargs):
    """
	获取单季度.间接法-经营活动产生的现金流量净额

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"qfa_im_net_cash_flows_oper_act",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getDupontAssetsToEquity(security:list,*args,**kwargs):
    """
	获取权益乘数(杜邦分析)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"dupont_assetstoequity",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWgsDDupontAssetsToEquity(security:list,*args,**kwargs):
    """
	获取权益乘数(杜邦分析)_GSD

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"wgsd_dupont_assetstoequity",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getSegmentIndustryItem(security:list,*args,**kwargs):
    """
	获取主营构成(按行业)-项目名称

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"segment_industry_item",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getSegmentIndustrySales1(security:list,*args,**kwargs):
    """
	获取主营构成(按行业)-项目收入

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"segment_industry_sales1",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getSegmentIndustryCost1(security:list,*args,**kwargs):
    """
	获取主营构成(按行业)-项目成本

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"segment_industry_cost1",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getSegmentIndustryProfit1(security:list,*args,**kwargs):
    """
	获取主营构成(按行业)-项目毛利

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"segment_industry_profit1",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getSegmentIndustryGpMargin(security:list,*args,**kwargs):
    """
	获取主营构成(按行业)-项目毛利率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"segment_industry_gpmargin",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getSegmentProductItem(security:list,*args,**kwargs):
    """
	获取主营构成(按产品)-项目名称

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"segment_product_item",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getSegmentProductSales1(security:list,*args,**kwargs):
    """
	获取主营构成(按产品)-项目收入

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"segment_product_sales1",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getSegmentProductCost1(security:list,*args,**kwargs):
    """
	获取主营构成(按产品)-项目成本

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"segment_product_cost1",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getSegmentProductProfit1(security:list,*args,**kwargs):
    """
	获取主营构成(按产品)-项目毛利

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"segment_product_profit1",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getSegmentProductGpMargin(security:list,*args,**kwargs):
    """
	获取主营构成(按产品)-项目毛利率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"segment_product_gpmargin",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getSegmentRegionItem(security:list,*args,**kwargs):
    """
	获取主营构成(按地区)-项目名称

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"segment_region_item",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getSegmentRegionSales1(security:list,*args,**kwargs):
    """
	获取主营构成(按地区)-项目收入

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"segment_region_sales1",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getSegmentRegionCost1(security:list,*args,**kwargs):
    """
	获取主营构成(按地区)-项目成本

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"segment_region_cost1",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getSegmentRegionProfit1(security:list,*args,**kwargs):
    """
	获取主营构成(按地区)-项目毛利

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"segment_region_profit1",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getSegmentRegionGpMargin(security:list,*args,**kwargs):
    """
	获取主营构成(按地区)-项目毛利率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"segment_region_gpmargin",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getSegmentIndustrySales(security:list,*args,**kwargs):
    """
	获取主营构成(按行业)-项目收入(旧)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"segment_industry_sales",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getSegmentIndustryCost(security:list,*args,**kwargs):
    """
	获取主营构成(按行业)-项目成本(旧)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"segment_industry_cost",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getSegmentIndustryProfit(security:list,*args,**kwargs):
    """
	获取主营构成(按行业)-项目毛利(旧)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"segment_industry_profit",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getSegmentProductSales(security:list,*args,**kwargs):
    """
	获取主营构成(按产品)-项目收入(旧)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"segment_product_sales",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getSegmentProductCost(security:list,*args,**kwargs):
    """
	获取主营构成(按产品)-项目成本(旧)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"segment_product_cost",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getSegmentProductProfit(security:list,*args,**kwargs):
    """
	获取主营构成(按产品)-项目毛利(旧)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"segment_product_profit",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getSegmentRegionSales(security:list,*args,**kwargs):
    """
	获取主营构成(按地区)-项目收入(旧)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"segment_region_sales",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getSegmentRegionCost(security:list,*args,**kwargs):
    """
	获取主营构成(按地区)-项目成本(旧)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"segment_region_cost",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getSegmentRegionProfit(security:list,*args,**kwargs):
    """
	获取主营构成(按地区)-项目毛利(旧)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"segment_region_profit",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getStmNoteAuditCategory(security:list,*args,**kwargs):
    """
	获取审计意见类别

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"stmnote_audit_category",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getStmNoteInAuditCategory(security:list,*args,**kwargs):
    """
	获取内控_审计意见类别

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"stmnote_InAudit_category",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getProvDePrAssets(security:list,*args,**kwargs):
    """
	获取资产减值准备

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"prov_depr_assets",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getStmNoteEoItems13(security:list,*args,**kwargs):
    """
	获取资产减值准备(非经常性损益)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"stmnote_Eoitems_13",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getStmNoteReserve21(security:list,*args,**kwargs):
    """
	获取固定资产减值准备合计

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"stmnote_reserve_21",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getStmNoteReserve22(security:list,*args,**kwargs):
    """
	获取固定资产减值准备-房屋、建筑物

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"stmnote_reserve_22",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getStmNoteReserve23(security:list,*args,**kwargs):
    """
	获取固定资产减值准备-机器设备

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"stmnote_reserve_23",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getStmNoteReserve24(security:list,*args,**kwargs):
    """
	获取固定资产减值准备-专用设备

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"stmnote_reserve_24",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getStmNoteReserve25(security:list,*args,**kwargs):
    """
	获取固定资产减值准备-运输工具

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"stmnote_reserve_25",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getStmNoteReserve26(security:list,*args,**kwargs):
    """
	获取固定资产减值准备-通讯设备

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"stmnote_reserve_26",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getStmNoteReserve27(security:list,*args,**kwargs):
    """
	获取固定资产减值准备-电子设备

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"stmnote_reserve_27",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getStmNoteReserve28(security:list,*args,**kwargs):
    """
	获取固定资产减值准备-办公及其它设备

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"stmnote_reserve_28",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getStmNoteReserve29(security:list,*args,**kwargs):
    """
	获取固定资产减值准备-其它设备

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"stmnote_reserve_29",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getStmNoteReserve30(security:list,*args,**kwargs):
    """
	获取无形资产减值准备

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"stmnote_reserve_30",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getStmNoteReserve31(security:list,*args,**kwargs):
    """
	获取无形资产减值准备-专利权

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"stmnote_reserve_31",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getStmNoteReserve32(security:list,*args,**kwargs):
    """
	获取无形资产减值准备-商标权

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"stmnote_reserve_32",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getStmNoteReserve33(security:list,*args,**kwargs):
    """
	获取无形资产减值准备-职工住房使用权

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"stmnote_reserve_33",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getStmNoteReserve34(security:list,*args,**kwargs):
    """
	获取无形资产减值准备-土地使用权

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"stmnote_reserve_34",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getStmNoteInvestmentIncome0007(security:list,*args,**kwargs):
    """
	获取计提投资资产减值准备

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"stmnote_InvestmentIncome_0007",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getQfaProvDePrAssets(security:list,*args,**kwargs):
    """
	获取单季度.资产减值准备

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"qfa_prov_depr_assets",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWgsDLandUseRights(security:list,*args,**kwargs):
    """
	获取土地使用权_GSD

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"wgsd_land_use_rights",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getStmNoteLandUseRights19(security:list,*args,**kwargs):
    """
	获取土地使用权_原值

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"stmnote_LandUseRights_19",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getStmNoteLandUseRights20(security:list,*args,**kwargs):
    """
	获取土地使用权_累计摊销

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"stmnote_LandUseRights_20",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getStmNoteLandUseRights21(security:list,*args,**kwargs):
    """
	获取土地使用权_减值准备

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"stmnote_LandUseRights_21",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getStmNoteLandUseRights22(security:list,*args,**kwargs):
    """
	获取土地使用权_账面价值

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"stmnote_LandUseRights_22",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPrtReverseRepo(security:list,*args,**kwargs):
    """
	获取买入返售金融资产

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"prt_reverserepo",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getStmNoteSPuAr0001(security:list,*args,**kwargs):
    """
	获取买入返售金融资产:证券

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"stmnote_SPUAR_0001",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getStmNoteSPuAr0002(security:list,*args,**kwargs):
    """
	获取买入返售金融资产:票据

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"stmnote_SPUAR_0002",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getStmNoteSPuAr0003(security:list,*args,**kwargs):
    """
	获取买入返售金融资产:贷款

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"stmnote_SPUAR_0003",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getStmNoteSPuAr0004(security:list,*args,**kwargs):
    """
	获取买入返售金融资产:信托及其他受益权

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"stmnote_SPUAR_0004",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getStmNoteSPuAr0005(security:list,*args,**kwargs):
    """
	获取买入返售金融资产:长期应收款

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"stmnote_SPUAR_0005",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getStmNoteSPuAr0006(security:list,*args,**kwargs):
    """
	获取买入返售金融资产:其他担保物

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"stmnote_SPUAR_0006",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getStmNoteSPuAr0007(security:list,*args,**kwargs):
    """
	获取买入返售金融资产:减值准备

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"stmnote_SPUAR_0007",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getStmNoteSPuAr10001(security:list,*args,**kwargs):
    """
	获取买入返售金融资产:股票质押式回购

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"stmnote_SPUAR_10001",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getStmNoteSPuAr10002(security:list,*args,**kwargs):
    """
	获取买入返售金融资产:约定购回式证券

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"stmnote_SPUAR_10002",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getStmNoteSPuAr10003(security:list,*args,**kwargs):
    """
	获取买入返售金融资产:债券买断式回购

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"stmnote_SPUAR_10003",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getStmNoteSPuAr10004(security:list,*args,**kwargs):
    """
	获取买入返售金融资产:债券质押式回购

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"stmnote_SPUAR_10004",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getStmNoteSPuAr10007(security:list,*args,**kwargs):
    """
	获取买入返售金融资产:债券回购

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"stmnote_SPUAR_10007",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getStmNoteSPuAr10005(security:list,*args,**kwargs):
    """
	获取买入返售金融资产:其他

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"stmnote_SPUAR_10005",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getStmNoteSPuAr10006(security:list,*args,**kwargs):
    """
	获取买入返售金融资产合计

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"stmnote_SPUAR_10006",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getStmBs17(security:list,*args,**kwargs):
    """
	获取买入返售金融资产_FUND

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"stm_bs_17",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getStmBsRepoInExChMkt(security:list,*args,**kwargs):
    """
	获取买入返售金融资产(交易所市场)_FUND

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"stm_bs_repoin_exchmkt",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getStmBsRepoInInterBmkT(security:list,*args,**kwargs):
    """
	获取买入返售金融资产(银行间市场)_FUND

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"stm_bs_repoin_interbmkt",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getStmIs3(security:list,*args,**kwargs):
    """
	获取买入返售金融资产收入_FUND

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"stm_is_3",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFinAssetsAvailForSale(security:list,*args,**kwargs):
    """
	获取可供出售金融资产

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fin_assets_avail_for_sale",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getStmNoteFaaViableForSale0001(security:list,*args,**kwargs):
    """
	获取可供出售金融资产:产生的利得/(损失)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"stmnote_FAAviableForSale_0001",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getStmNoteFaaViableForSale0002(security:list,*args,**kwargs):
    """
	获取可供出售金融资产:产生的所得税影响

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"stmnote_FAAviableForSale_0002",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getStmNoteFaaViableForSale0003(security:list,*args,**kwargs):
    """
	获取可供出售金融资产:前期计入其他综合收益当期转入损益的金额

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"stmnote_FAAviableForSale_0003",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getStmNoteFaaViableForSale0004(security:list,*args,**kwargs):
    """
	获取可供出售金融资产公允价值变动

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"stmnote_FAAviableForSale_0004",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getStmNoteImpairmentLoss8(security:list,*args,**kwargs):
    """
	获取可供出售金融资产减值损失

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"stmnote_ImpairmentLoss_8",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getNetInCrDispFinAssetsAvail(security:list,*args,**kwargs):
    """
	获取处置可供出售金融资产净增加额

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"net_incr_disp_fin_assets_avail",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getStmNoteSecuritiesLending3(security:list,*args,**kwargs):
    """
	获取融出证券:可供出售金融资产

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"stmnote_securitieslending_3",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getQfaNetInCrDispFinAssetsAvail(security:list,*args,**kwargs):
    """
	获取单季度.处置可供出售金融资产净增加额

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"qfa_net_incr_disp_fin_assets_avail",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getStmNoteSecuritiesLending1(security:list,*args,**kwargs):
    """
	获取融出证券合计

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"stmnote_securitieslending_1",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getStmNoteSecuritiesLending2(security:list,*args,**kwargs):
    """
	获取融出证券:交易性金融资产

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"stmnote_securitieslending_2",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getStmNoteSecuritiesLending4(security:list,*args,**kwargs):
    """
	获取融出证券:转融通融入证券

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"stmnote_securitieslending_4",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getStmNoteSecuritiesLending5(security:list,*args,**kwargs):
    """
	获取融出证券:转融通融入证券余额

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"stmnote_securitieslending_5",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getStmNoteSecuritiesLending6(security:list,*args,**kwargs):
    """
	获取融出证券:减值准备

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"stmnote_securitieslending_6",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getCashDepositsCentralBank(security:list,*args,**kwargs):
    """
	获取现金及存放中央银行款项

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"cash_deposits_central_bank",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getStmBs1(security:list,*args,**kwargs):
    """
	获取银行存款_FUND

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"stm_bs_1",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPrtCash(security:list,*args,**kwargs):
    """
	获取银行存款

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"prt_cash",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPrtCashToNav(security:list,*args,**kwargs):
    """
	获取银行存款占基金资产净值比

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"prt_cashtonav",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPrtCashToAsset(security:list,*args,**kwargs):
    """
	获取银行存款占基金资产总值比

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"prt_cashtoasset",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPrtCashValueGrowth(security:list,*args,**kwargs):
    """
	获取银行存款市值增长率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"prt_cashvaluegrowth",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPrtCashToNavGrowth(security:list,*args,**kwargs):
    """
	获取银行存款市值占基金资产净值比例增长

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"prt_cashtonavgrowth",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getStmNoteBankDeposit(security:list,*args,**kwargs):
    """
	获取货币资金-银行存款

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"stmnote_bankdeposit",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getCashToStDebt(security:list,*args,**kwargs):
    """
	获取货币资金/短期债务

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"cashtostdebt",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getYoYCash(security:list,*args,**kwargs):
    """
	获取货币资金增长率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"yoy_cash",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWgsDCashToLiqDebt(security:list,*args,**kwargs):
    """
	获取货币资金/流动负债_GSD

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"wgsd_cashtoliqdebt",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getStm07BsReItsCash(security:list,*args,**kwargs):
    """
	获取货币资金

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"stm07_bs_reits_cash",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getStmNoteDpsT4412(security:list,*args,**kwargs):
    """
	获取货币资金合计

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"stmnote_DPST_4412",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getStmNoteCashInvault(security:list,*args,**kwargs):
    """
	获取货币资金-库存现金

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"stmnote_cashinvault",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getStmNoteBorrow4512(security:list,*args,**kwargs):
    """
	获取借款合计

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"stmnote_Borrow_4512",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getStBorrow(security:list,*args,**kwargs):
    """
	获取短期借款

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"st_borrow",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getLtBorrow(security:list,*args,**kwargs):
    """
	获取长期借款

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"lt_borrow",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPledgeLoan(security:list,*args,**kwargs):
    """
	获取质押借款

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"pledge_loan",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getCashRecpBorrow(security:list,*args,**kwargs):
    """
	获取取得借款收到的现金

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"cash_recp_borrow",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getStmNoteStBorrow4512(security:list,*args,**kwargs):
    """
	获取短期借款小计

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"stmnote_STBorrow_4512",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getStmNoteLtBorrow4512(security:list,*args,**kwargs):
    """
	获取长期借款小计

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"stmnote_LTBorrow_4512",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getStmBs70(security:list,*args,**kwargs):
    """
	获取短期借款_FUND

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"stm_bs_70",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFaLtBorrowToAsset(security:list,*args,**kwargs):
    """
	获取长期借款/资产总计_PIT

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fa_ltborrowtoasset",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getBusLoanRatioN(security:list,*args,**kwargs):
    """
	获取国际商业借款比率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"busloanratio_n",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getBusLoanRatio(security:list,*args,**kwargs):
    """
	获取国际商业借款比率(旧)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"busloanratio",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getStmNoteStBorrow4506(security:list,*args,**kwargs):
    """
	获取美元短期借款(折算人民币)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"stmnote_STBorrow_4506",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getStmNoteStBorrow4507(security:list,*args,**kwargs):
    """
	获取日元短期借款(折算人民币)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"stmnote_STBorrow_4507",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getStmNoteStBorrow4508(security:list,*args,**kwargs):
    """
	获取欧元短期借款(折算人民币)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"stmnote_STBorrow_4508",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getStmNoteStBorrow4509(security:list,*args,**kwargs):
    """
	获取港币短期借款(折算人民币)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"stmnote_STBorrow_4509",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getStmNoteStBorrow4510(security:list,*args,**kwargs):
    """
	获取英镑短期借款(折算人民币)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"stmnote_STBorrow_4510",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getStmNoteLtBorrow4506(security:list,*args,**kwargs):
    """
	获取美元长期借款(折算人民币)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"stmnote_LTBorrow_4506",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getStmNoteLtBorrow4507(security:list,*args,**kwargs):
    """
	获取日元长期借款(折算人民币)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"stmnote_LTBorrow_4507",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getStmNoteLtBorrow4508(security:list,*args,**kwargs):
    """
	获取欧元长期借款(折算人民币)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"stmnote_LTBorrow_4508",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getStmNoteLtBorrow4509(security:list,*args,**kwargs):
    """
	获取港币长期借款(折算人民币)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"stmnote_LTBorrow_4509",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getStmNoteLtBorrow4510(security:list,*args,**kwargs):
    """
	获取英镑长期借款(折算人民币)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"stmnote_LTBorrow_4510",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getBorrowCentralBank(security:list,*args,**kwargs):
    """
	获取向中央银行借款

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"borrow_central_bank",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getNetInCrLoansCentralBank(security:list,*args,**kwargs):
    """
	获取向中央银行借款净增加额

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"net_incr_loans_central_bank",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getStmNoteStBorrow4505(security:list,*args,**kwargs):
    """
	获取人民币短期借款

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"stmnote_STBorrow_4505",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getStmNoteLtBorrow4505(security:list,*args,**kwargs):
    """
	获取人民币长期借款

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"stmnote_LTBorrow_4505",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getQfaCashRecpBorrow(security:list,*args,**kwargs):
    """
	获取单季度.取得借款收到的现金

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"qfa_cash_recp_borrow",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getStmNoteStBorrow4511(security:list,*args,**kwargs):
    """
	获取其他货币短期借款(折算人民币)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"stmnote_STBorrow_4511",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getStmNoteLtBorrow4511(security:list,*args,**kwargs):
    """
	获取其他货币长期借款(折算人民币)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"stmnote_LTBorrow_4511",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getStmNoteOthers7636(security:list,*args,**kwargs):
    """
	获取一年内到期的长期借款

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"stmnote_others_7636",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getQfaNetInCrLoansCentralBank(security:list,*args,**kwargs):
    """
	获取单季度.向中央银行借款净增加额

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"qfa_net_incr_loans_central_bank",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getExtraordinary(security:list,*args,**kwargs):
    """
	获取非经常性损益

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"extraordinary",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getStmNoteEoItems21(security:list,*args,**kwargs):
    """
	获取非经常性损益项目小计

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"stmnote_Eoitems_21",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getStmNoteEoItems24(security:list,*args,**kwargs):
    """
	获取非经常性损益项目合计

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"stmnote_Eoitems_24",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFaNRgl(security:list,*args,**kwargs):
    """
	获取非经常性损益_PIT

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fa_nrgl",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFaDeductProfitTtM(security:list,*args,**kwargs):
    """
	获取扣除非经常性损益后的净利润(TTM)_PIT

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fa_deductprofit_ttm",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getDpYoY(security:list,*args,**kwargs):
    """
	获取扣除非经常性损益后的净利润(同比增长率)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"dp_yoy",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getDeductedProfitTtM2(security:list,*args,**kwargs):
    """
	获取扣除非经常性损益后的净利润(TTM)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"deductedprofit_ttm2",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getDeductedProfit(security:list,*args,**kwargs):
    """
	获取扣除非经常性损益后的净利润

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"deductedprofit",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getDeductedProfitTtM3(security:list,*args,**kwargs):
    """
	获取扣除非经常性损益后的净利润(TTM)_GSD

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"deductedprofit_ttm3",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getDeductedProfitYoY(security:list,*args,**kwargs):
    """
	获取单季度.扣除非经常性损益后的净利润同比增长率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"deductedprofit_yoy",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getValPeDeductedTtM(security:list,*args,**kwargs):
    """
	获取市盈率PE(TTM,扣除非经常性损益)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"val_pe_deducted_ttm",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getImpairToGr(security:list,*args,**kwargs):
    """
	获取资产减值损失/营业总收入

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"impairtogr",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getImpairToOp(security:list,*args,**kwargs):
    """
	获取资产减值损失/营业利润

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"impairtoOP",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getImpairToGrTtM2(security:list,*args,**kwargs):
    """
	获取资产减值损失/营业总收入(TTM)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"impairtogr_ttm2",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getImpairmentTtM2(security:list,*args,**kwargs):
    """
	获取资产减值损失(TTM)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"impairment_ttm2",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getImpairLossAssets(security:list,*args,**kwargs):
    """
	获取资产减值损失

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"impair_loss_assets",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFaImpairToGrTtM(security:list,*args,**kwargs):
    """
	获取资产减值损失/营业总收入(TTM)_PIT

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fa_impairtogr_ttm",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFaImpairLossTtM(security:list,*args,**kwargs):
    """
	获取资产减值损失(TTM)_PIT

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fa_impairloss_ttm",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getImpairToGrTtM(security:list,*args,**kwargs):
    """
	获取资产减值损失/营业总收入(TTM,只有最新数据)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"impairtogr_ttm",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getImpairmentTtM(security:list,*args,**kwargs):
    """
	获取资产减值损失(TTM,只有最新数据)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"impairment_ttm",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getOtherAssetsImpairLoss(security:list,*args,**kwargs):
    """
	获取其他资产减值损失

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"other_assets_impair_loss",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getStmNoteImpairmentLoss10(security:list,*args,**kwargs):
    """
	获取固定资产减值损失

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"stmnote_ImpairmentLoss_10",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getImpairToOpQfa(security:list,*args,**kwargs):
    """
	获取单季度.资产减值损失/营业利润

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"impairtoop_qfa",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getQfaImpairLossAssets(security:list,*args,**kwargs):
    """
	获取单季度.资产减值损失

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"qfa_impair_loss_assets",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getQfaOtherImpair(security:list,*args,**kwargs):
    """
	获取单季度.其他资产减值损失

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"qfa_other_impair",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getStmNoteFineXp4(security:list,*args,**kwargs):
    """
	获取财务费用明细-利息支出

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"stmnote_finexp_4",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getStmNoteFineXp5(security:list,*args,**kwargs):
    """
	获取财务费用明细-利息收入

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"stmnote_finexp_5",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getStmNoteFineXp13(security:list,*args,**kwargs):
    """
	获取财务费用明细-利息资本化金额

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"stmnote_finexp_13",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getStmNoteFineXp6(security:list,*args,**kwargs):
    """
	获取财务费用明细-汇兑损益

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"stmnote_finexp_6",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getStmNoteFineXp7(security:list,*args,**kwargs):
    """
	获取财务费用明细-手续费

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"stmnote_finexp_7",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getStmNoteFineXp8(security:list,*args,**kwargs):
    """
	获取财务费用明细-其他

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"stmnote_finexp_8",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFaRdExpYoY(security:list,*args,**kwargs):
    """
	获取研发费用同比增长

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fa_rdexp_yoy",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWgsDRdExp(security:list,*args,**kwargs):
    """
	获取研发费用_GSD

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"wgsd_rd_exp",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getStm07IsReItsRdFee(security:list,*args,**kwargs):
    """
	获取研发费用

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"stm07_is_reits_rdfee",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getStmNoteRdSalary(security:list,*args,**kwargs):
    """
	获取研发费用-工资薪酬

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"stmnote_rdsalary",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getStmNoteRdDa(security:list,*args,**kwargs):
    """
	获取研发费用-折旧摊销

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"stmnote_rdda",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getStmNoteRdLease(security:list,*args,**kwargs):
    """
	获取研发费用-租赁费

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"stmnote_rdlease",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getStmNoteRdInv(security:list,*args,**kwargs):
    """
	获取研发费用-直接投入

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"stmnote_rdinv",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getStmNoteRdOthers(security:list,*args,**kwargs):
    """
	获取研发费用-其他

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"stmnote_rdothers",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getStmNoteRdExpCostToSales(security:list,*args,**kwargs):
    """
	获取研发费用占营业收入比例

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"stmnote_Rdexp_costtosales",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWgsDQfaRdExp(security:list,*args,**kwargs):
    """
	获取单季度.研发费用_GSD

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"wgsd_qfa_rd_exp",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getQfaRdExp(security:list,*args,**kwargs):
    """
	获取单季度.研发费用

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"qfa_rd_exp",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getTaxToEBT(security:list,*args,**kwargs):
    """
	获取所得税/利润总额

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"taxtoebt",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getTaxTtM(security:list,*args,**kwargs):
    """
	获取所得税(TTM)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"tax_ttm",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getTaxTtM2(security:list,*args,**kwargs):
    """
	获取所得税(TTM)_GSD

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"tax_ttm2",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWgsDIncTax(security:list,*args,**kwargs):
    """
	获取所得税_GSD

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"wgsd_inc_tax",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getTax(security:list,*args,**kwargs):
    """
	获取所得税

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"tax",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getStmNoteEoItems22(security:list,*args,**kwargs):
    """
	获取所得税影响数

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"stmnote_Eoitems_22",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getStmNoteIncomeTax6(security:list,*args,**kwargs):
    """
	获取所得税费用合计

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"stmnote_incometax_6",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getStmIs78(security:list,*args,**kwargs):
    """
	获取所得税费用_FUND

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"stm_is_78",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFaTaxTtM(security:list,*args,**kwargs):
    """
	获取所得税(TTM)_PIT

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fa_tax_ttm",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getDeferredTaxAssets(security:list,*args,**kwargs):
    """
	获取递延所得税资产

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"deferred_tax_assets",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getDeferredTaxLiaB(security:list,*args,**kwargs):
    """
	获取递延所得税负债

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"deferred_tax_liab",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getDecrDeferredIncTaxAssets(security:list,*args,**kwargs):
    """
	获取递延所得税资产减少

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"decr_deferred_inc_tax_assets",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getInCrDeferredIncTaxLiaB(security:list,*args,**kwargs):
    """
	获取递延所得税负债增加

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"incr_deferred_inc_tax_liab",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getStmNoteTax(security:list,*args,**kwargs):
    """
	获取年末所得税率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"stmnote_tax",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getStmNoteIncomeTax1(security:list,*args,**kwargs):
    """
	获取当期所得税:中国大陆

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"stmnote_incometax_1",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getStmNoteIncomeTax2(security:list,*args,**kwargs):
    """
	获取当期所得税:中国香港

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"stmnote_incometax_2",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getStmNoteIncomeTax3(security:list,*args,**kwargs):
    """
	获取当期所得税:其他境外

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"stmnote_incometax_3",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getStmNoteIncomeTax5(security:list,*args,**kwargs):
    """
	获取递延所得税

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"stmnote_incometax_5",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWgsDQfaIncTax(security:list,*args,**kwargs):
    """
	获取单季度.所得税_GSD

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"wgsd_qfa_inc_tax",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getQfaTax(security:list,*args,**kwargs):
    """
	获取单季度.所得税

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"qfa_tax",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getStmNoteIncomeTax4(security:list,*args,**kwargs):
    """
	获取以前年度所得税调整

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"stmnote_incometax_4",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getQfaDeferredTaxAssetsDecr(security:list,*args,**kwargs):
    """
	获取单季度.递延所得税资产减少

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"qfa_deferred_tax_assets_decr",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getQfaInCrDeferredIncTaxLiaB(security:list,*args,**kwargs):
    """
	获取单季度.递延所得税负债增加

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"qfa_incr_deferred_inc_tax_liab",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getRiskBetaUnIncomeTaxRate(security:list,*args,**kwargs):
    """
	获取Beta(剔除所得税率)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"risk_betaunincometaxrate",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWgsDGwIntang(security:list,*args,**kwargs):
    """
	获取商誉及无形资产_GSD

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"wgsd_gw_intang",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getGoodwill(security:list,*args,**kwargs):
    """
	获取商誉

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"goodwill",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getStmNoteImpairmentLoss6(security:list,*args,**kwargs):
    """
	获取商誉减值损失

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"stmnote_ImpairmentLoss_6",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getStmNoteGoodwillDetail(security:list,*args,**kwargs):
    """
	获取商誉-账面价值

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"stmnote_goodwilldetail",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getStmNoteGoodwillImpairment(security:list,*args,**kwargs):
    """
	获取商誉-减值准备

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"stmnote_goodwillimpairment",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getEMplBenPayable(security:list,*args,**kwargs):
    """
	获取应付职工薪酬

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"empl_ben_payable",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getStmNoteEMplPayableAdd(security:list,*args,**kwargs):
    """
	获取应付职工薪酬合计:本期增加

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"stmnote_emplpayable_add",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getStmNoteEMplPayableSb(security:list,*args,**kwargs):
    """
	获取应付职工薪酬合计:期初余额

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"stmnote_emplpayable_sb",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getStmNoteEMplPayableEb(security:list,*args,**kwargs):
    """
	获取应付职工薪酬合计:期末余额

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"stmnote_emplpayable_eb",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getStmNoteEMplPayableDe(security:list,*args,**kwargs):
    """
	获取应付职工薪酬合计:本期减少

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"stmnote_emplpayable_de",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getLtEMplBenPayable(security:list,*args,**kwargs):
    """
	获取长期应付职工薪酬

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"lt_empl_ben_payable",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getStmNoteTaxBusiness(security:list,*args,**kwargs):
    """
	获取营业税金及附加合计

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"stmnote_tax_business",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFaOperTaxTtM(security:list,*args,**kwargs):
    """
	获取营业税金及附加(TTM)_PIT

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fa_opertax_ttm",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getStmNoteTaxOTh(security:list,*args,**kwargs):
    """
	获取其他营业税金及附加

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"stmnote_tax_oth",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getStmIssuingDate(security:list,*args,**kwargs):
    """
	获取定期报告披露日期

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"stm_issuingdate",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getStmIssuingDateFs(security:list,*args,**kwargs):
    """
	获取定期报告正报披露日期

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"stm_issuingdate_fs",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getStmPredictIssuingDate(security:list,*args,**kwargs):
    """
	获取定期报告预计披露日期

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"stm_predict_issuingdate",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getStmRpTS(security:list,*args,**kwargs):
    """
	获取报告起始日期

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"stm_rpt_s",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getStmRpTE(security:list,*args,**kwargs):
    """
	获取报告截止日期

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"stm_rpt_e",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getLatelyRdBt(security:list,*args,**kwargs):
    """
	获取最新报告期

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"latelyrd_bt",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFaErrorCorrectionDate(security:list,*args,**kwargs):
    """
	获取会计差错更正披露日期

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fa_errorcorrectiondate",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFaErrorCorrectionOrNot(security:list,*args,**kwargs):
    """
	获取是否存在会计差错更正

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fa_errorcorrectionornot",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getStmNoteAuditAm(security:list,*args,**kwargs):
    """
	获取会计准则类型

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"stmnote_audit_am",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPerformanceTime(security:list,*args,**kwargs):
    """
	获取业绩说明会时间

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"performancetime",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPerformanceDate(security:list,*args,**kwargs):
    """
	获取业绩说明会日期

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"performancedate",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getEsGEScoreWind(security:list,*args,**kwargs):
    """
	获取环境维度得分

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"esg_escore_wind",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getEsGSScoreWind(security:list,*args,**kwargs):
    """
	获取社会维度得分

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"esg_sscore_wind",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getEsGGScoreWind(security:list,*args,**kwargs):
    """
	获取治理维度得分

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"esg_gscore_wind",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIssueFeeFeeSum(security:list,*args,**kwargs):
    """
	获取发行费用合计

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"issuefee_feesum",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIpoExpense2(security:list,*args,**kwargs):
    """
	获取首发发行费用

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"ipo_expense2",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIpoExpense(security:list,*args,**kwargs):
    """
	获取首发发行费用(旧)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"ipo_expense",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getCbListAnnoCeDate(security:list,*args,**kwargs):
    """
	获取发行结果公告日

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"cb_list_annocedate",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundApprovedDate(security:list,*args,**kwargs):
    """
	获取基金获批注册日期

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_approveddate",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIssueAnnouncedAte(security:list,*args,**kwargs):
    """
	获取发行公告日

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"issue_announcedate",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getTenderAnceDate(security:list,*args,**kwargs):
    """
	获取发行公告日期

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"tender_ancedate",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFellowAnnCeDate(security:list,*args,**kwargs):
    """
	获取上网发行公告日

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fellow_anncedate",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIssueDate(security:list,*args,**kwargs):
    """
	获取发行日期

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"issue_date",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIpoIssueDate(security:list,*args,**kwargs):
    """
	获取首发发行日期

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"ipo_issuedate",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFellowIssueDatePp(security:list,*args,**kwargs):
    """
	获取定增发行日期

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fellow_issuedate_pp",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getCbListDToNl(security:list,*args,**kwargs):
    """
	获取网上发行日期

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"cb_list_dtonl",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getCbListDateInStOff(security:list,*args,**kwargs):
    """
	获取网下向机构投资者发行日期

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"cb_list_dateinstoff",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIssueType(security:list,*args,**kwargs):
    """
	获取发行方式

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"issue_type",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIpoType(security:list,*args,**kwargs):
    """
	获取首发发行方式

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"ipo_type",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFellowIssueType(security:list,*args,**kwargs):
    """
	获取增发发行方式

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fellow_issuetype",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIssueObject(security:list,*args,**kwargs):
    """
	获取发行对象

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"issue_object",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFellowShareholders(security:list,*args,**kwargs):
    """
	获取增发发行对象

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fellow_shareholders",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIssueUnit(security:list,*args,**kwargs):
    """
	获取发行份额

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"issue_unit",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIssueTotalUnit(security:list,*args,**kwargs):
    """
	获取发行总份额

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"issue_totalunit",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundReItsIssueSize(security:list,*args,**kwargs):
    """
	获取发行规模

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_reitsissuesize",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundActualScale(security:list,*args,**kwargs):
    """
	获取实际发行规模

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_actualscale",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIssueTotalSize(security:list,*args,**kwargs):
    """
	获取发行总规模

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"issue_totalsize",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIssueInitiator(security:list,*args,**kwargs):
    """
	获取基金发起人

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"issue_initiator",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIssueLeadUnderwriter(security:list,*args,**kwargs):
    """
	获取基金主承销商

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"issue_leadunderwriter",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIssueDeputy(security:list,*args,**kwargs):
    """
	获取基金销售代理人

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"issue_deputy",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIssueNominator(security:list,*args,**kwargs):
    """
	获取基金上市推荐人

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"issue_nominator",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIssueOeClsPeriod(security:list,*args,**kwargs):
    """
	获取发行封闭期

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"issue_oeclsperiod",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIssueOeCNdNetPurchase(security:list,*args,**kwargs):
    """
	获取成立条件-净认购份额

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"issue_oecndnetpurchase",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIssueOeCNdPurchasers(security:list,*args,**kwargs):
    """
	获取成立条件-认购户数

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"issue_oecndpurchasers",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIssueOEfMaxCollection(security:list,*args,**kwargs):
    """
	获取募集份额上限

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"issue_oef_maxcollection",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIssueOEfConfirmRatio(security:list,*args,**kwargs):
    """
	获取认购份额确认比例

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"issue_oef_confirmratio",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIssueOEfNumPurchasers(security:list,*args,**kwargs):
    """
	获取开放式基金认购户数

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"issue_oef_numpurchasers",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIssueEtFDealShareOnMarket(security:list,*args,**kwargs):
    """
	获取上市交易份额

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"issue_etfdealshareonmarket",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIssueOnlineCashOfferingSymbol(security:list,*args,**kwargs):
    """
	获取网上现金发售代码

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"issue_onlinecashofferingsymbol",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIssueFirstMarketFundCode(security:list,*args,**kwargs):
    """
	获取一级市场基金代码

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"issue_firstmarketfundcode",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIssueOEfMThDInD(security:list,*args,**kwargs):
    """
	获取个人投资者认购方式

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"issue_oef_mthdind",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIssueOEfMinamTinD(security:list,*args,**kwargs):
    """
	获取个人投资者认购金额下限

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"issue_oef_minamtind",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIssueOEfMaxAmtInD(security:list,*args,**kwargs):
    """
	获取个人投资者认购金额上限

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"issue_oef_maxamtind",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIssueOEfStartDateInD(security:list,*args,**kwargs):
    """
	获取个人投资者认购起始日

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"issue_oef_startdateind",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIssueOEfEnddateInD(security:list,*args,**kwargs):
    """
	获取个人投资者认购终止日

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"issue_oef_enddateind",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIssueOEfMThDInSt(security:list,*args,**kwargs):
    """
	获取封闭期机构投资者认购方式

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"issue_oef_mthdinst",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIssueOEfStartDateInSt(security:list,*args,**kwargs):
    """
	获取机构投资者设立认购起始日

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"issue_oef_startdateinst",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIssueOEfDndDateInSt(security:list,*args,**kwargs):
    """
	获取机构投资者设立认购终止日

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"issue_oef_dnddateinst",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIssueOEfMinamTinSt(security:list,*args,**kwargs):
    """
	获取封闭期机构投资者认购下限

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"issue_oef_minamtinst",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIssueOEfMaxAmtInSt(security:list,*args,**kwargs):
    """
	获取封闭期机构投资者认购上限

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"issue_oef_maxamtinst",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIssueCefInIPurchase(security:list,*args,**kwargs):
    """
	获取封闭式基金认购数量

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"issue_cef_inipurchase",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIssueCefOverSub(security:list,*args,**kwargs):
    """
	获取封闭式基金超额认购倍数

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"issue_cef_oversub",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIssueCefSuccRatio(security:list,*args,**kwargs):
    """
	获取封闭式基金中签率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"issue_cef_succratio",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIssueRaSingIsStartEarly(security:list,*args,**kwargs):
    """
	获取是否提前开始募集

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"issue_rasing_isstartearly",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIssueRaSingIsStartDeferred(security:list,*args,**kwargs):
    """
	获取是否延期募集

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"issue_rasing_isstartdeferred",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIssueRaSingIsEndEarly(security:list,*args,**kwargs):
    """
	获取是否提前结束募集

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"issue_rasing_isendearly",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIssueRaSingIsEndDeferred(security:list,*args,**kwargs):
    """
	获取是否延长募集期

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"issue_rasing_isenddeferred",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIssueOEfDays(security:list,*args,**kwargs):
    """
	获取认购天数

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"issue_oef_days",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getDivPerUnit(security:list,*args,**kwargs):
    """
	获取单位年度分红

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"div_perunit",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getDivAccumulatedPerUnit(security:list,*args,**kwargs):
    """
	获取单位累计分红

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"div_accumulatedperunit",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getDivPayOut(security:list,*args,**kwargs):
    """
	获取年度分红总额

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"div_payout",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getDivTimes(security:list,*args,**kwargs):
    """
	获取年度分红次数

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"div_times",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getDivAccumulatedPayOut(security:list,*args,**kwargs):
    """
	获取累计分红总额

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"div_accumulatedpayout",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getDivAuALaCcmDiv3(security:list,*args,**kwargs):
    """
	获取年度累计分红总额

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"div_aualaccmdiv3",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getDivAuALaCcmDivArd(security:list,*args,**kwargs):
    """
	获取年度累计分红总额(已宣告)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"div_aualaccmdiv_ard",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getDivAuALaCcmDiv(security:list,*args,**kwargs):
    """
	获取年度累计分红总额(沪深)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"div_aualaccmdiv",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getDivAccumulatedTimes(security:list,*args,**kwargs):
    """
	获取累计分红次数

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"div_accumulatedtimes",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getDivPeriodPerUnit(security:list,*args,**kwargs):
    """
	获取区间单位分红

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"div_periodperunit",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getDivPeriodPayOut(security:list,*args,**kwargs):
    """
	获取区间分红总额

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"div_periodpayout",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getDivPeriodTimes(security:list,*args,**kwargs):
    """
	获取区间分红次数

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"div_periodtimes",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getDivClause(security:list,*args,**kwargs):
    """
	获取分红条款

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"div_clause",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getCacLawsuitNum(security:list,*args,**kwargs):
    """
	获取区间诉讼次数

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"cac_lawsuitnum",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getCacLawsuitAmount(security:list,*args,**kwargs):
    """
	获取区间诉讼涉案金额

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"cac_lawsuitamount",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getCacIllegalityNum(security:list,*args,**kwargs):
    """
	获取区间违规处罚次数

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"cac_illegalitynum",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getCacIllegalityAmount(security:list,*args,**kwargs):
    """
	获取区间违规处罚金额

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"cac_illegalityamount",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getUnitNonTradable(security:list,*args,**kwargs):
    """
	获取未上市流通基金份数(封闭式)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"unit_nontradable",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getUnitTradable(security:list,*args,**kwargs):
    """
	获取已上市流通基金份数(封闭式)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"unit_tradable",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPrtTotalAsset(security:list,*args,**kwargs):
    """
	获取基金资产总值

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"prt_totalasset",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPrtTotalAssetChange(security:list,*args,**kwargs):
    """
	获取基金资产总值变动

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"prt_totalassetchange",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPrtTotalAssetChangeRatio(security:list,*args,**kwargs):
    """
	获取基金资产总值变动率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"prt_totalassetchangeratio",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPrtNavToAsset(security:list,*args,**kwargs):
    """
	获取基金净值占基金资产总值比

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"prt_navtoasset",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPrtStockToAsset(security:list,*args,**kwargs):
    """
	获取股票市值占基金资产总值比

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"prt_stocktoasset",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPrtBondToAsset(security:list,*args,**kwargs):
    """
	获取债券市值占基金资产总值比

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"prt_bondtoasset",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPrtFundToAsset(security:list,*args,**kwargs):
    """
	获取基金市值占基金资产总值比

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"prt_fundtoasset",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPrtWarrantToAsset(security:list,*args,**kwargs):
    """
	获取权证市值占基金资产总值比

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"prt_warranttoasset",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPrtOtherToAsset(security:list,*args,**kwargs):
    """
	获取其他资产占基金资产总值比

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"prt_othertoasset",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPrtGovernmentBondToAsset(security:list,*args,**kwargs):
    """
	获取国债市值占基金资产总值比

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"prt_governmentbondtoasset",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPrtFinancialBondToAsset(security:list,*args,**kwargs):
    """
	获取金融债市值占基金资产总值比

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"prt_financialbondtoasset",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPrtCorporateBondsToAsset(security:list,*args,**kwargs):
    """
	获取企业债市值占基金资产总值比

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"prt_corporatebondstoasset",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPrtConvertibleBondToAsset(security:list,*args,**kwargs):
    """
	获取可转债市值占基金资产总值比

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"prt_convertiblebondtoasset",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPrtStockValueIndustryToAsset2(security:list,*args,**kwargs):
    """
	获取分行业市值占基金资产总值比

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"prt_stockvalue_industrytoasset2",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPrtHeavilyHeldStockToAsset(security:list,*args,**kwargs):
    """
	获取重仓股市值占基金资产总值比

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"prt_heavilyheldstocktoasset",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPrtHkStockToAsset(security:list,*args,**kwargs):
    """
	获取港股投资市值占基金资产总值比

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"prt_hkstocktoasset",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getMmFReverseRepoToAsset(security:list,*args,**kwargs):
    """
	获取买入返售证券占基金资产总值比例

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"mmf_reverserepotoasset",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPrtCentralBankBillToAsset(security:list,*args,**kwargs):
    """
	获取央行票据市值占基金资产总值比

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"prt_centralbankbilltoasset",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPrtStockValueTopIndustryToAsset2(security:list,*args,**kwargs):
    """
	获取重仓行业市值占基金资产总值比

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"prt_stockvalue_topindustrytoasset2",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPrtHeavilyHeldBondToAsset(security:list,*args,**kwargs):
    """
	获取重仓债券市值占基金资产总值比

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"prt_heavilyheldbondtoasset",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPrtHeavilyHeldFundToAsset(security:list,*args,**kwargs):
    """
	获取重仓基金市值占基金资产总值比

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"prt_heavilyheldfundtoasset",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPrtPFbToAsset(security:list,*args,**kwargs):
    """
	获取政策性金融债市值占基金资产总值比

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"prt_pfbtoasset",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPrtCorporateBondToAsset(security:list,*args,**kwargs):
    """
	获取企业发行债券市值占基金资产总值比

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"prt_corporatebondtoasset",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPrtHeavilyHeldAbsToAsset(security:list,*args,**kwargs):
    """
	获取重仓资产支持证券市值占基金资产总值比

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"prt_heavilyheldabstoasset",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPrtSecLendingValueToAsset(security:list,*args,**kwargs):
    """
	获取转融通证券出借业务市值占基金资产总值比

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"prt_seclendingvaluetoasset",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPrtNetAsset(security:list,*args,**kwargs):
    """
	获取基金资产净值

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"prt_netasset",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPrtNetAssetChange(security:list,*args,**kwargs):
    """
	获取基金资产净值变动

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"prt_netassetchange",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPrtNetAssetChangeRatio(security:list,*args,**kwargs):
    """
	获取基金资产净值变动率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"prt_netassetchangeratio",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPrtCurrency(security:list,*args,**kwargs):
    """
	获取报告期基金资产净值币种

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"prt_currency",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPrtStocktonAv(security:list,*args,**kwargs):
    """
	获取股票市值占基金资产净值比

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"prt_stocktonav",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPrtBondToNav(security:list,*args,**kwargs):
    """
	获取债券市值占基金资产净值比

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"prt_bondtonav",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPrtFundToNav(security:list,*args,**kwargs):
    """
	获取基金市值占基金资产净值比

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"prt_fundtonav",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPrtWarrantToNav(security:list,*args,**kwargs):
    """
	获取权证市值占基金资产净值比

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"prt_warranttonav",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPrtOtherToNav(security:list,*args,**kwargs):
    """
	获取其他资产占基金资产净值比

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"prt_othertonav",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPrtStocktonAvGrowth(security:list,*args,**kwargs):
    """
	获取股票市值占基金资产净值比例增长

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"prt_stocktonavgrowth",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPrtBondToNavGrowth(security:list,*args,**kwargs):
    """
	获取债券市值占基金资产净值比例增长

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"prt_bondtonavgrowth",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPrtFundToNavGrowth(security:list,*args,**kwargs):
    """
	获取基金市值占基金资产净值比例增长

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"prt_fundtonavgrowth",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPrtWarrantToNavGrowth(security:list,*args,**kwargs):
    """
	获取权证市值占基金资产净值比例增长

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"prt_warranttonavgrowth",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPrtGovernmentBondToNav(security:list,*args,**kwargs):
    """
	获取国债市值占基金资产净值比

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"prt_governmentbondtonav",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPrtGovernmentBondToNavGrowth(security:list,*args,**kwargs):
    """
	获取国债市值占基金资产净值比例增长

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"prt_governmentbondtonavgrowth",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPrtFinancialBondToNav(security:list,*args,**kwargs):
    """
	获取金融债市值占基金资产净值比

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"prt_financialbondtonav",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPrtCorporateBondsToNav(security:list,*args,**kwargs):
    """
	获取企业债市值占基金资产净值比

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"prt_corporatebondstonav",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPrtConvertibleBondToNav(security:list,*args,**kwargs):
    """
	获取可转债市值占基金资产净值比

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"prt_convertiblebondtonav",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPrtFinancialBondToNavGrowth(security:list,*args,**kwargs):
    """
	获取金融债市值占基金资产净值比例增长

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"prt_financialbondtonavgrowth",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPrtCorporateBondsToNavGrowth(security:list,*args,**kwargs):
    """
	获取企业债市值占基金资产净值比例增长

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"prt_corporatebondstonavgrowth",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPrtConvertibleBondToNavGrowth(security:list,*args,**kwargs):
    """
	获取可转债市值占基金资产净值比例增长

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"prt_convertiblebondtonavgrowth",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPrtStockValueIndustryToNav2(security:list,*args,**kwargs):
    """
	获取分行业市值占基金资产净值比

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"prt_stockvalue_industrytonav2",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPrtStockValueIndustryToNavGrowth2(security:list,*args,**kwargs):
    """
	获取分行业市值占基金资产净值比增长

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"prt_stockvalue_industrytonavgrowth2",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPrtIndustryToNavGrowthWind(security:list,*args,**kwargs):
    """
	获取分行业市值占基金资产净值比增长(Wind)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"prt_industrytonavgrowth_wind",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPrtIndustryToNavGrowthCitiC(security:list,*args,**kwargs):
    """
	获取分行业市值占基金资产净值比增长(中信)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"prt_industrytonavgrowth_citic",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPrtIndustryToNavGrowthSw(security:list,*args,**kwargs):
    """
	获取分行业市值占基金资产净值比增长(申万)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"prt_industrytonavgrowth_sw",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPrtHeavilyHeldStocktonAv(security:list,*args,**kwargs):
    """
	获取重仓股市值占基金资产净值比

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"prt_heavilyheldstocktonav",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getMmFDifferentPtMToNav(security:list,*args,**kwargs):
    """
	获取各期限资产占基金资产净值比例

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"mmf_differentptmtonav",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPrtHkStocktonAv(security:list,*args,**kwargs):
    """
	获取港股投资市值占基金资产净值比

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"prt_hkstocktonav",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPrtReverseRepoToNav(security:list,*args,**kwargs):
    """
	获取买入返售证券占基金资产净值比例

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"prt_reverserepotonav",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPrtOtherToNavGrowth(security:list,*args,**kwargs):
    """
	获取其他资产市值占基金资产净值比例增长

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"prt_othertonavgrowth",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPrtCdsToNav(security:list,*args,**kwargs):
    """
	获取同业存单市值占基金资产净值比

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"prt_CDstonav",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPrtCentralBankBillToNav(security:list,*args,**kwargs):
    """
	获取央行票据市值占基金资产净值比

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"prt_centralbankbilltonav",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPrtMtnToNav(security:list,*args,**kwargs):
    """
	获取中期票据市值占基金资产净值比

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"prt_mtntonav",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPrtOtherBondToNav(security:list,*args,**kwargs):
    """
	获取其他债券市值占基金资产净值比

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"prt_otherbondtonav",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPrtCentralBankBillToNavGrowth(security:list,*args,**kwargs):
    """
	获取央行票据市值占基金资产净值比例增长

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"prt_centralbankbilltonavgrowth",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPrtStockValueTopIndustryToNav2(security:list,*args,**kwargs):
    """
	获取重仓行业市值占基金资产净值比

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"prt_stockvalue_topindustrytonav2",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPrtHeavilyHeldBondToNav(security:list,*args,**kwargs):
    """
	获取重仓债券市值占基金资产净值比

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"prt_heavilyheldbondtonav",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPrtHeavilyHeldFundToNav(security:list,*args,**kwargs):
    """
	获取重仓基金市值占基金资产净值比

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"prt_heavilyheldfundtonav",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPrtCpToNav(security:list,*args,**kwargs):
    """
	获取短期融资券市值占基金资产净值比

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"prt_cptonav",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPrtGicSIndustryValueToNav(security:list,*args,**kwargs):
    """
	获取分行业投资市值占基金资产净值比例(Wind全球行业)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"prt_gicsindustryvaluetonav",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPrtIndustryValueToNavWind(security:list,*args,**kwargs):
    """
	获取分行业投资市值占基金资产净值比(Wind)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"prt_industryvaluetonav_wind",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPrtIndustryValueToNavCitiC(security:list,*args,**kwargs):
    """
	获取分行业投资市值占基金资产净值比(中信)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"prt_industryvaluetonav_citic",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPrtIndustryValueToNavSw(security:list,*args,**kwargs):
    """
	获取分行业投资市值占基金资产净值比(申万)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"prt_industryvaluetonav_sw",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getQAnalNetAsset(security:list,*args,**kwargs):
    """
	获取单季度.报告期期末基金资产净值

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"qanal_netasset",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPrtStocktonAvPassiveInvest(security:list,*args,**kwargs):
    """
	获取指数投资股票市值占基金资产净值比

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"prt_stocktonav_passiveinvest",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPrtStocktonAvActiveInvest(security:list,*args,**kwargs):
    """
	获取积极投资股票市值占基金资产净值比

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"prt_stocktonav_activeinvest",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPrtPFbToNav(security:list,*args,**kwargs):
    """
	获取政策性金融债市值占基金资产净值比

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"prt_pfbtonav",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPrtCorporateBondToNav(security:list,*args,**kwargs):
    """
	获取企业发行债券市值占基金资产净值比

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"prt_corporatebondtonav",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPrtAbsToNav(security:list,*args,**kwargs):
    """
	获取资产支持证券市值占基金资产净值比

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"prt_abstonav",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPrtMMitoNav(security:list,*args,**kwargs):
    """
	获取货币市场工具市值占基金资产净值比

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"prt_mmitonav",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPrtCorporateBondToNavGrowth(security:list,*args,**kwargs):
    """
	获取企业发行债券市值占基金资产净值比例增长

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"prt_corporatebondtonavgrowth",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPrtTopGicSIndustryValueToNav(security:list,*args,**kwargs):
    """
	获取重仓行业投资市值占基金资产净值比例(Wind全球行业)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"prt_topgicsindustryvaluetonav",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPrtTopIndustryValueToNavWind(security:list,*args,**kwargs):
    """
	获取重仓行业投资市值占基金资产净值比(Wind)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"prt_topindustryvaluetonav_wind",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPrtTopIndustryValueToNavCitiC(security:list,*args,**kwargs):
    """
	获取重仓行业投资市值占基金资产净值比(中信)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"prt_topindustryvaluetonav_citic",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPrtTopIndustryValueToNavSw(security:list,*args,**kwargs):
    """
	获取重仓行业投资市值占基金资产净值比(申万)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"prt_topindustryvaluetonav_sw",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPrtQdIiCountryRegionInvestmentToNav(security:list,*args,**kwargs):
    """
	获取国家/地区投资市值占基金资产净值比例(QDII)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"prt_qdii_countryregioninvestmenttonav",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPrtHeavilyHeldAbsToNav(security:list,*args,**kwargs):
    """
	获取重仓资产支持证券市值占基金资产净值比

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"prt_heavilyheldabstonav",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPrtSecLendingValueToNav(security:list,*args,**kwargs):
    """
	获取转融通证券出借业务市值占基金资产净值比

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"prt_seclendingvaluetonav",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPrtTopNStocktonAv(security:list,*args,**kwargs):
    """
	获取前N名重仓股票市值合计占基金资产净值比

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"prt_topnstocktonav",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPrtTop5ToNav(security:list,*args,**kwargs):
    """
	获取前N名重仓债券市值合计占基金资产净值比

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"prt_top5tonav",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPrtTopNFundToNav(security:list,*args,**kwargs):
    """
	获取前N名重仓基金市值合计占基金资产净值比

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"prt_topnfundtonav",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPrtAvgNetAsset(security:list,*args,**kwargs):
    """
	获取报告期基金日均资产净值

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"prt_avgnetasset",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPrtFundNetAssetTotal(security:list,*args,**kwargs):
    """
	获取资产净值(合计)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"prt_fundnetasset_total",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPrtMergedNavOrNot(security:list,*args,**kwargs):
    """
	获取资产净值是否为合并数据(最新)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"prt_mergednavornot",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPrtMergedNavOrNot1(security:list,*args,**kwargs):
    """
	获取资产净值是否为合并数据(报告期)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"prt_mergednavornot1",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundAvgFundScale(security:list,*args,**kwargs):
    """
	获取同类基金平均规模

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_avgfundscale",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundMarketOutlook(security:list,*args,**kwargs):
    """
	获取市场展望

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_marketoutlook",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundMarketAnalysis(security:list,*args,**kwargs):
    """
	获取市场分析

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_marketanalysis",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPrtStockValue(security:list,*args,**kwargs):
    """
	获取股票投资市值

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"prt_stockvalue",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPrtStockValueIndustryTostock2(security:list,*args,**kwargs):
    """
	获取分行业市值占股票投资市值比

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"prt_stockvalue_industrytostock2",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPrtHeavilyHeldStockTostock(security:list,*args,**kwargs):
    """
	获取重仓股市值占股票投资市值比

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"prt_heavilyheldstocktostock",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPrtStockValueTopIndustryTostock2(security:list,*args,**kwargs):
    """
	获取重仓行业市值占股票投资市值比

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"prt_stockvalue_topindustrytostock2",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPrtTopNStockTostock(security:list,*args,**kwargs):
    """
	获取前N名重仓股票市值合计占股票投资市值比

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"prt_topnstocktostock",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPrtStockValuePassiveInvest(security:list,*args,**kwargs):
    """
	获取指数投资股票市值

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"prt_stockvalue_passiveinvest",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPrtStockValueActiveInvest(security:list,*args,**kwargs):
    """
	获取积极投资股票市值

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"prt_stockvalue_activeinvest",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPrtHkStockValue(security:list,*args,**kwargs):
    """
	获取港股投资市值

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"prt_hkstockvalue",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPrtBondValue(security:list,*args,**kwargs):
    """
	获取债券投资市值

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"prt_bondvalue",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPrtGovernmentBondToBond(security:list,*args,**kwargs):
    """
	获取国债市值占债券投资市值比

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"prt_governmentbondtobond",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPrtFinancialBondToBond(security:list,*args,**kwargs):
    """
	获取金融债市值占债券投资市值比

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"prt_financialbondtobond",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPrtCorporateBondsToBond(security:list,*args,**kwargs):
    """
	获取企业债市值占债券投资市值比

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"prt_corporatebondstobond",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPrtConvertibleBondToBond(security:list,*args,**kwargs):
    """
	获取可转债市值占债券投资市值比

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"prt_convertiblebondtobond",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPrtCentralBankBillToBond(security:list,*args,**kwargs):
    """
	获取央行票据市值占债券投资市值比

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"prt_centralbankbilltobond",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPrtPFbToBond(security:list,*args,**kwargs):
    """
	获取政策性金融债占债券投资市值比

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"prt_pfbtobond",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPrtNcdToBond(security:list,*args,**kwargs):
    """
	获取同业存单市值占债券投资市值比

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"prt_NCDtobond",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPrtHeavilyHeldBondToBond(security:list,*args,**kwargs):
    """
	获取重仓债券市值占债券投资市值比

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"prt_heavilyheldbondtobond",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPrtCorporateBondToBond(security:list,*args,**kwargs):
    """
	获取企业发行债券市值占债券投资市值比

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"prt_corporatebondtobond",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPrtTop5ToBond(security:list,*args,**kwargs):
    """
	获取前N名重仓债券市值合计占债券投资市值比

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"prt_top5tobond",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPrtFundValue(security:list,*args,**kwargs):
    """
	获取基金投资市值

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"prt_fundvalue",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPrtHeavilyHeldFundToFund(security:list,*args,**kwargs):
    """
	获取重仓基金市值占基金投资市值比

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"prt_heavilyheldfundtofund",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPrtTopFundToFund(security:list,*args,**kwargs):
    """
	获取前N名重仓基金市值合计占基金投资市值比

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"prt_topfundtofund",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPrtSiFutures(security:list,*args,**kwargs):
    """
	获取股指期货投资市值

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"prt_SIfutures",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPrtGbFutures(security:list,*args,**kwargs):
    """
	获取国债期货投资市值

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"prt_gbfutures",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPrtWarrantValue(security:list,*args,**kwargs):
    """
	获取权证投资市值

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"prt_warrantvalue",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPrtSecLendingValue(security:list,*args,**kwargs):
    """
	获取转融通证券出借业务市值

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"prt_seclendingvalue",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWgsDAssetsOTh(security:list,*args,**kwargs):
    """
	获取其他资产_GSD

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"wgsd_assets_oth",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPrtOther(security:list,*args,**kwargs):
    """
	获取其他资产

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"prt_other",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getStmBs18(security:list,*args,**kwargs):
    """
	获取其他资产_FUND

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"stm_bs_18",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPrtOtherValueGrowth(security:list,*args,**kwargs):
    """
	获取其他资产市值增长率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"prt_othervaluegrowth",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPrtStockValueGrowth(security:list,*args,**kwargs):
    """
	获取股票市值增长率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"prt_stockvaluegrowth",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPrtBondValueGrowth(security:list,*args,**kwargs):
    """
	获取债券市值增长率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"prt_bondvaluegrowth",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPrtCorporateBondGrowth(security:list,*args,**kwargs):
    """
	获取企业发行债券市值增长率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"prt_corporatebondgrowth",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPrtFundValueGrowth(security:list,*args,**kwargs):
    """
	获取基金市值增长率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"prt_fundvaluegrowth",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPrtWarrantValueGrowth(security:list,*args,**kwargs):
    """
	获取权证市值增长率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"prt_warrantvaluegrowth",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPrtFoundLeverage(security:list,*args,**kwargs):
    """
	获取基金杠杆率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"prt_foundleverage",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPrtGovernmentBond(security:list,*args,**kwargs):
    """
	获取国债市值

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"prt_governmentbond",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPrtGovernmentBondGrowth(security:list,*args,**kwargs):
    """
	获取国债市值增长率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"prt_governmentbondgrowth",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPrtCds(security:list,*args,**kwargs):
    """
	获取同业存单市值

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"prt_CDs",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPrtCentralBankBill(security:list,*args,**kwargs):
    """
	获取央行票据市值

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"prt_centralbankbill",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPrtCentralBankBillGrowth(security:list,*args,**kwargs):
    """
	获取央行票据市值增长率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"prt_centralbankbillgrowth",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPrtFinancialBond(security:list,*args,**kwargs):
    """
	获取金融债市值

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"prt_financialbond",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPrtFinancialBondGrowth(security:list,*args,**kwargs):
    """
	获取金融债市值增长率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"prt_financialbondgrowth",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPrtPFbValue(security:list,*args,**kwargs):
    """
	获取政策性金融债市值

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"prt_pfbvalue",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPrtCorporateBond(security:list,*args,**kwargs):
    """
	获取企业发行债券市值

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"prt_corporatebond",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPrtCorporateBonds(security:list,*args,**kwargs):
    """
	获取企业债市值

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"prt_corporatebonds",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPrtCorporateBondsGrowth(security:list,*args,**kwargs):
    """
	获取企业债市值增长率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"prt_corporatebondsgrowth",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPrtCpValue(security:list,*args,**kwargs):
    """
	获取短期融资券市值

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"prt_cpvalue",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPrtMtnValue(security:list,*args,**kwargs):
    """
	获取中期票据市值

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"prt_mtnvalue",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPrtConvertibleBond(security:list,*args,**kwargs):
    """
	获取可转债市值

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"prt_convertiblebond",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPrtConvertibleBondGrowth(security:list,*args,**kwargs):
    """
	获取可转债市值增长率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"prt_convertiblebondgrowth",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPrtAbsValue(security:list,*args,**kwargs):
    """
	获取资产支持证券市值

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"prt_absvalue",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPrtMmIValue(security:list,*args,**kwargs):
    """
	获取货币市场工具市值

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"prt_mmivalue",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPrtOtherBond(security:list,*args,**kwargs):
    """
	获取其他债券市值

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"prt_otherbond",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPrtStockValueIndustry2(security:list,*args,**kwargs):
    """
	获取分行业投资市值

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"prt_stockvalue_industry2",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPrtGicSIndustryValue(security:list,*args,**kwargs):
    """
	获取分行业投资市值(Wind全球行业)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"prt_gicsindustryvalue",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPrtIndustryValueWind(security:list,*args,**kwargs):
    """
	获取分行业投资市值(Wind)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"prt_industryvalue_wind",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPrtIndustryValueCitiC(security:list,*args,**kwargs):
    """
	获取分行业投资市值(中信)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"prt_industryvalue_citic",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPrtIndustryValueSw(security:list,*args,**kwargs):
    """
	获取分行业投资市值(申万)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"prt_industryvalue_sw",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPrtStockValueIndustryValueGrowth2(security:list,*args,**kwargs):
    """
	获取分行业市值增长率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"prt_stockvalue_industryvaluegrowth2",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPrtIndustryValueGrowthWind(security:list,*args,**kwargs):
    """
	获取分行业市值增长率(Wind)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"prt_industryvaluegrowth_wind",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPrtIndustryValueGrowthCitiC(security:list,*args,**kwargs):
    """
	获取分行业市值增长率(中信)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"prt_industryvaluegrowth_citic",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPrtIndustryValueGrowthSw(security:list,*args,**kwargs):
    """
	获取分行业市值增长率(申万)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"prt_industryvaluegrowth_sw",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPrtStockValueTopIndustryName2(security:list,*args,**kwargs):
    """
	获取重仓行业名称

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"prt_stockvalue_topindustryname2",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPrtTopGicSIndustryName(security:list,*args,**kwargs):
    """
	获取重仓行业名称(Wind全球行业)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"prt_topgicsindustryname",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPrtTopIndustryNameWind(security:list,*args,**kwargs):
    """
	获取重仓行业名称(Wind)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"prt_topindustryname_wind",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPrtTopIndustryNameCitiC(security:list,*args,**kwargs):
    """
	获取重仓行业名称(中信)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"prt_topindustryname_citic",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPrtTopIndustryNameSw(security:list,*args,**kwargs):
    """
	获取重仓行业名称(申万)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"prt_topindustryname_sw",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPrtStockValueTopIndustrySymbol2(security:list,*args,**kwargs):
    """
	获取重仓行业代码

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"prt_stockvalue_topindustrysymbol2",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPrtStockValueTopIndustryValue2(security:list,*args,**kwargs):
    """
	获取重仓行业市值

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"prt_stockvalue_topindustryvalue2",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPrtStockHolding(security:list,*args,**kwargs):
    """
	获取报告期末持有股票个数(中报、年报)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"prt_stockholding",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPrtShareNumStKhlDGStyle(security:list,*args,**kwargs):
    """
	获取报告期不同持仓风格股票只数

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"prt_sharenum_stkhldgstyle",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPrtTopStockName(security:list,*args,**kwargs):
    """
	获取重仓股股票名称

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"prt_topstockname",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPrtTopStockCode(security:list,*args,**kwargs):
    """
	获取重仓股股票代码

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"prt_topstockcode",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPrtTopStockDate(security:list,*args,**kwargs):
    """
	获取最早重仓时间

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"prt_topstockdate",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPrtTopStockQuantity(security:list,*args,**kwargs):
    """
	获取重仓股持股数量

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"prt_topstockquantity",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPrtTopStockValue(security:list,*args,**kwargs):
    """
	获取重仓股持股市值

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"prt_topstockvalue",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPrtTopStockHoldingChanging(security:list,*args,**kwargs):
    """
	获取重仓股持仓变动

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"prt_topstockholdingchanging",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPrtTopProportionToFloating(security:list,*args,**kwargs):
    """
	获取重仓股持仓占流通股比例

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"prt_topproportiontofloating",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPrtFundNoOfStocks(security:list,*args,**kwargs):
    """
	获取重仓股票持有基金数

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"prt_fundnoofstocks",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPrtTopStockHeldNo(security:list,*args,**kwargs):
    """
	获取重仓股报告期重仓次数

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"prt_topstockheldno",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPrtBuyStockCost(security:list,*args,**kwargs):
    """
	获取报告期买入股票总成本

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"prt_buystockcost",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPrtSellStockIncome(security:list,*args,**kwargs):
    """
	获取报告期卖出股票总收入

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"prt_sellstockincome",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPrtStockVolumeByBroker(security:list,*args,**kwargs):
    """
	获取股票成交金额(分券商明细)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"prt_stockvolumebybroker",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPrtTopBondName(security:list,*args,**kwargs):
    """
	获取重仓债券名称

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"prt_topbondname",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPrtTopBondSymbol(security:list,*args,**kwargs):
    """
	获取重仓债券代码

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"prt_topbondsymbol",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPrtTopBondQuantity(security:list,*args,**kwargs):
    """
	获取重仓债券持仓数量

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"prt_topbondquantity",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPrtTopBondValue(security:list,*args,**kwargs):
    """
	获取重仓债券持仓市值

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"prt_topbondvalue",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPrtTopBondHoldingChanging(security:list,*args,**kwargs):
    """
	获取重仓债券持仓变动

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"prt_topbondholdingchanging",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPrtFundNoOfBonds(security:list,*args,**kwargs):
    """
	获取重仓债券持有基金数

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"prt_fundnoofbonds",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPrtTopAbsName(security:list,*args,**kwargs):
    """
	获取重仓资产支持证券名称

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"prt_topabsname",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPrtTopAbsSymbol(security:list,*args,**kwargs):
    """
	获取重仓资产支持证券代码

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"prt_topabssymbol",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPrtTopAbsQuantity(security:list,*args,**kwargs):
    """
	获取重仓资产支持证券持仓数量

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"prt_topabsquantity",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPrtTopAbsValue(security:list,*args,**kwargs):
    """
	获取重仓资产支持证券持有市值

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"prt_topabsvalue",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPrtTopAbsHoldingChanging(security:list,*args,**kwargs):
    """
	获取重仓资产支持证券持仓变动

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"prt_topabsholdingchanging",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPrtTopFundName(security:list,*args,**kwargs):
    """
	获取重仓基金名称

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"prt_topfundname",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPrtTopFundCode(security:list,*args,**kwargs):
    """
	获取重仓基金代码

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"prt_topfundcode",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPrtTopFundQuantity(security:list,*args,**kwargs):
    """
	获取重仓基金持仓数量

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"prt_topfundquantity",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPrtTopFundValue(security:list,*args,**kwargs):
    """
	获取重仓基金持有市值

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"prt_topfundvalue",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPrtTopFundHoldingChanging(security:list,*args,**kwargs):
    """
	获取重仓基金持仓变动

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"prt_topfundholdingchanging",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPrtFundNoOfFunds(security:list,*args,**kwargs):
    """
	获取重仓基金持有基金数

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"prt_fundnooffunds",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getMmFrequencyOfDeviation(security:list,*args,**kwargs):
    """
	获取报告期内偏离度的绝对值在0.25%(含)-0.5%间的次数

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"mmfrequencyofdeviation",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getMmMaxDeviation(security:list,*args,**kwargs):
    """
	获取报告期内偏离度的最高值

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"mmmaxdeviation",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getMmmInDeviation(security:list,*args,**kwargs):
    """
	获取报告期内偏离度的最低值

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"mmmindeviation",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getMmAvgDeviation(security:list,*args,**kwargs):
    """
	获取报告期内每个工作日偏离度的绝对值的简单平均值

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"mmavgdeviation",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundReItsEValue(security:list,*args,**kwargs):
    """
	获取资产估值

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_reitsevalue",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundReItsDIsTrAmountF(security:list,*args,**kwargs):
    """
	获取可供分配金额(预测)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_reitsdistramountf",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundReItsDprF(security:list,*args,**kwargs):
    """
	获取派息率(预测)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_reitsdprf",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getEmployeeAdmin(security:list,*args,**kwargs):
    """
	获取综合管理人员人数

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"employee_admin",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getEmployeeAdminPct(security:list,*args,**kwargs):
    """
	获取综合管理人员人数占比

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"employee_admin_pct",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getStmNoteInSur9(security:list,*args,**kwargs):
    """
	获取综合成本率(产险)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"stmnote_insur_9",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getQStmNoteInSur212507(security:list,*args,**kwargs):
    """
	获取综合偿付能力溢额

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"qstmnote_insur_212507",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getQStmNoteInSur212508(security:list,*args,**kwargs):
    """
	获取综合偿付能力充足率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"qstmnote_insur_212508",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getQStmNoteInSur212534(security:list,*args,**kwargs):
    """
	获取综合流动比率:3个月内

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"qstmnote_insur_212534",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getQStmNoteInSur212535(security:list,*args,**kwargs):
    """
	获取综合流动比率:1年内

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"qstmnote_insur_212535",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getQStmNoteInSur212536(security:list,*args,**kwargs):
    """
	获取综合流动比率:1年以上

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"qstmnote_insur_212536",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getQStmNoteInSur212537(security:list,*args,**kwargs):
    """
	获取综合流动比率:1-3年内

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"qstmnote_insur_212537",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getQStmNoteInSur212538(security:list,*args,**kwargs):
    """
	获取综合流动比率:3-5年内

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"qstmnote_insur_212538",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getQStmNoteInSur212539(security:list,*args,**kwargs):
    """
	获取综合流动比率:5年以上

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"qstmnote_insur_212539",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWgsDComPrInc(security:list,*args,**kwargs):
    """
	获取综合收益_GSD

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"wgsd_compr_inc",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getStm07IsReItsGeneralProfit(security:list,*args,**kwargs):
    """
	获取综合收益总额

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"stm07_is_reits_generalprofit",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getRatingMarketAvg(security:list,*args,**kwargs):
    """
	获取市场综合3年评级

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"rating_marketavg",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWgsDComEqForExCh(security:list,*args,**kwargs):
    """
	获取其他综合性收益_GSD

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"wgsd_com_eq_for_exch",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getOtherCompRehIncBs(security:list,*args,**kwargs):
    """
	获取其他综合收益_BS

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"other_compreh_inc_bs",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getOtherCompRehInc(security:list,*args,**kwargs):
    """
	获取其他综合收益

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"other_compreh_inc",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getEsGEwa01004(security:list,*args,**kwargs):
    """
	获取废水综合利用率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"esg_ewa01004",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getRatingWindAvg(security:list,*args,**kwargs):
    """
	获取Wind综合评级

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"rating_windavg",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWgsDQfaComPrInc(security:list,*args,**kwargs):
    """
	获取单季度.综合收益_GSD

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"wgsd_qfa_compr_inc",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getQfaToTCompRehInc(security:list,*args,**kwargs):
    """
	获取单季度.综合收益总额

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"qfa_tot_compreh_inc",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getQStmNoteInSur212529(security:list,*args,**kwargs):
    """
	获取最近一次风险综合评级类别

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"qstmnote_insur_212529",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWgsDCompRehIncParentComp(security:list,*args,**kwargs):
    """
	获取归属普通股东综合收益_GSD

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"wgsd_compreh_inc_parent_comp",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getQfaOtherCompRehInc(security:list,*args,**kwargs):
    """
	获取单季度.其他综合收益

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"qfa_other_compreh_inc",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWgsDTenantReImExp(security:list,*args,**kwargs):
    """
	获取租户认缴物业维护综合费_GSD

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"wgsd_tenant_reim_exp",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getToTCompRehIncMinSHrhLDr(security:list,*args,**kwargs):
    """
	获取归属于少数股东的综合收益总额

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"tot_compreh_inc_min_shrhldr",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getEsGScoreWind(security:list,*args,**kwargs):
    """
	获取Wind ESG综合得分

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"esg_score_wind",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getRatingShanghaiOverall3Y(security:list,*args,**kwargs):
    """
	获取上海证券3年评级(综合评级)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"rating_shanghaioverall3y",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getRatingShanghaiOverall5Y(security:list,*args,**kwargs):
    """
	获取上海证券5年评级(综合评级)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"rating_shanghaioverall5y",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWgsDQfaCompRehIncParentComp(security:list,*args,**kwargs):
    """
	获取单季度.归属普通股东综合收益_GSD

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"wgsd_qfa_compreh_inc_parent_comp",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getToTCompRehIncParentComp(security:list,*args,**kwargs):
    """
	获取归属于母公司普通股东综合收益总额

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"tot_compreh_inc_parent_comp",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWgsDQfaTenantReImExp(security:list,*args,**kwargs):
    """
	获取单季度.租户认缴物业维护综合费_GSD

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"wgsd_qfa_tenant_reim_exp",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getQfaToTCompRehIncMinSHrhLDr(security:list,*args,**kwargs):
    """
	获取单季度.归属于少数股东的综合收益总额

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"qfa_tot_compreh_inc_min_shrhldr",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getQfaToTCompRehIncParentComp(security:list,*args,**kwargs):
    """
	获取单季度.归属于母公司普通股东综合收益总额

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"qfa_tot_compreh_inc_parent_comp",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFinAssetsChgCompRehInc(security:list,*args,**kwargs):
    """
	获取以公允价值计量且其变动计入其他综合收益的金融资产

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fin_assets_chg_compreh_inc",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getStmNoteSocialSecurityAdd(security:list,*args,**kwargs):
    """
	获取社会保险费:本期增加

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"stmnote_socialsecurity_add",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getStmNoteSocialSecuritySb(security:list,*args,**kwargs):
    """
	获取社会保险费:期初余额

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"stmnote_socialsecurity_sb",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getStmNoteSocialSecurityEb(security:list,*args,**kwargs):
    """
	获取社会保险费:期末余额

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"stmnote_socialsecurity_eb",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getStmNoteSocialSecurityDe(security:list,*args,**kwargs):
    """
	获取社会保险费:本期减少

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"stmnote_socialsecurity_de",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getEsGRatingCasVi(security:list,*args,**kwargs):
    """
	获取社会价值投资联盟ESG评级

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"esg_rating_casvi",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getRegisterNumber(security:list,*args,**kwargs):
    """
	获取统一社会信用代码

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"registernumber",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getEsGMdc01002(security:list,*args,**kwargs):
    """
	获取公司是否有独立的公司社会责任报告

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"esg_mdc01002",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getRatingYinHe1Y(security:list,*args,**kwargs):
    """
	获取(停止)银河1年评级

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"rating_yinhe1y",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getRatingYinHe2Y(security:list,*args,**kwargs):
    """
	获取(停止)银河2年评级

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"rating_yinhe2y",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getRatingZhaoShang3Y(security:list,*args,**kwargs):
    """
	获取(停止)招商3年评级

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"rating_zhaoshang3y",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getRatingHaiTong3Y(security:list,*args,**kwargs):
    """
	获取(停止)海通3年评级

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"rating_haitong3y",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundInvestStyle(security:list,*args,**kwargs):
    """
	获取(停止)投资风格

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_investstyle",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIndustryGx(security:list,*args,**kwargs):
    """
	获取(停止)所属国信行业名称

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"industry_gx",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getBondScore(security:list,*args,**kwargs):
    """
	获取(停止)债券评分

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"bondscore",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIssuersCore(security:list,*args,**kwargs):
    """
	获取(停止)发行人评分

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"issuerscore",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getAbstract(security:list,*args,**kwargs):
    """
	获取(停止)公司一句话介绍

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"abstract",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundManagerTotalGeometricReturn(security:list,*args,**kwargs):
    """
	获取(废弃)任职基金几何总回报

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_manager_totalgeometricreturn",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFellowNetPrice(security:list,*args,**kwargs):
    """
	获取(废弃)净值价格

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fellow_netprice",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getDefaultSource(security:list,*args,**kwargs):
    """
	获取(废弃)估值来源

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"defaultsource",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getTheOPricePer(security:list,*args,**kwargs):
    """
	获取(废弃)区间理论价

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"theo_price_per",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getStmIs83(security:list,*args,**kwargs):
    """
	获取(废弃)基金投资收益

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"stm_is_83",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getXQACcmFocus(security:list,*args,**kwargs):
    """
	获取(废弃)累计关注人数_雪球

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"xq_accmfocus",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getXQACcmComments(security:list,*args,**kwargs):
    """
	获取(废弃)累计讨论次数_雪球

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"xq_accmcomments",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getXQACcmShares(security:list,*args,**kwargs):
    """
	获取(废弃)累计交易分享数_雪球

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"xq_accmshares",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getXQFocusAdded(security:list,*args,**kwargs):
    """
	获取(废弃)一周新增关注_雪球

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"xq_focusadded",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getXQCommentsAdded(security:list,*args,**kwargs):
    """
	获取(废弃)一周新增讨论数_雪球

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"xq_commentsadded",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getXQSharesAdded(security:list,*args,**kwargs):
    """
	获取(废弃)一周新增交易分享数_雪球

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"xq_sharesadded",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getXQWowFocus(security:list,*args,**kwargs):
    """
	获取(废弃)一周关注增长率_雪球

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"xq_WOW_focus",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getXQWowComments(security:list,*args,**kwargs):
    """
	获取(废弃)一周讨论增长率_雪球

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"xq_WOW_comments",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getXQWowShares(security:list,*args,**kwargs):
    """
	获取(废弃)一周交易分享增长率_雪球

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"xq_WOW_shares",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getShareCategory(security:list,*args,**kwargs):
    """
	获取(废弃)大股东类型

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"sharecategory",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIndustryCsrC12(security:list,*args,**kwargs):
    """
	获取(废弃)所属证监会行业名称

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"industry_CSRC12",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getDivPayOutRatio(security:list,*args,**kwargs):
    """
	获取年度现金分红比例(沪深)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"div_payoutratio",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getShareNonTradable(security:list,*args,**kwargs):
    """
	获取非流通股(沪深)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"share_nontradable",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getYieldCsi(security:list,*args,**kwargs):
    """
	获取估价收益率(中证指数)(旧)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"yield_csi",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getNetCsi(security:list,*args,**kwargs):
    """
	获取估价净价(中证指数)(旧)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"net_csi",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getDirtyCsi(security:list,*args,**kwargs):
    """
	获取估价全价(中证指数)(旧)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"dirty_csi",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getModiDuraCsi(security:list,*args,**kwargs):
    """
	获取估价修正久期(中证指数)(旧)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"modidura_csi",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getCNvXTyCsi(security:list,*args,**kwargs):
    """
	获取估价凸性(中证指数)(旧)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"cnvxty_csi",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIpoNetCollection(security:list,*args,**kwargs):
    """
	获取首发募集资金净额(旧)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"ipo_netcollection",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIpoPrice(security:list,*args,**kwargs):
    """
	获取首发价格(旧)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"ipo_price",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIpoExpectedCollection(security:list,*args,**kwargs):
    """
	获取首发预计募集资金(旧)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"ipo_expectedcollection",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIpoCollectionOldShares(security:list,*args,**kwargs):
    """
	获取股东售股金额(旧)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"ipo_collection_oldshares",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIpoUsFees(security:list,*args,**kwargs):
    """
	获取首发承销保荐费用(旧)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"ipo_usfees",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundFeeDiscountOrNot(security:list,*args,**kwargs):
    """
	获取(废弃)是否费率优惠

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_feediscountornot",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundMinPurchaseDiscounts(security:list,*args,**kwargs):
    """
	获取(废弃)最低申购折扣费率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_minpurchasediscounts",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundMinaIpDiscounts(security:list,*args,**kwargs):
    """
	获取(废弃)最低定投折扣率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_minaipdiscounts",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getEsGSem01003(security:list,*args,**kwargs):
    """
	获取(废弃)兼职人员比例

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"esg_sem01003",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getValPep(security:list,*args,**kwargs):
    """
	获取(废弃)市盈率百分位

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"val_pep",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getNavWinLossRatio(security:list,*args,**kwargs):
    """
	获取(废弃)基金盈利概率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"NAV_winlossratio",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundMaturityDate(security:list,*args,**kwargs):
    """
	获取(废弃)基金到期日

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_maturitydate",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFoundDate(security:list,*args,**kwargs):
    """
	获取(废弃)成立日期

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"founddate",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIpoLeadUndRN(security:list,*args,**kwargs):
    """
	获取(废弃)主办券商(持续督导)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"ipo_leadundr_n",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFrMindPDirector(security:list,*args,**kwargs):
    """
	获取(废弃)公司独立董事(历任)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"frmindpdirector",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getSecName(security:list,*args,**kwargs):
    """
	获取证券简称

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"sec_name",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getSecName1(security:list,*args,**kwargs):
    """
	获取证券简称(支持历史)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"sec_name1",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getSecEnglishname(security:list,*args,**kwargs):
    """
	获取证券英文简称

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"sec_englishname",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIpoDate(security:list,*args,**kwargs):
    """
	获取上市日期

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"ipo_date",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getBackdoorDate(security:list,*args,**kwargs):
    """
	获取借壳上市日期

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"backdoordate",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundEtFListedDate(security:list,*args,**kwargs):
    """
	获取ETF上市日期

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_etflisteddate",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundReItsListedDate(security:list,*args,**kwargs):
    """
	获取REITs上市日期

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund__reitslisteddate",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIpoJurisDate(security:list,*args,**kwargs):
    """
	获取网下配售部分上市日期

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"ipo_jurisdate",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIpoInStIsDate(security:list,*args,**kwargs):
    """
	获取向战略投资者配售部分上市日期

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"ipo_instisdate",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFellowInStListDate(security:list,*args,**kwargs):
    """
	获取向机构投资者增发部分上市日期

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fellow_instlistdate",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getExchangeCn(security:list,*args,**kwargs):
    """
	获取交易所中文名称

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"exchange_cn",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getExChEng(security:list,*args,**kwargs):
    """
	获取交易所英文简称

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"exch_eng",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getMkt(security:list,*args,**kwargs):
    """
	获取上市板

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"mkt",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getSecStatus(security:list,*args,**kwargs):
    """
	获取证券存续状态

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"sec_status",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getRiskAdmonitionDate(security:list,*args,**kwargs):
    """
	获取戴帽摘帽时间

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"riskadmonition_date",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getDeListDate(security:list,*args,**kwargs):
    """
	获取摘牌日期

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"delist_date",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIssueCurrencyCode(security:list,*args,**kwargs):
    """
	获取发行币种

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"issuecurrencycode",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getCurR(security:list,*args,**kwargs):
    """
	获取交易币种

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"curr",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getValBsHrMarketValue4(security:list,*args,**kwargs):
    """
	获取B股市值(含限售股,交易币种)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"val_bshrmarketvalue4",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getValBsHrMarketValue2(security:list,*args,**kwargs):
    """
	获取B股市值(不含限售股,交易币种)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"val_bshrmarketvalue2",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundSettlementMode(security:list,*args,**kwargs):
    """
	获取交易结算模式

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_settlementmode",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getParValue(security:list,*args,**kwargs):
    """
	获取每股面值

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"parvalue",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIpoPar(security:list,*args,**kwargs):
    """
	获取发行时每股面值

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"ipo_par",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getLotSize(security:list,*args,**kwargs):
    """
	获取每手股数

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"lotsize",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getTunIt(security:list,*args,**kwargs):
    """
	获取交易单位

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"tunit",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getCountry(security:list,*args,**kwargs):
    """
	获取所属国家或地区代码

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"country",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getBaseDate(security:list,*args,**kwargs):
    """
	获取基期

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"basedate",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getBaseValue(security:list,*args,**kwargs):
    """
	获取基点

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"basevalue",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getCalcPvbP(security:list,*args,**kwargs):
    """
	获取基点价值

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"calc_pvbp",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getVoBpCnBd(security:list,*args,**kwargs):
    """
	获取估价基点价值(中债)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"vobp_cnbd",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getVoBpShc(security:list,*args,**kwargs):
    """
	获取估价基点价值(上清所)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"vobp_shc",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getAnalBasePointValue(security:list,*args,**kwargs):
    """
	获取平均基点价值

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"anal_basepointvalue",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getBaseValueIfExe(security:list,*args,**kwargs):
    """
	获取行权基点价值

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"basevalue_ifexe",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getCalcFloatAddBp(security:list,*args,**kwargs):
    """
	获取计算浮息债隐含加息基点

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"calc_floataddbp",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getNumberOfConstituents(security:list,*args,**kwargs):
    """
	获取成份个数

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"numberofconstituents",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getNumberOfConstituents2(security:list,*args,**kwargs):
    """
	获取成份个数(支持历史)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"numberofconstituents2",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFirstDayOfConstituents(security:list,*args,**kwargs):
    """
	获取最早成份日期

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"firstdayofconstituents",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getMethodology(security:list,*args,**kwargs):
    """
	获取加权方式

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"methodology",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getRepoBriefing(security:list,*args,**kwargs):
    """
	获取证券简介

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"repo_briefing",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getLaunchDate(security:list,*args,**kwargs):
    """
	获取发布日期

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"launchdate",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPreName(security:list,*args,**kwargs):
    """
	获取证券曾用名

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"prename",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getExChCity(security:list,*args,**kwargs):
    """
	获取上市地点

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"exch_city",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getTrackedByFunds(security:list,*args,**kwargs):
    """
	获取跟踪标的基金代码

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"trackedbyfunds",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getSuperiorCode(security:list,*args,**kwargs):
    """
	获取上级行业指数代码

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"superiorcode",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getCodeChangeDate(security:list,*args,**kwargs):
    """
	获取证券代码变更日期

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"codechangedate",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getAnchorBond(security:list,*args,**kwargs):
    """
	获取主证券代码

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"anchorbond",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getMajorIndexCode(security:list,*args,**kwargs):
    """
	获取主指数代码

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"majorindexcode",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getSubIndexCode(security:list,*args,**kwargs):
    """
	获取副指数代码

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"subindexcode",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getRelationCode(security:list,*args,**kwargs):
    """
	获取跨市场代码

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"relationCode",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getBcLc(security:list,*args,**kwargs):
    """
	获取公司债对应上市公司代码

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"bclc",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getTendRstCode(security:list,*args,**kwargs):
    """
	获取中债招标发行代码

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"tendrst_code",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getSzSeDistRibCode(security:list,*args,**kwargs):
    """
	获取深交所分销代码

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"szse_distribcode",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getCbName(security:list,*args,**kwargs):
    """
	获取同公司可转债简称

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"cbname",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getUsShareName(security:list,*args,**kwargs):
    """
	获取同公司美股简称

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"ussharename",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getStockClass(security:list,*args,**kwargs):
    """
	获取股票种类

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"stockclass",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIpoIssuingSystem(security:list,*args,**kwargs):
    """
	获取发行制度

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"ipo_issuingsystem",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getListsTd(security:list,*args,**kwargs):
    """
	获取所属上市标准

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"liststd",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFeaturedListsTd(security:list,*args,**kwargs):
    """
	获取北交所准入标准

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"featuredliststd",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getCompIndex2(security:list,*args,**kwargs):
    """
	获取是否属于重要指数成份

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"compindex2",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getConcept(security:list,*args,**kwargs):
    """
	获取所属概念板块

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"concept",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getScaleStyle(security:list,*args,**kwargs):
    """
	获取所属规模风格类型

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"scalestyle",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getShSc(security:list,*args,**kwargs):
    """
	获取是否沪港通买入标的

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"SHSC",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getShSc2(security:list,*args,**kwargs):
    """
	获取是否深港通买入标的

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"SHSC2",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getParallelCode(security:list,*args,**kwargs):
    """
	获取是否并行代码

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"parallelcode",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getSecType(security:list,*args,**kwargs):
    """
	获取证券类型

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"sec_type",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getBackdoor(security:list,*args,**kwargs):
    """
	获取是否借壳上市

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"backdoor",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getList(security:list,*args,**kwargs):
    """
	获取是否上市

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"list",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getListingOrNot(security:list,*args,**kwargs):
    """
	获取是否上市公司

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"listingornot",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getRiskWarning(security:list,*args,**kwargs):
    """
	获取是否属于风险警示板

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"riskwarning",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getOfficialStyle(security:list,*args,**kwargs):
    """
	获取指数风格

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"officialstyle",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getChain(security:list,*args,**kwargs):
    """
	获取所属产业链板块

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"chain",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getLargeCommodity(security:list,*args,**kwargs):
    """
	获取所属大宗商品概念板块

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"largecommodity",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getDepositAryBank(security:list,*args,**kwargs):
    """
	获取存托机构

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"depositarybank",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIpoLeadUndRN1(security:list,*args,**kwargs):
    """
	获取主办券商(持续督导)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"ipo_leadundr_n1",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIpoMarketMaker(security:list,*args,**kwargs):
    """
	获取做市商名称

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"ipo_marketMaker",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getMarketMakeDate(security:list,*args,**kwargs):
    """
	获取做市首日

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"marketmakedate",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getTransferType(security:list,*args,**kwargs):
    """
	获取交易类型

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"transfertype",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getNeEqMarketMakerNum(security:list,*args,**kwargs):
    """
	获取做市商家数

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"neeq_marketmakernum",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getNeEqPark(security:list,*args,**kwargs):
    """
	获取挂牌园区

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"neeq_park",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getNeEqListAnnDate(security:list,*args,**kwargs):
    """
	获取挂牌公告日

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"neeq_listanndate",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getNeEqMarketMakeAnnDate(security:list,*args,**kwargs):
    """
	获取转做市公告日

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"neeq_marketmakeanndate",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIndustryNeeQgIcs(security:list,*args,**kwargs):
    """
	获取所属挂牌公司投资型行业名称

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"industry_neeqgics",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIndustryNeeQgIcsCodeInv(security:list,*args,**kwargs):
    """
	获取所属挂牌公司投资型行业代码

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"industry_neeqgicscode_inv",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIndustryNeeQgIcsCode(security:list,*args,**kwargs):
    """
	获取所属挂牌公司投资型行业板块代码

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"industry_neeqgicscode",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIndustryNeEqConcept(security:list,*args,**kwargs):
    """
	获取所属新三板概念类板块

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"industry_neeqconcept",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getNeEqLevel(security:list,*args,**kwargs):
    """
	获取所属分层

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"neeq_level",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getNeEqStandard(security:list,*args,**kwargs):
    """
	获取所属创新层标准

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"neeq_standard",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIpoTutor(security:list,*args,**kwargs):
    """
	获取挂牌企业上市辅导券商

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"ipo_tutor",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIpoTutoringStartDate(security:list,*args,**kwargs):
    """
	获取挂牌企业上市辅导开始日期

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"ipo_tutoring_startdate",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIpoTutoringEnddate(security:list,*args,**kwargs):
    """
	获取挂牌企业上市辅导结束日期

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"ipo_tutoring_enddate",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getNeEqListingDate(security:list,*args,**kwargs):
    """
	获取挂牌日

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"neeq_listingdate",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getNeEqListDateInnovationLevel(security:list,*args,**kwargs):
    """
	获取创新层挂牌日

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"neeq_listdate_innovationlevel",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getNeEqSuspensionDay(security:list,*args,**kwargs):
    """
	获取挂牌公司转板北交所前停牌日

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"neeq_suspensionday",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getCompName(security:list,*args,**kwargs):
    """
	获取公司中文名称

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"comp_name",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getCompNameEng(security:list,*args,**kwargs):
    """
	获取公司英文名称

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"comp_name_eng",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getNature1(security:list,*args,**kwargs):
    """
	获取公司属性

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"nature1",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getNature(security:list,*args,**kwargs):
    """
	获取公司属性(旧)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"nature",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getShareholderNature(security:list,*args,**kwargs):
    """
	获取股东公司属性

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"shareholdernature",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getAgencyGuarantorNature(security:list,*args,**kwargs):
    """
	获取担保人公司属性

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"agency_guarantornature",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getInstitutionType(security:list,*args,**kwargs):
    """
	获取金融机构类型

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"institutiontype",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getCorpScale(security:list,*args,**kwargs):
    """
	获取企业规模

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"corpscale",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getBankType(security:list,*args,**kwargs):
    """
	获取上市公司(银行)类型

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"banktype",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFoundDate1(security:list,*args,**kwargs):
    """
	获取成立日期

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"founddate1",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundCorpEstablishmentDate(security:list,*args,**kwargs):
    """
	获取基金管理人成立日期

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_corpestablishmentdate",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getRegCapital(security:list,*args,**kwargs):
    """
	获取注册资本

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"regcapital",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getRegCapitalCur(security:list,*args,**kwargs):
    """
	获取注册资本币种

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"regcapitalcur",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundCorpRegisteredCapital(security:list,*args,**kwargs):
    """
	获取基金管理人注册资本

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_corpregisteredcapital",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getChairman(security:list,*args,**kwargs):
    """
	获取法定代表人

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"chairman",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getLegalRepresentative(security:list,*args,**kwargs):
    """
	获取法定代表人(支持历史)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"legalrepresentative",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFiscalDate(security:list,*args,**kwargs):
    """
	获取会计年结日

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fiscaldate",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getBusiness(security:list,*args,**kwargs):
    """
	获取经营范围

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"business",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getBriefing(security:list,*args,**kwargs):
    """
	获取公司简介

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"briefing",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getShareholderBriefing(security:list,*args,**kwargs):
    """
	获取股东公司简介

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"shareholderbriefing",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getAgencyGuarantorBriefing(security:list,*args,**kwargs):
    """
	获取担保人公司简介

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"agency_guarantorbriefing",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getMajorProductType(security:list,*args,**kwargs):
    """
	获取主营产品类型

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"majorproducttype",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getMajorProductName(security:list,*args,**kwargs):
    """
	获取主营产品名称

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"majorproductname",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getEmployee(security:list,*args,**kwargs):
    """
	获取员工总数

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"employee",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getEmployeePc(security:list,*args,**kwargs):
    """
	获取母公司员工人数

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"employee_pc",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getAdministrativeDivision(security:list,*args,**kwargs):
    """
	获取所属行政区划

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"administrativedivision",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getAdminCode(security:list,*args,**kwargs):
    """
	获取所属行政区划代码

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"admincode",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getCsrCJurisdiction(security:list,*args,**kwargs):
    """
	获取所属证监会辖区

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"csrcjurisdiction",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getProvince(security:list,*args,**kwargs):
    """
	获取省份

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"province",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getCity(security:list,*args,**kwargs):
    """
	获取城市

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"city",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundCorpCity(security:list,*args,**kwargs):
    """
	获取基金管理人注册城市

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_corpcity",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getAddress(security:list,*args,**kwargs):
    """
	获取注册地址

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"address",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundCorpAddress(security:list,*args,**kwargs):
    """
	获取基金管理人注册地址

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_corpaddress",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getOffice(security:list,*args,**kwargs):
    """
	获取办公地址

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"office",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundCorpOffice(security:list,*args,**kwargs):
    """
	获取基金管理人办公地址

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_corpoffice",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getZipCode(security:list,*args,**kwargs):
    """
	获取邮编

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"zipcode",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundCorpZip(security:list,*args,**kwargs):
    """
	获取基金管理人邮编

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_corpzip",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPhone(security:list,*args,**kwargs):
    """
	获取公司电话

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"phone",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFax(security:list,*args,**kwargs):
    """
	获取公司传真

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fax",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getEmail(security:list,*args,**kwargs):
    """
	获取公司电子邮件地址

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"email",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWebsite(security:list,*args,**kwargs):
    """
	获取公司网站

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"website",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getDIsCloser(security:list,*args,**kwargs):
    """
	获取信息披露人

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"discloser",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getMedia(security:list,*args,**kwargs):
    """
	获取信息指定披露媒体

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"media",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getOrganizationCode(security:list,*args,**kwargs):
    """
	获取组织机构代码

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"organizationcode",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getReportCur(security:list,*args,**kwargs):
    """
	获取记账本位币

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"report_cur",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIssuerShortened(security:list,*args,**kwargs):
    """
	获取发行人中文简称

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"issuershortened",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getMainProduct(security:list,*args,**kwargs):
    """
	获取主要产品及业务

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"mainproduct",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getCompPreName(security:list,*args,**kwargs):
    """
	获取公司曾用名

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"compprename",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getCbIssueOrNot(security:list,*args,**kwargs):
    """
	获取是否发行可转债

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"cbissueornot",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getVote(security:list,*args,**kwargs):
    """
	获取是否存在投票权差异

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"vote",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getSei(security:list,*args,**kwargs):
    """
	获取所属战略性新兴产业分类

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"sei",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getZJtXorNot(security:list,*args,**kwargs):
    """
	获取是否专精特新企业

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"zjtxornot",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIndustryCsrC12N(security:list,*args,**kwargs):
    """
	获取所属证监会行业名称

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"industry_csrc12_n",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIndustryCsrC(security:list,*args,**kwargs):
    """
	获取所属证监会行业名称(旧)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"industry_CSRC",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIndustryCsrCCode12(security:list,*args,**kwargs):
    """
	获取所属证监会行业代码

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"industry_CSRCcode12",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIndustryCsrCCode(security:list,*args,**kwargs):
    """
	获取所属证监会行业代码(旧)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"industry_CSRCcode",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIndustrySw(security:list,*args,**kwargs):
    """
	获取所属申万行业名称

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"industry_sw",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIndustrySw2021(security:list,*args,**kwargs):
    """
	获取所属申万行业名称(2021)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"industry_sw_2021",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIndustrySwHk(security:list,*args,**kwargs):
    """
	获取所属申万行业名称(港股)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"industry_sw_hk",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIndustrySw2021Hk(security:list,*args,**kwargs):
    """
	获取所属申万行业名称(港股)(2021)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"industry_sw_2021_hk",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIndustrySwCode(security:list,*args,**kwargs):
    """
	获取所属申万行业代码

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"industry_swcode",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIndustrySwCode2021(security:list,*args,**kwargs):
    """
	获取所属申万行业代码(2021)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"industry_swcode_2021",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIndustrySwCodeHk(security:list,*args,**kwargs):
    """
	获取所属申万行业代码(港股)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"industry_swcode_hk",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIndustrySwCode2021Hk(security:list,*args,**kwargs):
    """
	获取所属申万行业代码(港股)(2021)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"industry_swcode_2021_hk",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIndustrySwOriginCode(security:list,*args,**kwargs):
    """
	获取所属申万行业原始代码

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"industry_sworigincode",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIndustrySwOriginCode2021(security:list,*args,**kwargs):
    """
	获取所属申万行业原始代码(2021)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"industry_sworigincode_2021",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIndexCodeSw(security:list,*args,**kwargs):
    """
	获取所属申万行业指数代码

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"indexcode_sw",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIndustryCitiC(security:list,*args,**kwargs):
    """
	获取所属中信行业名称

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"industry_citic",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIndustryCitiCHk(security:list,*args,**kwargs):
    """
	获取所属中信行业名称(港股)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"industry_citic_hk",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIndustryCitiCCode(security:list,*args,**kwargs):
    """
	获取所属中信行业代码

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"industry_citiccode",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIndustryCitiCCodeHk(security:list,*args,**kwargs):
    """
	获取所属中信行业代码(港股)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"industry_citiccode_hk",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIndexCodeCitiC(security:list,*args,**kwargs):
    """
	获取所属中信行业指数代码

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"indexcode_citic",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIndexCodeCitiCHk(security:list,*args,**kwargs):
    """
	获取所属中信证券港股通指数代码(港股)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"indexcode_citic_hk",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIndexNameCitiCHk(security:list,*args,**kwargs):
    """
	获取所属中信证券港股通指数名称(港股)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"indexname_citic_hk",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIssuerIndustryCcXi(security:list,*args,**kwargs):
    """
	获取所属中诚信行业名称

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"issuer_industry_ccxi",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIndustryGicS2(security:list,*args,**kwargs):
    """
	获取废弃行业

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"industry_gics2",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIndustryHs(security:list,*args,**kwargs):
    """
	获取所属恒生行业名称

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"industry_HS",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIndustry2(security:list,*args,**kwargs):
    """
	获取所属行业名称(支持历史)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"industry2",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIndustryCode(security:list,*args,**kwargs):
    """
	获取所属行业代码(支持历史)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"industrycode",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIndustryName(security:list,*args,**kwargs):
    """
	获取所属行业板块名称(支持历史)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"industryname",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIndustryCsi(security:list,*args,**kwargs):
    """
	获取所属中证行业名称

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"industry_csi",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIndustryCsiCode(security:list,*args,**kwargs):
    """
	获取所属中证行业代码

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"industry_csicode",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIndustryNcCode(security:list,*args,**kwargs):
    """
	获取所属国民经济行业代码

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"industry_nccode",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIndustryCJsc(security:list,*args,**kwargs):
    """
	获取所属长江行业名称

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"industry_cjsc",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIndexCodeCJsc(security:list,*args,**kwargs):
    """
	获取所属长江行业指数代码

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"indexcode_cjsc",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIndustryCn(security:list,*args,**kwargs):
    """
	获取所属国证行业名称

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"industry_cn",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIndustryCnCode(security:list,*args,**kwargs):
    """
	获取所属国证行业代码

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"industry_cncode",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIndexCodeCn(security:list,*args,**kwargs):
    """
	获取所属国证行业指数代码

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"indexcode_cn",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getThematicIndustrySib(security:list,*args,**kwargs):
    """
	获取所属科创板主题行业

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"thematicindustry_sib",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getBoardChairmen(security:list,*args,**kwargs):
    """
	获取董事长

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"boardchairmen",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getStmNoteMGmtBenBc(security:list,*args,**kwargs):
    """
	获取董事长薪酬

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"stmnote_mgmt_ben_bc",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getCeo(security:list,*args,**kwargs):
    """
	获取总经理

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"ceo",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getStmNoteMGmtBenCeo(security:list,*args,**kwargs):
    """
	获取总经理薪酬

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"stmnote_mgmt_ben_ceo",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundCorpManager(security:list,*args,**kwargs):
    """
	获取基金管理人总经理

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_corpmanager",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getDIsCloser1(security:list,*args,**kwargs):
    """
	获取董事会秘书

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"discloser1",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getStmNoteMGmtBenDIsCloser(security:list,*args,**kwargs):
    """
	获取董事会秘书薪酬

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"stmnote_mgmt_ben_discloser",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getSar1(security:list,*args,**kwargs):
    """
	获取证券事务代表

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"sar1",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getStmNoteMGmtBenSar(security:list,*args,**kwargs):
    """
	获取证券事务代表薪酬

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"stmnote_mgmt_ben_sar",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getCfO(security:list,*args,**kwargs):
    """
	获取财务总监

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"cfo",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getStmNoteMGmtBenCfO(security:list,*args,**kwargs):
    """
	获取财务总监薪酬

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"stmnote_mgmt_ben_cfo",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getCrtInDpDirector(security:list,*args,**kwargs):
    """
	获取公司独立董事(现任)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"crtindpdirector",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getSUciNdpDirector(security:list,*args,**kwargs):
    """
	获取公司独立董事(历任)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"sucindpdirector",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getDirector(security:list,*args,**kwargs):
    """
	获取公司董事

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"director",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getSUcDirector(security:list,*args,**kwargs):
    """
	获取公司董事(历任)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"sucdirector",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getSupervisor(security:list,*args,**kwargs):
    """
	获取公司监事

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"supervisor",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getSUcSupervisor(security:list,*args,**kwargs):
    """
	获取公司监事(历任)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"sucsupervisor",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getExecutives(security:list,*args,**kwargs):
    """
	获取公司高管

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"executives",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getSUcExecutives(security:list,*args,**kwargs):
    """
	获取公司高管(历任)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"sucexecutives",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getStmNoteMGmtBenTop3B(security:list,*args,**kwargs):
    """
	获取金额前三的董事薪酬合计

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"stmnote_mgmt_ben_top3b",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getStmNoteMGmtBenTop3M(security:list,*args,**kwargs):
    """
	获取金额前三的高管薪酬合计

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"stmnote_mgmt_ben_top3m",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getEmployeeBoard(security:list,*args,**kwargs):
    """
	获取董事会人数

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"employee_board",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getEmployeeExecutiveDirector(security:list,*args,**kwargs):
    """
	获取非独立董事人数

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"employee_executivedirector",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getEmployeeInDpDirector(security:list,*args,**kwargs):
    """
	获取独立董事人数

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"employee_indpdirector",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getEmployeeMGmt(security:list,*args,**kwargs):
    """
	获取高管人数

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"employee_mgmt",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getEmployeeTechCore(security:list,*args,**kwargs):
    """
	获取核心技术人员人数

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"employee_techcore",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getAuditor(security:list,*args,**kwargs):
    """
	获取审计机构

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"auditor",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getAuditor2(security:list,*args,**kwargs):
    """
	获取审计机构(支持历史)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"auditor2",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIpoAuditor(security:list,*args,**kwargs):
    """
	获取首发审计机构

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"ipo_auditor",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getClo(security:list,*args,**kwargs):
    """
	获取法律顾问

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"clo",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getLiC(security:list,*args,**kwargs):
    """
	获取经办律师

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"lic",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIpoLawEr(security:list,*args,**kwargs):
    """
	获取首发经办律师

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"ipo_lawer",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundReItSvaAg(security:list,*args,**kwargs):
    """
	获取资产评估机构

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund__reitsvaag",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getVic(security:list,*args,**kwargs):
    """
	获取经办评估人员

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"vic",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getBanks(security:list,*args,**kwargs):
    """
	获取主要往来银行

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"banks",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getEmployeeProducer(security:list,*args,**kwargs):
    """
	获取生产人员人数

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"employee_producer",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getEmployeeProducerPct(security:list,*args,**kwargs):
    """
	获取生产人员人数占比

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"employee_producer_pct",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getEmployeeSale(security:list,*args,**kwargs):
    """
	获取销售人员人数

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"employee_sale",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getEmployeeSalePct(security:list,*args,**kwargs):
    """
	获取销售人员人数占比

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"employee_sale_pct",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getEmployeeServer(security:list,*args,**kwargs):
    """
	获取客服人员人数

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"employee_server",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getEmployeeServerPct(security:list,*args,**kwargs):
    """
	获取客服人员人数占比

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"employee_server_pct",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getEmployeeTech(security:list,*args,**kwargs):
    """
	获取技术人员人数

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"employee_tech",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getEmployeeTechPct(security:list,*args,**kwargs):
    """
	获取技术人员人数占比

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"employee_tech_pct",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getEmployeeFin(security:list,*args,**kwargs):
    """
	获取财务人员人数

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"employee_fin",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getEmployeeFinPct(security:list,*args,**kwargs):
    """
	获取财务人员人数占比

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"employee_fin_pct",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getEmployeeHr(security:list,*args,**kwargs):
    """
	获取人事人员人数

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"employee_hr",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getEmployeeHrPct(security:list,*args,**kwargs):
    """
	获取人事人员人数占比

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"employee_hr_pct",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getEmployeeExCu(security:list,*args,**kwargs):
    """
	获取行政人员人数

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"employee_excu",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getEmployeeExCuPct(security:list,*args,**kwargs):
    """
	获取行政人员人数占比

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"employee_excu_pct",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getEmployeeRc(security:list,*args,**kwargs):
    """
	获取风控稽核人员人数

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"employee_rc",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getEmployeeRcPct(security:list,*args,**kwargs):
    """
	获取风控稽核人员人数占比

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"employee_rc_pct",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getEmployeePur(security:list,*args,**kwargs):
    """
	获取采购仓储人员人数

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"employee_pur",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getEmployeePurPct(security:list,*args,**kwargs):
    """
	获取采购仓储人员人数占比

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"employee_pur_pct",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getEmployeeOThDept(security:list,*args,**kwargs):
    """
	获取其他人员人数

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"employee_othdept",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getEmployeePhd(security:list,*args,**kwargs):
    """
	获取博士人数

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"employee_PHD",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getEmployeePhdPct(security:list,*args,**kwargs):
    """
	获取博士人数占比

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"employee_PHD_pct",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getEmployeeMs(security:list,*args,**kwargs):
    """
	获取硕士人数

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"employee_MS",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getEmployeeMsPct(security:list,*args,**kwargs):
    """
	获取硕士人数占比

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"employee_MS_pct",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getEmployeeBa(security:list,*args,**kwargs):
    """
	获取本科人数

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"employee_BA",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getEmployeeBaPct(security:list,*args,**kwargs):
    """
	获取本科人数占比

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"employee_BA_pct",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getEmployeeColl(security:list,*args,**kwargs):
    """
	获取专科人数

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"employee_coll",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getEmployeeCollPct(security:list,*args,**kwargs):
    """
	获取专科人数占比

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"employee_coll_pct",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getEmployeeHighschool(security:list,*args,**kwargs):
    """
	获取高中及以下人数

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"employee_highschool",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getEmployeeHighschoolPct(security:list,*args,**kwargs):
    """
	获取高中及以下人数占比

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"employee_highschool_pct",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getEmployeeOThDegree(security:list,*args,**kwargs):
    """
	获取其他学历人数

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"employee_othdegree",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getEmployeeOThDegreePct(security:list,*args,**kwargs):
    """
	获取其他学历人数占比

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"employee_othdegree_pct",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getEmployeeOThDeptPct(security:list,*args,**kwargs):
    """
	获取其他专业人员人数占比

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"employee_othdept_pct",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getTotalShares(security:list,*args,**kwargs):
    """
	获取总股本

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"total_shares",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getMaTotalShares(security:list,*args,**kwargs):
    """
	获取备考总股本(并购后)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"matotalshares",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getShareToTSharesPre(security:list,*args,**kwargs):
    """
	获取上市前总股本

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"share_totshares_pre",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIpoToTCapAfterIssue(security:list,*args,**kwargs):
    """
	获取首发后总股本(上市日)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"ipo_totcapafterissue",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIpoToTCapBeforeIssue(security:list,*args,**kwargs):
    """
	获取首发前总股本

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"ipo_totcapbeforeissue",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIpoToTCapAfterIssueEst(security:list,*args,**kwargs):
    """
	获取预计发行后总股本

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"ipo_totcapafterissue_est",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getHolderPctLiq(security:list,*args,**kwargs):
    """
	获取流通股东持股比例(相对总股本)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"holder_pct_liq",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFreeFloatShares(security:list,*args,**kwargs):
    """
	获取自由流通股本

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"free_float_shares",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getShareTotalOtc(security:list,*args,**kwargs):
    """
	获取三板合计

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"share_totalotc",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getShareH(security:list,*args,**kwargs):
    """
	获取香港上市股

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"share_h",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getShareOverSea(security:list,*args,**kwargs):
    """
	获取海外上市股

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"share_oversea",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getShareTotalTradable(security:list,*args,**kwargs):
    """
	获取流通股合计

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"share_totaltradable",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getShareTotalRestricted(security:list,*args,**kwargs):
    """
	获取限售股合计

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"share_totalrestricted",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getShareNonTradable2(security:list,*args,**kwargs):
    """
	获取非流通股

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"share_nontradable2",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getCbResultEfInvestorNonTrAd(security:list,*args,**kwargs):
    """
	获取原非流通股股东有效申购户数

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"cb_result_efinvestornontrad",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getCbResultEfAmNtNonTrAd(security:list,*args,**kwargs):
    """
	获取原非流通股股东有效申购金额

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"cb_result_efamntnontrad",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getCbResultRationAmtNonTrAd(security:list,*args,**kwargs):
    """
	获取原非流通股股东获配金额

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"cb_result_rationamtnontrad",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getShareNtrDPrFShare(security:list,*args,**kwargs):
    """
	获取优先股

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"share_ntrd_prfshare",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWgsDPfDStK(security:list,*args,**kwargs):
    """
	获取优先股_GSD

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"wgsd_pfd_stk",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWgsDDvdPfDAdj(security:list,*args,**kwargs):
    """
	获取优先股利及其他调整项_GSD

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"wgsd_dvd_pfd_adj",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWgsDQfaDvdPfDAdj(security:list,*args,**kwargs):
    """
	获取单季度.优先股利及其他调整项_GSD

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"wgsd_qfa_dvd_pfd_adj",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getOtherEquityInstrumentsPre(security:list,*args,**kwargs):
    """
	获取其他权益工具:优先股

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"other_equity_instruments_PRE",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getShareIssuing(security:list,*args,**kwargs):
    """
	获取已发行数量

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"share_issuing",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getShareIssuingMkt(security:list,*args,**kwargs):
    """
	获取流通股本

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"share_issuing_mkt",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getShareRTdState(security:list,*args,**kwargs):
    """
	获取限售股份(国家持股)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"share_rtd_state",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getShareRTdStateJur(security:list,*args,**kwargs):
    """
	获取限售股份(国有法人持股)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"share_rtd_statejur",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getShareRTdSubOtherDomes(security:list,*args,**kwargs):
    """
	获取限售股份(其他内资持股合计)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"share_rtd_subotherdomes",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getShareRTdDomesJur(security:list,*args,**kwargs):
    """
	获取限售股份(境内法人持股)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"share_rtd_domesjur",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getShareRTdInSt(security:list,*args,**kwargs):
    """
	获取限售股份(机构配售股份)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"share_rtd_inst",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getShareRTdDomeSnp(security:list,*args,**kwargs):
    """
	获取限售股份(境内自然人持股)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"share_rtd_domesnp",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getShareRTdSubFrgN(security:list,*args,**kwargs):
    """
	获取限售股份(外资持股合计)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"share_rtd_subfrgn",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getShareRTdFrgNJur(security:list,*args,**kwargs):
    """
	获取限售股份(境外法人持股)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"share_rtd_frgnjur",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getShareRTdFrgNNp(security:list,*args,**kwargs):
    """
	获取限售股份(境外自然人持股)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"share_rtd_frgnnp",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getSharePledgedAPct(security:list,*args,**kwargs):
    """
	获取质押比例

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"share_pledgeda_pct",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getShareLiqAPledgedPct(security:list,*args,**kwargs):
    """
	获取无限售股份质押比例

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"share_liqa_pledgedpct",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getShareRestrictedAPledgedPct(security:list,*args,**kwargs):
    """
	获取有限售股份质押比例

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"share_restricteda_pledgedpct",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getShareLiqAPledged(security:list,*args,**kwargs):
    """
	获取无限售股份质押数量

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"share_liqa_pledged",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getShareRestrictedAPledged(security:list,*args,**kwargs):
    """
	获取有限售股份质押数量

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"share_restricteda_pledged",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getSharePledgedRepurchase(security:list,*args,**kwargs):
    """
	获取质押待购回余量

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"share_pledged_repurchase",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getShareRTdUnlockingDate(security:list,*args,**kwargs):
    """
	获取限售解禁日期

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"share_rtd_unlockingdate",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getShareTradableCurrent(security:list,*args,**kwargs):
    """
	获取本期解禁数量

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"share_tradable_current",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getShareRTdBAnce(security:list,*args,**kwargs):
    """
	获取未流通数量

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"share_rtd_bance",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getShareRTdDataType(security:list,*args,**kwargs):
    """
	获取解禁数据类型

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"share_rtd_datatype",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getShareRTdDataTypeFwd(security:list,*args,**kwargs):
    """
	获取指定日之后最近一次解禁数据类型

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"share_rtd_datatype_fwd",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getShareTradableShareType(security:list,*args,**kwargs):
    """
	获取解禁股份性质

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"share_tradable_sharetype",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getShareTradableShareTypeFwd(security:list,*args,**kwargs):
    """
	获取指定日之后最近一次解禁股份性质

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"share_tradable_sharetype_fwd",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getShareRTdUnlockingDateFwd(security:list,*args,**kwargs):
    """
	获取指定日之后最近一次解禁日期

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"share_rtd_unlockingdate_fwd",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getShareTradableCurrentFwd(security:list,*args,**kwargs):
    """
	获取指定日之后最近一次解禁数量

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"share_tradable_current_fwd",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getShareOtcTradable(security:list,*args,**kwargs):
    """
	获取流通三板股

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"share_otctradable",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getShareOtcTradableController(security:list,*args,**kwargs):
    """
	获取流通股(控股股东或实际控制人)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"share_otctradable_controller",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getShareOtcTradableBackbone(security:list,*args,**kwargs):
    """
	获取流通股(核心员工)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"share_otctradable_backbone",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getShareOtcTradableOthers(security:list,*args,**kwargs):
    """
	获取流通股(其他)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"share_otctradable_others",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getShareOtcRestricted(security:list,*args,**kwargs):
    """
	获取限售三板股

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"share_otcrestricted",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getShareOtcRestrictedController(security:list,*args,**kwargs):
    """
	获取限售股份(控股股东或实际控制人)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"share_otcrestricted_controller",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getShareRestrictedM(security:list,*args,**kwargs):
    """
	获取限售股份(高管持股)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"share_restricted_m",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getShareOtcRestrictedBackbone(security:list,*args,**kwargs):
    """
	获取限售股份(核心员工)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"share_otcrestricted_backbone",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getShareOtcRestrictedOthers(security:list,*args,**kwargs):
    """
	获取限售股份(其他)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"share_otcrestricted_others",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getUnitMergedSharesOrNot(security:list,*args,**kwargs):
    """
	获取份额是否为合并数据

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"unit_mergedsharesornot",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getHolderMergedHoldingOrNot(security:list,*args,**kwargs):
    """
	获取持有份额是否为合并数据

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"holder_mergedholdingornot",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getUnitFloorTrading(security:list,*args,**kwargs):
    """
	获取场内流通份额

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"unit_floortrading",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getUnitFloorTradingChange(security:list,*args,**kwargs):
    """
	获取当期场内流通份额变化

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"unit_floortradingchange",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getUnitPurchase(security:list,*args,**kwargs):
    """
	获取报告期总申购份额

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"unit_purchase",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getUnitRedemption(security:list,*args,**kwargs):
    """
	获取报告期总赎回份额

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"unit_redemption",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getUnitNetPurchase(security:list,*args,**kwargs):
    """
	获取报告期申购赎回净额

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"unit_netpurchase",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getUnitPurchaseQTy(security:list,*args,**kwargs):
    """
	获取单季度总申购份额

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"unit_purchase_qty",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getUnitRedemptionQTy(security:list,*args,**kwargs):
    """
	获取单季度总赎回份额

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"unit_redemption_qty",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getUnitNetQuarterlyRatio(security:list,*args,**kwargs):
    """
	获取单季度净申购赎回率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"unit_netquarterlyratio",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getUnitNetPurchaseQTy(security:list,*args,**kwargs):
    """
	获取单季度申购赎回净额

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"unit_netpurchase_qty",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getHolderTop10Pct(security:list,*args,**kwargs):
    """
	获取前十大股东持股比例合计

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"holder_top10pct",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getHolderTop10Quantity(security:list,*args,**kwargs):
    """
	获取前十大股东持股数量合计

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"holder_top10quantity",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getHolderTop10LiqQuantity(security:list,*args,**kwargs):
    """
	获取前十大流通股东持股数量合计

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"holder_top10liqquantity",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getSharePledgedAHolder(security:list,*args,**kwargs):
    """
	获取大股东累计质押数量

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"share_pledgeda_holder",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getSharePledgedALargestHolder(security:list,*args,**kwargs):
    """
	获取大股东累计质押数量(旧)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"share_pledgeda_largestholder",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getSharePledgedAPctHolder(security:list,*args,**kwargs):
    """
	获取大股东累计质押数占持股数比例

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"share_pledgeda_pct_holder",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getSharePledgedAPctLargestHolder(security:list,*args,**kwargs):
    """
	获取大股东累计质押数占持股数比例(旧)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"share_pledgeda_pct_largestholder",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getShareFrozenAHolder(security:list,*args,**kwargs):
    """
	获取大股东累计冻结数量

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"share_frozena_holder",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getShareFrozenAPctHolder(security:list,*args,**kwargs):
    """
	获取大股东累计冻结数占持股数比例

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"share_frozena_pct_holder",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getHolderRpTController(security:list,*args,**kwargs):
    """
	获取公布实际控制人名称

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"holder_rptController",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getHolderController(security:list,*args,**kwargs):
    """
	获取实际控制人名称

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"holder_controller",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getHolderControllerAtTr(security:list,*args,**kwargs):
    """
	获取实际控制人属性

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"holder_controllerattr",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getHolderInstitute(security:list,*args,**kwargs):
    """
	获取机构股东名称

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"holder_institute",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getHolderName(security:list,*args,**kwargs):
    """
	获取大股东名称

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"holder_name",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getHolderQuantity(security:list,*args,**kwargs):
    """
	获取大股东持股数量

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"holder_quantity",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getHolderPct(security:list,*args,**kwargs):
    """
	获取大股东持股比例

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"holder_pct",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getHolderSumPctTop5(security:list,*args,**kwargs):
    """
	获取前5大股东持股比例之和_PIT

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"holder_sumpcttop5",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getHolderSumsQuPctTop5(security:list,*args,**kwargs):
    """
	获取前5大股东持股比例平方之和_PIT

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"holder_sumsqupcttop5",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getHolderSumsQuPctTop10(security:list,*args,**kwargs):
    """
	获取前10大股东持股比例平方之和_PIT

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"holder_sumsqupcttop10",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getHolderShareCategory(security:list,*args,**kwargs):
    """
	获取大股东持股股本性质

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"holder_sharecategory",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getHolderQuantityRestricted(security:list,*args,**kwargs):
    """
	获取大股东持有的限售股份数

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"holder_quantity_restricted",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getHolderNature(security:list,*args,**kwargs):
    """
	获取大股东性质

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"holder_nature",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getHolderCategory(security:list,*args,**kwargs):
    """
	获取机构股东类型

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"holder_category",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getHolderLiqName(security:list,*args,**kwargs):
    """
	获取流通股东名称

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"holder_liqname",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getHolderLiqQuantity(security:list,*args,**kwargs):
    """
	获取流通股东持股数量

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"holder_liqquantity",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getHolderLiqPct(security:list,*args,**kwargs):
    """
	获取流通股东持股比例

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"holder_liqpct",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getHolderLiqShareCategory(security:list,*args,**kwargs):
    """
	获取流通股东持股股本性质

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"holder_liqsharecategory",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getHolderAvgNum(security:list,*args,**kwargs):
    """
	获取户均持股数量

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"holder_avgnum",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getHolderAvgPct(security:list,*args,**kwargs):
    """
	获取户均持股比例

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"holder_avgpct",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getHolderHAvgPctChange(security:list,*args,**kwargs):
    """
	获取户均持股比例半年增长率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"holder_havgpctchange",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getHolderQAvgPctChange(security:list,*args,**kwargs):
    """
	获取户均持股比例季度增长率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"holder_qavgpctchange",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getHolderAvgPctChange(security:list,*args,**kwargs):
    """
	获取相对上一报告期户均持股比例差

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"holder_avgpctchange",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getHolderHAvgChange(security:list,*args,**kwargs):
    """
	获取户均持股数半年增长率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"holder_havgchange",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getHolderQAvgChange(security:list,*args,**kwargs):
    """
	获取户均持股数季度增长率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"holder_qavgchange",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getHolderTotalByFund(security:list,*args,**kwargs):
    """
	获取基金持股数量

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"holder_totalbyfund",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getHolderTotalBySSFund(security:list,*args,**kwargs):
    """
	获取社保基金持股数量

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"holder_totalbyssfund",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getHolderTotalByBySec(security:list,*args,**kwargs):
    """
	获取券商持股数量

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"holder_totalbybysec",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getHolderTotalByByWMp(security:list,*args,**kwargs):
    """
	获取券商理财产品持股数量

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"holder_totalbybywmp",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getHolderTotalByHf(security:list,*args,**kwargs):
    """
	获取阳光私募持股数量

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"holder_totalbyhf",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getHolderTotalByInSur(security:list,*args,**kwargs):
    """
	获取保险公司持股数量

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"holder_totalbyinsur",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getHolderTotalByCorpPension(security:list,*args,**kwargs):
    """
	获取企业年金持股数量

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"holder_totalbycorppension",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getHolderTotalByTrustCorp(security:list,*args,**kwargs):
    """
	获取信托公司持股数量

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"holder_totalbytrustcorp",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getHolderTotalByFinanceCorp(security:list,*args,**kwargs):
    """
	获取财务公司持股数量

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"holder_totalbyfinancecorp",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getHolderTotalByBank(security:list,*args,**kwargs):
    """
	获取银行持股数量

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"holder_totalbybank",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getHolderTotalByGeneralCorp(security:list,*args,**kwargs):
    """
	获取一般法人持股数量

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"holder_totalbygeneralcorp",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getHolderTotalByLnFCorp(security:list,*args,**kwargs):
    """
	获取非金融类上市公司持股数量

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"holder_totalbylnfcorp",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getHolderPctByFund(security:list,*args,**kwargs):
    """
	获取基金持股比例

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"holder_pctbyfund",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getHolderPctBySSFund(security:list,*args,**kwargs):
    """
	获取社保基金持股比例

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"holder_pctbyssfund",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getHolderPctBySec(security:list,*args,**kwargs):
    """
	获取券商持股比例

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"holder_pctbysec",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getHolderPctByByWMp(security:list,*args,**kwargs):
    """
	获取券商理财产品持股比例

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"holder_pctbybywmp",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getHolderPctByHf(security:list,*args,**kwargs):
    """
	获取阳光私募持股比例

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"holder_pctbyhf",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getHolderPctByInSur(security:list,*args,**kwargs):
    """
	获取保险公司持股比例

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"holder_pctbyinsur",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getHolderPctByCorpPension(security:list,*args,**kwargs):
    """
	获取企业年金持股比例

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"holder_pctbycorppension",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getHolderPctByTrustCorp(security:list,*args,**kwargs):
    """
	获取信托公司持股比例

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"holder_pctbytrustcorp",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getHolderPctByFinanceCorp(security:list,*args,**kwargs):
    """
	获取财务公司持股比例

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"holder_pctbyfinancecorp",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getHolderPctByBank(security:list,*args,**kwargs):
    """
	获取银行持股比例

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"holder_pctbybank",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getHolderPctByGeneralCorp(security:list,*args,**kwargs):
    """
	获取一般法人持股比例

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"holder_pctbygeneralcorp",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getHolderPctByLnFCorp(security:list,*args,**kwargs):
    """
	获取非金融类上市公司持股比例

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"holder_pctbylnfcorp",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getHolderNumI(security:list,*args,**kwargs):
    """
	获取持股机构数

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"holder_num_i",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getHolderNumFund(security:list,*args,**kwargs):
    """
	获取持股基金数

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"holder_num_fund",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getHolderNumSSFund(security:list,*args,**kwargs):
    """
	获取持股社保基金数

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"holder_num_ssfund",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getHolderNumInSur(security:list,*args,**kwargs):
    """
	获取持股保险公司数

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"holder_num_insur",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getHolderPriceFellowOn(security:list,*args,**kwargs):
    """
	获取定向增发价格

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"holder_price_fellowon",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getHolderPriceMajorShareholders(security:list,*args,**kwargs):
    """
	获取大股东增持价格

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"holder_price_Majorshareholders",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getHolderPriceEsOp(security:list,*args,**kwargs):
    """
	获取员工持股计划买入价格

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"holder_price_ESOP",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getHolderMergedNumberOrNot(security:list,*args,**kwargs):
    """
	获取持有人户数是否为合并数据

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"holder_mergednumberornot",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getHolderInstitutionHolding(security:list,*args,**kwargs):
    """
	获取机构投资者持有份额

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"holder_institution_holding",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getHolderInstitutionTotalHolding(security:list,*args,**kwargs):
    """
	获取机构投资者持有份额(合计)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"holder_institution_totalholding",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getHolderInstitutionHoldingPct(security:list,*args,**kwargs):
    """
	获取机构投资者持有比例

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"holder_institution_holdingpct",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getHolderInstitutionTotalHoldingPct(security:list,*args,**kwargs):
    """
	获取机构投资者持有比例(合计)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"holder_institution_totalholdingpct",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getHolderMNgEmpHolding(security:list,*args,**kwargs):
    """
	获取管理人员工持有份额

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"holder_mngemp_holding",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getHolderMNgEmpHoldingPct(security:list,*args,**kwargs):
    """
	获取管理人员工持有比例

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"holder_mngemp_holdingpct",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getHolderCorpHolding(security:list,*args,**kwargs):
    """
	获取基金管理公司持有份额

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"holder_corp_holding",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getHolderCorpHoldingPct(security:list,*args,**kwargs):
    """
	获取基金管理公司持有比例

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"holder_corp_holdingpct",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getHolderPersonalHolding(security:list,*args,**kwargs):
    """
	获取个人投资者持有份额

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"holder_personal_holding",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getHolderPersonalTotalHolding(security:list,*args,**kwargs):
    """
	获取个人投资者持有份额(合计)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"holder_personal_totalholding",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getHolderPersonalHoldingPct(security:list,*args,**kwargs):
    """
	获取个人投资者持有比例

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"holder_personal_holdingpct",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getHolderPersonalTotalHoldingPct(security:list,*args,**kwargs):
    """
	获取个人投资者持有比例(合计)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"holder_personal_totalholdingpct",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundHolderTop10Holding(security:list,*args,**kwargs):
    """
	获取前十大持有人持有份额合计

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_holder_top10_holding",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundHolderTop10HoldingMmF(security:list,*args,**kwargs):
    """
	获取前十大持有人持有份额合计(货币)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_holder_top10_holdingmmf",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundHolderTop10Pct(security:list,*args,**kwargs):
    """
	获取前十大持有人持有比例合计

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_holder_top10_pct",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundHolderTop10PctMmF(security:list,*args,**kwargs):
    """
	获取前十大持有人持有比例合计(货币)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_holder_top10_pctmmf",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getHolderSingleHolding(security:list,*args,**kwargs):
    """
	获取单一投资者报告期末持有份额

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"holder_single_holding",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getHolderSingleTotalHolding(security:list,*args,**kwargs):
    """
	获取单一投资者报告期末持有份额合计

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"holder_single_totalholding",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getHolderSingleHoldingPct(security:list,*args,**kwargs):
    """
	获取单一投资者报告期末持有比例

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"holder_single_holdingpct",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getHolderSingleTotalHoldingPct(security:list,*args,**kwargs):
    """
	获取单一投资者报告期末持有比例合计

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"holder_single_totalholdingpct",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getBondQualifiedInvestor(security:list,*args,**kwargs):
    """
	获取合格投资者类型

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"bond_qualified_investor",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundHoldFunds(security:list,*args,**kwargs):
    """
	获取持有基金家数

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fundhold_funds",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundHoldRatioOfPositionToAmNt(security:list,*args,**kwargs):
    """
	获取基金持有数量合计占存量比

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fundhold_ratioofpositiontoamnt",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundHoldPosition(security:list,*args,**kwargs):
    """
	获取基金持有数量合计

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fundhold_position",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getBondHolderName(security:list,*args,**kwargs):
    """
	获取持有人名称

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"bondholder_name",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundHolderName(security:list,*args,**kwargs):
    """
	获取第N名持有人名称

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_holder_name",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundHolderNameListing(security:list,*args,**kwargs):
    """
	获取第N名持有人名称(上市公告)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_holder_namelisting",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getBondHolderPct(security:list,*args,**kwargs):
    """
	获取持有人持有比例

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"bondholder_pct",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundHolderPct(security:list,*args,**kwargs):
    """
	获取第N名持有人持有比例

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_holder_pct",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundHolderPctListing(security:list,*args,**kwargs):
    """
	获取第N名持有人持有比例(上市公告)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_holder_pctlisting",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundHolderPctMmF(security:list,*args,**kwargs):
    """
	获取第N名持有人持有比例(货币)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_holder_pctmmf",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getBondHolderQuantity(security:list,*args,**kwargs):
    """
	获取持有人持有数量

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"bondholder_quantity",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundHoldBondNames(security:list,*args,**kwargs):
    """
	获取持有基金名称

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fundholdbond_names",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundHoldBondValue(security:list,*args,**kwargs):
    """
	获取基金持债市值

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fundholdbond_value",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundHoldBondRatio(security:list,*args,**kwargs):
    """
	获取基金持债市值占发行量比

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fundholdbond_ratio",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getShareN(security:list,*args,**kwargs):
    """
	获取沪(深)股通持股数量

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"share_N",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getShareHkS(security:list,*args,**kwargs):
    """
	获取港股通持股数量

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"share_HKS",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getShareHkSh(security:list,*args,**kwargs):
    """
	获取沪市港股通持股数量

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"share_HKSH",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getShareHkSz(security:list,*args,**kwargs):
    """
	获取深市港股通持股数量

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"share_HKSZ",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getSharePctN(security:list,*args,**kwargs):
    """
	获取沪(深)股通持股占比

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"share_pct_N",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getSharePctNToFreeFloat(security:list,*args,**kwargs):
    """
	获取沪(深)股通持股占自由流通股比例

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"share_pct_Ntofreefloat",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getSharePctHkS(security:list,*args,**kwargs):
    """
	获取港股通持股占比

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"share_pct_HKS",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getSharePctHkSh(security:list,*args,**kwargs):
    """
	获取沪市港股通持股占比

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"share_pct_HKSH",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getSharePctHkSz(security:list,*args,**kwargs):
    """
	获取深市港股通持股占比

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"share_pct_HKSZ",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFullName(security:list,*args,**kwargs):
    """
	获取证券全称

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fullname",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIssuerUpdated(security:list,*args,**kwargs):
    """
	获取债务主体

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"issuerupdated",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIssuerActual(security:list,*args,**kwargs):
    """
	获取实际发行人

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"issuer_actual",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPar(security:list,*args,**kwargs):
    """
	获取债券初始面值

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"par",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getLatestPar(security:list,*args,**kwargs):
    """
	获取债券最新面值

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"latestpar",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIssueAmount(security:list,*args,**kwargs):
    """
	获取发行总额

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"issueamount",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getTranche(security:list,*args,**kwargs):
    """
	获取各级发行总额

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"tranche",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getCbIssueAmount(security:list,*args,**kwargs):
    """
	获取转债发行总额

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"cb_issueamount",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIssueAmountPlan(security:list,*args,**kwargs):
    """
	获取计划发行总额

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"issue_amountplan",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getTenderAmountPlan(security:list,*args,**kwargs):
    """
	获取计划发行总额(文字)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"tender_amountplan",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getTendRstAmountAct(security:list,*args,**kwargs):
    """
	获取实际发行总额

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"tendrst_amountact",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getTrancheRatio(security:list,*args,**kwargs):
    """
	获取各级占比

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"trancheratio",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getOutstandingBalance(security:list,*args,**kwargs):
    """
	获取债券余额

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"outstandingbalance",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFinaTotalAmount(security:list,*args,**kwargs):
    """
	获取存量债券余额

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fina_totalamount",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFinalTotalAmOutAnytime(security:list,*args,**kwargs):
    """
	获取存量债券余额(支持历史)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"final_totalamout_anytime",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFinaMat(security:list,*args,**kwargs):
    """
	获取存量债券余额(按期限)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fina_mat",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getTBondBalance(security:list,*args,**kwargs):
    """
	获取国债余额(做市后)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"tbondbalance",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getCarryDate(security:list,*args,**kwargs):
    """
	获取起息日期

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"carrydate",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getCarryEnddate(security:list,*args,**kwargs):
    """
	获取计息截止日

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"carryenddate",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getMaturityDate(security:list,*args,**kwargs):
    """
	获取到期日期

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"maturitydate",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getTerm(security:list,*args,**kwargs):
    """
	获取债券期限(年)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"term",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getTerm2(security:list,*args,**kwargs):
    """
	获取债券期限(文字)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"term2",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getInterestType(security:list,*args,**kwargs):
    """
	获取利率类型

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"interesttype",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getCouponRate(security:list,*args,**kwargs):
    """
	获取票面利率(发行时)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"couponrate",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getCouponTxt(security:list,*args,**kwargs):
    """
	获取利率说明

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"coupontxt",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getClauseInterest6(security:list,*args,**kwargs):
    """
	获取补偿利率说明

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"clause_interest_6",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPaymentType(security:list,*args,**kwargs):
    """
	获取计息方式

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"paymenttype",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getActualBenchmark(security:list,*args,**kwargs):
    """
	获取计息基准

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"actualbenchmark",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getCoupon(security:list,*args,**kwargs):
    """
	获取息票品种

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"coupon",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getForm(security:list,*args,**kwargs):
    """
	获取凭证类别

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"form",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getInterestFrequency(security:list,*args,**kwargs):
    """
	获取每年付息次数

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"interestfrequency",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPaymentDate(security:list,*args,**kwargs):
    """
	获取年付息日

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"paymentdate",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getCouponDateTxt(security:list,*args,**kwargs):
    """
	获取付息日说明

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"coupondatetxt",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getTaxFree(security:list,*args,**kwargs):
    """
	获取是否免税

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"taxfree",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getTaxRate(security:list,*args,**kwargs):
    """
	获取税率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"taxrate",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getMktPriceType(security:list,*args,**kwargs):
    """
	获取市价类型

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"mktpricetype",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getRedemptionBeginning(security:list,*args,**kwargs):
    """
	获取兑付日

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"redemption_beginning",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getRedemptionRegBeginning(security:list,*args,**kwargs):
    """
	获取兑付登记日

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"redemption_regbeginning",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getRedemptionFeeRation(security:list,*args,**kwargs):
    """
	获取兑付费率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"redemption_feeration",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getRepaymentMethod(security:list,*args,**kwargs):
    """
	获取偿还方式

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"repaymentmethod",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPaymentOrder(security:list,*args,**kwargs):
    """
	获取偿付顺序

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"paymentorder",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIsAssetOut(security:list,*args,**kwargs):
    """
	获取资产是否出表

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"isassetout",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getAbsSPv(security:list,*args,**kwargs):
    """
	获取计划管理人

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"abs_spv",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundReItsOriginal(security:list,*args,**kwargs):
    """
	获取原始权益人

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund__reitsoriginal",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundReItsOrCom(security:list,*args,**kwargs):
    """
	获取原始权益人企业性质

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund__reitsorcom",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getAbsPenetrateActRuAlDebtor(security:list,*args,**kwargs):
    """
	获取穿透信用主体

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"abs_penetrateactrualdebtor",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIssuerBankType(security:list,*args,**kwargs):
    """
	获取发行人(银行)类型

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"issuer_banktype",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getRepoLastEstDate(security:list,*args,**kwargs):
    """
	获取最新交易日期

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"repo_lastestdate",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getAbsCurrentLoan(security:list,*args,**kwargs):
    """
	获取当前贷款笔数

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"abs_currentloan",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getAbsCurrentLoans(security:list,*args,**kwargs):
    """
	获取当前贷款余额

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"abs_currentloans",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getAbsCurrentWarm(security:list,*args,**kwargs):
    """
	获取当前加权平均贷款剩余期限

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"abs_currentwarm",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getAbsCurrentWtGAvgRate(security:list,*args,**kwargs):
    """
	获取当前加权平均贷款利率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"abs_currentwtgavgrate",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getAbsCumulativeDefaultRate(security:list,*args,**kwargs):
    """
	获取累计违约率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"abs_cumulativedefaultrate",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getAbsDelinquencyRate(security:list,*args,**kwargs):
    """
	获取严重拖欠率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"abs_delinquencyrate",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getAbsCreditNormal(security:list,*args,**kwargs):
    """
	获取承销团成员

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"abs_creditnormal",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getAbsIndustry(security:list,*args,**kwargs):
    """
	获取主体行业

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"abs_industry",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getAbsIndustry1(security:list,*args,**kwargs):
    """
	获取主体性质

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"abs_industry1",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getAbsProvince(security:list,*args,**kwargs):
    """
	获取主体地区

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"abs_province",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getAbsAgencyTrustee1(security:list,*args,**kwargs):
    """
	获取受托机构

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"abs_agency_trustee1",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getAbsFullNamePro(security:list,*args,**kwargs):
    """
	获取项目名称

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"abs_fullnamepro",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getAbsNamePro(security:list,*args,**kwargs):
    """
	获取项目简称

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"abs_namepro",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getAbsProjectCode(security:list,*args,**kwargs):
    """
	获取项目代码

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"abs_projectcode",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getAbsPayBack(security:list,*args,**kwargs):
    """
	获取还本方式

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"abs_payback",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPrepayMethod(security:list,*args,**kwargs):
    """
	获取提前还本方式

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"prepaymethod",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getAbsBorrower(security:list,*args,**kwargs):
    """
	获取基础债务人

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"abs_borrower",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getAbsCoreIndustry(security:list,*args,**kwargs):
    """
	获取基础债务人行业

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"abs_coreindustry",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getAbsCoreProvince(security:list,*args,**kwargs):
    """
	获取基础债务人地区

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"abs_coreprovince",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getAbsCoreProperty(security:list,*args,**kwargs):
    """
	获取基础债务人性质

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"abs_coreproperty",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getAbsRecommendCpr(security:list,*args,**kwargs):
    """
	获取早偿率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"abs_recommendcpr",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getAbsWeightedAverageMaturityWithPrepay(security:list,*args,**kwargs):
    """
	获取加权平均期限

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"abs_weightedaveragematuritywithprepay",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getAbsCreditSupport(security:list,*args,**kwargs):
    """
	获取信用支持

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"abs_creditsupport",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getAbsDealOutStStandingAmount(security:list,*args,**kwargs):
    """
	获取项目余额

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"abs_dealoutststandingamount",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getAbsFiExdCapitalCostRate(security:list,*args,**kwargs):
    """
	获取固定资金成本

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"abs_fiexdcapitalcostrate",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getAbsCapYieldPerTermOfSub(security:list,*args,**kwargs):
    """
	获取次级每期收益率上限

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"abs_capyieldpertermofSUB",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getAbsSelfSustainingProportion(security:list,*args,**kwargs):
    """
	获取自持比例

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"abs_selfsustainingproportion",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getAbsLegalMaturity(security:list,*args,**kwargs):
    """
	获取法定到期日

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"abs_legalmaturity",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getAbsPaymentDate(security:list,*args,**kwargs):
    """
	获取支付日

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"abs_paymentdate",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getAbsFirstPaymentDate(security:list,*args,**kwargs):
    """
	获取首次支付日

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"abs_firstpaymentdate",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getAbsExpectedMaturityWithPrepay(security:list,*args,**kwargs):
    """
	获取早偿预期到期日

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"abs_expectedmaturitywithprepay",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getAbsCutoffDate(security:list,*args,**kwargs):
    """
	获取初始起算日

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"abs_cutoffdate",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getAbsStartDateOfAssetClearing(security:list,*args,**kwargs):
    """
	获取清算起始日

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"abs_startdateofassetclearing",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getAbsEnddateOfAssetClearing(security:list,*args,**kwargs):
    """
	获取清算结束日

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"abs_enddateofassetclearing",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getAbsDefIGuarantor(security:list,*args,**kwargs):
    """
	获取差额支付承诺人

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"abs_defiguarantor",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getAbsTrustee(security:list,*args,**kwargs):
    """
	获取专项计划托管人

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"abs_trustee",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getAbsAssetServiceAgency(security:list,*args,**kwargs):
    """
	获取资产服务机构

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"abs_assetserviceagency",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getAccountTreatment(security:list,*args,**kwargs):
    """
	获取会计处理

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"accounttreatment",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getChinaBondL1Type(security:list,*args,**kwargs):
    """
	获取中债债券一级分类

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"chinabondl1type",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getChinaBondL2Type(security:list,*args,**kwargs):
    """
	获取中债债券二级分类

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"chinabondl2type",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getMunicipalBondWind(security:list,*args,**kwargs):
    """
	获取是否城投债(Wind)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"municipalbondWind",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getMunicipalBond(security:list,*args,**kwargs):
    """
	获取是否城投债

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"municipalbond",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getMunicipalBondyY(security:list,*args,**kwargs):
    """
	获取是否城投债(YY)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"municipalbondYY",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getCityInvestmentBondGeoWind(security:list,*args,**kwargs):
    """
	获取城投行政级别(Wind)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"cityinvestmentbondgeoWind",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getCityInvestmentBondGeo(security:list,*args,**kwargs):
    """
	获取城投行政级别

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"cityinvestmentbondgeo",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getMultiMktOrNot(security:list,*args,**kwargs):
    """
	获取是否跨市场交易

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"multimktornot",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getSubordinateOrNot(security:list,*args,**kwargs):
    """
	获取是否次级债

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"subordinateornot",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getMixCapital(security:list,*args,**kwargs):
    """
	获取是否混合资本债券

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"mixcapital",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIssueAdditional(security:list,*args,**kwargs):
    """
	获取是否增发

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"issueadditional",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getAdditionalTo(security:list,*args,**kwargs):
    """
	获取增发债对应原债券

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"additionalto",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPerpetualOrNot(security:list,*args,**kwargs):
    """
	获取是否永续债

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"perpetualornot",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getBaseRate(security:list,*args,**kwargs):
    """
	获取基准利率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"baserate",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getCmBir(security:list,*args,**kwargs):
    """
	获取基准利率确定方式

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"cmbir",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getBaseRate2(security:list,*args,**kwargs):
    """
	获取基准利率(发行时)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"baserate2",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getBaseRate3(security:list,*args,**kwargs):
    """
	获取基准利率(指定日期)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"baserate3",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getCalcFloatBench(security:list,*args,**kwargs):
    """
	获取计算浮息债隐含基准利率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"calc_floatbench",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getSpread(security:list,*args,**kwargs):
    """
	获取固定利差

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"spread",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIssueFirstPriceDate(security:list,*args,**kwargs):
    """
	获取首个定价日

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"issue_firstpricedate",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getCouponRate2(security:list,*args,**kwargs):
    """
	获取票面利率(当期)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"couponrate2",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getCouponRate3(security:list,*args,**kwargs):
    """
	获取票面利率(指定日期)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"couponrate3",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getSpread2(security:list,*args,**kwargs):
    """
	获取行权后利差

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"spread2",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getInterestFloor(security:list,*args,**kwargs):
    """
	获取保底利率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"interestfloor",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getEmbeddedOpt(security:list,*args,**kwargs):
    """
	获取是否含权债

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"embeddedopt",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getClause(security:list,*args,**kwargs):
    """
	获取特殊条款

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"clause",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getClauseAbbr(security:list,*args,**kwargs):
    """
	获取特殊条款(缩写)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"clauseabbr",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getClauseItem(security:list,*args,**kwargs):
    """
	获取指定条款文字

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"clauseitem",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getExecMaturityEmbedded(security:list,*args,**kwargs):
    """
	获取含权债行权期限

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"execmaturityembedded",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getEObSpecialInStrutIons(security:list,*args,**kwargs):
    """
	获取含权债期限特殊说明

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"eobspecialinstrutions",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPrepaymentDate(security:list,*args,**kwargs):
    """
	获取提前还本日

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"prepaymentdate",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPrepayPortion(security:list,*args,**kwargs):
    """
	获取提前还本比例

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"prepayportion",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getRedemptionDate(security:list,*args,**kwargs):
    """
	获取赎回日

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"redemptiondate",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getRepurchaseDate(security:list,*args,**kwargs):
    """
	获取回售日

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"repurchasedate",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getClauseCallOptionRedemptionPrice(security:list,*args,**kwargs):
    """
	获取赎回价格

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"clause_calloption_redemptionprice",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getClauseCallOptionRedemptionMemo(security:list,*args,**kwargs):
    """
	获取赎回价格说明

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"clause_calloption_redemptionmemo",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getClausePutOptionResellingPrice(security:list,*args,**kwargs):
    """
	获取回售价格

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"clause_putoption_resellingprice",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getClausePutOptionResellingPriceExplainAtion(security:list,*args,**kwargs):
    """
	获取回售价格说明

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"clause_putoption_resellingpriceexplaination",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getClausePutOptionAdditionalPriceMemo(security:list,*args,**kwargs):
    """
	获取附加回售价格说明

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"clause_putoption_additionalpricememo",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPutCode(security:list,*args,**kwargs):
    """
	获取回售代码

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"putcode",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getRepurchaseBeginDate(security:list,*args,**kwargs):
    """
	获取回售登记起始日

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"repurchasebegindate",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getRepurchaseEnddate(security:list,*args,**kwargs):
    """
	获取回售登记截止日

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"repurchaseenddate",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFunDarRialDate(security:list,*args,**kwargs):
    """
	获取行权资金到账日

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fundarrialdate",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getCouponAdjMax(security:list,*args,**kwargs):
    """
	获取票面利率调整上限

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"couponadj_max",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getCouponAdjMin(security:list,*args,**kwargs):
    """
	获取票面利率调整下限

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"couponadj_min",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getClauseCallOptionRecordDate(security:list,*args,**kwargs):
    """
	获取赎回登记日

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"clause_calloption_recorddate",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getAgencyGuarantor(security:list,*args,**kwargs):
    """
	获取担保人

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"agency_guarantor",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getRateRateGuarantor(security:list,*args,**kwargs):
    """
	获取担保人评级

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"rate_rateguarantor",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getRateFwdGuarantor(security:list,*args,**kwargs):
    """
	获取担保人评级展望

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"rate_fwdguarantor",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getRateChNgGuarantor(security:list,*args,**kwargs):
    """
	获取担保人评级变动方向

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"rate_chngguarantor",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getRateAgencyGuarantor(security:list,*args,**kwargs):
    """
	获取担保人评级评级机构

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"rate_agencyguarantor",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getAgencyReGuarantor(security:list,*args,**kwargs):
    """
	获取再担保人

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"agency_reguarantor",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getRateBeginGuarantor(security:list,*args,**kwargs):
    """
	获取发行时担保人评级

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"rate_beginguarantor",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getAgencyGrNtType(security:list,*args,**kwargs):
    """
	获取担保方式

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"agency_grnttype",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getGuarTerm(security:list,*args,**kwargs):
    """
	获取担保期限

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"guarterm",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getGuarRange(security:list,*args,**kwargs):
    """
	获取担保范围

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"guarrange",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getAgencyGrNtRange(security:list,*args,**kwargs):
    """
	获取担保条款文字

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"agency_grntrange",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getCounterGuar(security:list,*args,**kwargs):
    """
	获取反担保情况

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"counterguar",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getCvnTPerHundred(security:list,*args,**kwargs):
    """
	获取标准券折算金额(每百元面值)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"cvntperhundred",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getCollateralCode(security:list,*args,**kwargs):
    """
	获取质押券代码

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"collateralcode",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getCollateralName(security:list,*args,**kwargs):
    """
	获取质押券简称

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"collateralname",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundPledGableOrNot(security:list,*args,**kwargs):
    """
	获取是否可质押

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_pledgableornot",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getRateOfStdBndCsi(security:list,*args,**kwargs):
    """
	获取报价式回购折算率(中证指数)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"rateofstdbndcsi",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getClauseInterest5(security:list,*args,**kwargs):
    """
	获取是否随存款利率调整

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"clause_interest_5",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getClauseInterest8(security:list,*args,**kwargs):
    """
	获取是否有利息补偿

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"clause_interest_8",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getClauseInterestCompensationInterest(security:list,*args,**kwargs):
    """
	获取补偿利率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"clause_interest_compensationinterest",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getClauseCompensationInterest(security:list,*args,**kwargs):
    """
	获取补偿利率(公布)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"clause_compensationinterest",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getClauseProcessModeInterest(security:list,*args,**kwargs):
    """
	获取利息处理方式

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"clause_processmodeinterest",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getUnderlyingCode(security:list,*args,**kwargs):
    """
	获取正股代码

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"underlyingcode",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getUnderlyingName(security:list,*args,**kwargs):
    """
	获取正股简称

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"underlyingname",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getClauseConversion2RelativeSwapShareMonth(security:list,*args,**kwargs):
    """
	获取相对转股期

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"clause_conversion_2_relativeswapsharemonth",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getClauseConversion2SwapShareStartDate(security:list,*args,**kwargs):
    """
	获取自愿转股起始日期

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"clause_conversion_2_swapsharestartdate",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getClauseConversion2SwapShareEnddate(security:list,*args,**kwargs):
    """
	获取自愿转股终止日期

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"clause_conversion_2_swapshareenddate",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getClauseConversion2IsForced(security:list,*args,**kwargs):
    """
	获取是否强制转股

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"clause_conversion_2_isforced",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getClauseConversion2ForceConvertDate(security:list,*args,**kwargs):
    """
	获取强制转股日

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"clause_conversion_2_forceconvertdate",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getClauseConversion2ForceConvertPrice(security:list,*args,**kwargs):
    """
	获取强制转股价格

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"clause_conversion_2_forceconvertprice",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getClauseConversion2SwapSharePrice(security:list,*args,**kwargs):
    """
	获取转股价格

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"clause_conversion2_swapshareprice",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getClauseConversionCode(security:list,*args,**kwargs):
    """
	获取转股代码

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"clause_conversion_code",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getClauseConversion2ConversionProportion(security:list,*args,**kwargs):
    """
	获取转换比例

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"clause_conversion2_conversionproportion",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getClauseConversion2BondLot(security:list,*args,**kwargs):
    """
	获取未转股余额

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"clause_conversion2_bondlot",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getClauseConversion2BondProportion(security:list,*args,**kwargs):
    """
	获取未转股比例

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"clause_conversion2_bondproportion",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getClauseResetItem(security:list,*args,**kwargs):
    """
	获取特别向下修正条款全文

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"clause_reset_item",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getClauseResetIsExitReset(security:list,*args,**kwargs):
    """
	获取是否有特别向下修正条款

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"clause_reset_isexitreset",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getClauseResetResetStartDate(security:list,*args,**kwargs):
    """
	获取特别修正起始时间

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"clause_reset_resetstartdate",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getClauseResetResetPeriodEnddate(security:list,*args,**kwargs):
    """
	获取特别修正结束时间

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"clause_reset_resetperiodenddate",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getClauseResetResetMaxTimespan(security:list,*args,**kwargs):
    """
	获取重设触发计算最大时间区间

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"clause_reset_resetmaxtimespan",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getClauseResetResetTimespan(security:list,*args,**kwargs):
    """
	获取重设触发计算时间区间

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"clause_reset_resettimespan",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getClauseResetResetTriggerRatio(security:list,*args,**kwargs):
    """
	获取触发比例

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"clause_reset_resettriggerratio",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getClauseCallOptionTriggerProportion(security:list,*args,**kwargs):
    """
	获取赎回触发比例

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"clause_calloption_triggerproportion",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getClausePutOptionRedeemTriggerProportion(security:list,*args,**kwargs):
    """
	获取回售触发比例

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"clause_putoption_redeem_triggerproportion",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getClauseResetResetRange(security:list,*args,**kwargs):
    """
	获取特别修正幅度

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"clause_reset_resetrange",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getClauseResetStockPriceLowestLimit(security:list,*args,**kwargs):
    """
	获取修正价格底线说明

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"clause_reset_stockpricelowestlimit",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getClauseResetResetTimesLimit(security:list,*args,**kwargs):
    """
	获取修正次数限制

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"clause_reset_resettimeslimit",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getClauseResetTimePointClause(security:list,*args,**kwargs):
    """
	获取时点修正条款全文

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"clause_reset_timepointclause",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getClauseCallOptionRelativeCallOptionPeriod(security:list,*args,**kwargs):
    """
	获取相对赎回期

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"clause_calloption_relativecalloptionperiod",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getClauseCallOptionRedemptionTimesPerYear(security:list,*args,**kwargs):
    """
	获取每年可赎回次数

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"clause_calloption_redemptiontimesperyear",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getClauseCallOptionConditionalRedeemStartDate(security:list,*args,**kwargs):
    """
	获取条件赎回起始日期

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"clause_calloption_conditionalredeemstartdate",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getClauseCallOptionConditionalRedeemEnddate(security:list,*args,**kwargs):
    """
	获取条件赎回截止日期

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"clause_calloption_conditionalredeemenddate",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getClauseCallOptionRedeemMaxSpan(security:list,*args,**kwargs):
    """
	获取赎回触发计算最大时间区间

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"clause_calloption_redeemmaxspan",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getClauseCallOptionRedeemSpan(security:list,*args,**kwargs):
    """
	获取赎回触发计算时间区间

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"clause_calloption_redeemspan",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getClausePutOptionInterestDisposing(security:list,*args,**kwargs):
    """
	获取利息处理

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"clause_putoption_interestdisposing",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getClauseCallOptionTimeRedemptionTimes(security:list,*args,**kwargs):
    """
	获取时点赎回数

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"clause_calloption_timeredemptiontimes",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getConditionalCallPrice(security:list,*args,**kwargs):
    """
	获取有条件赎回价

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"conditionalcallprice",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getMaturityCallPrice(security:list,*args,**kwargs):
    """
	获取到期赎回价

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"maturitycallprice",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getClauseCallOptionTriggerPrice(security:list,*args,**kwargs):
    """
	获取赎回触发价

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"clause_calloption_triggerprice",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getClauseCallOptionNoticeDate(security:list,*args,**kwargs):
    """
	获取赎回公告日

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"clause_calloption_noticedate",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getClausePutOptionPutBackPeriodObS(security:list,*args,**kwargs):
    """
	获取相对回售期

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"clause_putoption_putbackperiodobs",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getClausePutOptionConditionalPutBackStartEnddate(security:list,*args,**kwargs):
    """
	获取条件回售起始日期

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"clause_putoption_conditionalputbackstartenddate",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getClausePutOptionPutBackStartDate(security:list,*args,**kwargs):
    """
	获取无条件回售起始日期

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"clause_putoption_putbackstartdate",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getClausePutOptionConditionalPutBackEnddate(security:list,*args,**kwargs):
    """
	获取条件回售截止日期

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"clause_putoption_conditionalputbackenddate",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getClausePutOptionPutBackTriggerMaxSpan(security:list,*args,**kwargs):
    """
	获取回售触发计算最大时间区间

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"clause_putoption_putbacktriggermaxspan",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getClausePutOptionPutBackTriggerSpan(security:list,*args,**kwargs):
    """
	获取回售触发计算时间区间

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"clause_putoption_putbacktriggerspan",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getClausePutOptionPutBackTimesPerYear(security:list,*args,**kwargs):
    """
	获取每年回售次数

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"clause_putoption_putbacktimesperyear",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getClausePutOptionPutBackPeriod(security:list,*args,**kwargs):
    """
	获取无条件回售期

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"clause_putoption_putbackperiod",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getClausePutOptionPutBackEnddate(security:list,*args,**kwargs):
    """
	获取无条件回售结束日期

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"clause_putoption_putbackenddate",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getClausePutOptionPutBackPrice(security:list,*args,**kwargs):
    """
	获取无条件回售价

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"clause_putoption_putbackprice",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getClausePutOptionTimePutBackTimes(security:list,*args,**kwargs):
    """
	获取时点回售数

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"clause_putoption_timeputbacktimes",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getClausePutOptionPutBackAdditionalCondition(security:list,*args,**kwargs):
    """
	获取附加回售条件

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"clause_putoption_putbackadditionalcondition",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getConditionalPutPrice(security:list,*args,**kwargs):
    """
	获取有条件回售价

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"conditionalputprice",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getClausePutOptionTriggerPrice(security:list,*args,**kwargs):
    """
	获取回售触发价

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"clause_putoption_triggerprice",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getClausePutOptionNoticeDate(security:list,*args,**kwargs):
    """
	获取回售公告日

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"clause_putoption_noticedate",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getCreditRating(security:list,*args,**kwargs):
    """
	获取发行时债项评级

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"creditrating",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIssuerRating(security:list,*args,**kwargs):
    """
	获取发行时主体评级

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"issuer_rating",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIssuerRatingOutlook(security:list,*args,**kwargs):
    """
	获取发行时主体评级展望

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"issuerratingoutlook",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getRateCreditRatingAgency(security:list,*args,**kwargs):
    """
	获取发行人委托评级机构

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"rate_creditratingagency",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIsSurerCreditRatingCompany(security:list,*args,**kwargs):
    """
	获取发债主体评级机构

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"issurercreditratingcompany",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getAmount(security:list,*args,**kwargs):
    """
	获取最新债项评级

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"amount",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getRateLatest(security:list,*args,**kwargs):
    """
	获取最新债项评级日期

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"rate_latest",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getRateLatest1(security:list,*args,**kwargs):
    """
	获取最新债项评级日期(指定机构)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"rate_latest1",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getRateChangesOfRating(security:list,*args,**kwargs):
    """
	获取最新债项评级变动方向

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"rate_changesofrating",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getRateStyle(security:list,*args,**kwargs):
    """
	获取最新债项评级评级类型

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"rate_style",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getLowestIsSurerCreditRating(security:list,*args,**kwargs):
    """
	获取发行人最新最低评级

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"lowestissurercreditrating",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getRateRateBond(security:list,*args,**kwargs):
    """
	获取债项评级

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"rate_ratebond",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getRateChNgBond(security:list,*args,**kwargs):
    """
	获取债项评级变动方向

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"rate_chngbond",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getRateAgencyBond(security:list,*args,**kwargs):
    """
	获取债项评级机构

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"rate_agencybond",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getRateFormer(security:list,*args,**kwargs):
    """
	获取历史债项评级

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"rate_former",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getInStYyBondRating(security:list,*args,**kwargs):
    """
	获取(废弃)债项评级(YY)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"inst_yybondrating",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getLatestIsSurerCreditRating2(security:list,*args,**kwargs):
    """
	获取主体评级

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"latestissurercreditrating2",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getRateFwdIssuer(security:list,*args,**kwargs):
    """
	获取主体评级展望

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"rate_fwdissuer",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getRateChNgIssuer(security:list,*args,**kwargs):
    """
	获取主体评级变动方向

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"rate_chngissuer",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getRateAgencyIssuer(security:list,*args,**kwargs):
    """
	获取主体评级评级机构

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"rate_agencyissuer",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getInStYyIssuerRating(security:list,*args,**kwargs):
    """
	获取主体评级(YY)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"inst_yyissuerrating",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getInStYyIssuerRatingHis(security:list,*args,**kwargs):
    """
	获取主体评级历史(YY)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"inst_yyissuerratinghis",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getRateIssuer(security:list,*args,**kwargs):
    """
	获取指定日主体评级

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"rate_issuer",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getRateIssuerFormer(security:list,*args,**kwargs):
    """
	获取发债主体历史信用等级

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"rate_issuerformer",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getCreditLine(security:list,*args,**kwargs):
    """
	获取最新授信额度

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"credit_line",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getCreditLineUsed(security:list,*args,**kwargs):
    """
	获取最新已使用授信额度

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"credit_lineused",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getCreditLineUnused(security:list,*args,**kwargs):
    """
	获取最新未使用授信额度

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"credit_lineunused",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getCreditLineUsed2(security:list,*args,**kwargs):
    """
	获取历史已使用授信额度

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"credit_lineused2",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getCreditFormerLine(security:list,*args,**kwargs):
    """
	获取历史授信额度

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"credit_formerline",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getCreditLineDate(security:list,*args,**kwargs):
    """
	获取最新授信日期

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"credit_linedate",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getGuarLatestBalance(security:list,*args,**kwargs):
    """
	获取最新担保余额

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"guar_latestbalance",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getGuarLatestInwards(security:list,*args,**kwargs):
    """
	获取最新对内担保余额

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"guar_latestinwards",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getGuarLatestOutwards(security:list,*args,**kwargs):
    """
	获取最新对外担保余额

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"guar_latestoutwards",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getGuarFormerBalance(security:list,*args,**kwargs):
    """
	获取历史担保余额

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"guar_formerbalance",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getGuarFormerInwards(security:list,*args,**kwargs):
    """
	获取对内担保余额

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"guar_formerinwards",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getGuarFormerOutwards(security:list,*args,**kwargs):
    """
	获取对外担保余额

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"guar_formeroutwards",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getDCmUnuEsDAmount(security:list,*args,**kwargs):
    """
	获取实际可用剩余额度

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"dcm_unuesdamount",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getDCmUeSdAmount(security:list,*args,**kwargs):
    """
	获取已使用注册额度

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"dcm_uesdamount",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getDCmFirstIssueEnddate(security:list,*args,**kwargs):
    """
	获取首期发行截止日

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"dcm_firstissueenddate",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getDCmMeetingData(security:list,*args,**kwargs):
    """
	获取未使用注册会议日期

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"dcm_meetingdata",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getDCmExpirationData(security:list,*args,**kwargs):
    """
	获取未使用额度有效期

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"dcm_expirationdata",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getDCmNumber(security:list,*args,**kwargs):
    """
	获取最新注册文件编号

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"dcm_number",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getDCmUnderwriter(security:list,*args,**kwargs):
    """
	获取未使用额度主承销商

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"dcm_underwriter",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getDCmAcCumAmount(security:list,*args,**kwargs):
    """
	获取历史累计注册额度

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"dcm_accumamount",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFinaTotalAmount2(security:list,*args,**kwargs):
    """
	获取区间发行债券总额

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fina_totalamount2",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFinaTotalNumber(security:list,*args,**kwargs):
    """
	获取区间发行债券数目

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fina_totalnumber",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFinaRemainingNumber(security:list,*args,**kwargs):
    """
	获取存量债券数目

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fina_remainingnumber",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundInfoName(security:list,*args,**kwargs):
    """
	获取基金简称

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_info_name",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getNameOfficial(security:list,*args,**kwargs):
    """
	获取基金简称(官方)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"name_official",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundFullName(security:list,*args,**kwargs):
    """
	获取基金全称

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_fullname",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundFullNameEn(security:list,*args,**kwargs):
    """
	获取基金全称(英文)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_fullnameen",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundExchangeShortname(security:list,*args,**kwargs):
    """
	获取基金场内简称

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_exchangeshortname",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundExchangeShortnameExtend(security:list,*args,**kwargs):
    """
	获取基金扩位场内简称

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_exchangeshortnameextend",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundIssuerShortname(security:list,*args,**kwargs):
    """
	获取发行机构自编简称

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_issuershortname",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundExistingYear(security:list,*args,**kwargs):
    """
	获取成立年限

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_existingyear",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundMinHoldingPeriod(security:list,*args,**kwargs):
    """
	获取基金最短持有期

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_minholdingperiod",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundPtMYear(security:list,*args,**kwargs):
    """
	获取基金存续期

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_ptmyear",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundPtMDay(security:list,*args,**kwargs):
    """
	获取剩余存续期

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_ptmday",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundBenchmark(security:list,*args,**kwargs):
    """
	获取业绩比较基准

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_benchmark",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundChangeOfBenchmark(security:list,*args,**kwargs):
    """
	获取业绩比较基准变更说明

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_changeofbenchmark",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getBenchReturn(security:list,*args,**kwargs):
    """
	获取业绩比较基准增长率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"bench_return",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getNavBenchReturn(security:list,*args,**kwargs):
    """
	获取报告期业绩比较基准增长率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"NAV_benchreturn",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getNavBenchStdDev(security:list,*args,**kwargs):
    """
	获取报告期业绩比较基准增长率标准差

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"NAV_benchstddev",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getQAnalBenchReturn(security:list,*args,**kwargs):
    """
	获取单季度.业绩比较基准收益率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"qanal_benchreturn",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getQAnalStdBenchReturn(security:list,*args,**kwargs):
    """
	获取单季度.业绩比较基准收益率标准差

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"qanal_stdbenchreturn",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundBenchIndexCode(security:list,*args,**kwargs):
    """
	获取基准指数代码

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_benchindexcode",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundInvestObject(security:list,*args,**kwargs):
    """
	获取投资目标

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_investobject",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundInvestScope(security:list,*args,**kwargs):
    """
	获取投资范围

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_investscope",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundInvestmentProportion(security:list,*args,**kwargs):
    """
	获取投资品种比例限制

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_investmentproportion",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundHkScInvestmentProportion(security:list,*args,**kwargs):
    """
	获取港股通股票投资比例说明

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_hkscinvestmentproportion",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundInvestConception(security:list,*args,**kwargs):
    """
	获取投资理念

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_investconception",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundInvestmentRegion(security:list,*args,**kwargs):
    """
	获取投资区域

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_investmentregion",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundInvestingRegionDescription(security:list,*args,**kwargs):
    """
	获取主要投资区域说明

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_investingregiondescription",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundParValue(security:list,*args,**kwargs):
    """
	获取面值

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_parvalue",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundInitial(security:list,*args,**kwargs):
    """
	获取是否初始基金

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_initial",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundStructuredFundOrNot(security:list,*args,**kwargs):
    """
	获取是否分级基金

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_structuredfundornot",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundReGulOpenFundOrNot(security:list,*args,**kwargs):
    """
	获取是否定期开放基金

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_regulopenfundornot",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundSidePocketFundOrNot(security:list,*args,**kwargs):
    """
	获取是否使用侧袋机制

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_sidepocketfundornot",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundExceptionStatus(security:list,*args,**kwargs):
    """
	获取产品异常状态

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_exceptionstatus",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundOperatePeriodCls(security:list,*args,**kwargs):
    """
	获取封闭运作期

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_operateperiod_cls",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getExpectedYield(security:list,*args,**kwargs):
    """
	获取预期收益率(文字)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"expectedyield",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundFundTransition(security:list,*args,**kwargs):
    """
	获取基金转型说明

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_fundtransition",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundValuationMethod(security:list,*args,**kwargs):
    """
	获取基金估值方法

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_valuationmethod",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundRiskReturnCharacters(security:list,*args,**kwargs):
    """
	获取风险收益特征

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_riskreturn_characters",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getMarketRisk(security:list,*args,**kwargs):
    """
	获取市场风险提示

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"marketrisk",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getManagementRisk(security:list,*args,**kwargs):
    """
	获取管理风险提示

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"managementrisk",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getTechnicalRisk(security:list,*args,**kwargs):
    """
	获取技术风险提示

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"technicalrisk",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getRedemptionRisk(security:list,*args,**kwargs):
    """
	获取赎回风险提示

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"redemptionrisk",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getOtherRisks(security:list,*args,**kwargs):
    """
	获取其他风险提示

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"otherrisks",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundFrontendCode(security:list,*args,**kwargs):
    """
	获取基金前端代码

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_frontendcode",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundBackendCode(security:list,*args,**kwargs):
    """
	获取基金后端代码

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_backendcode",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundInitialCode(security:list,*args,**kwargs):
    """
	获取基金初始代码

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_initialcode",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundRelatedCode(security:list,*args,**kwargs):
    """
	获取关联基金代码

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_relatedcode",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundAMacCode(security:list,*args,**kwargs):
    """
	获取基金业协会编码

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_AMACcode",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundBWMpRecordCode(security:list,*args,**kwargs):
    """
	获取理财产品登记编码

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_bwmp_recordcode",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundIssuerCode(security:list,*args,**kwargs):
    """
	获取发行机构自编代码

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_issuercode",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundExchangeCode(security:list,*args,**kwargs):
    """
	获取理财产品交易所代码

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_exchangecode",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundPeQuotationCode(security:list,*args,**kwargs):
    """
	获取机构间私募产品报价系统编码

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_pequotationcode",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundSetUpdate(security:list,*args,**kwargs):
    """
	获取基金成立日

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_setupdate",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundMaturityDate2(security:list,*args,**kwargs):
    """
	获取基金到期日

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_maturitydate_2",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundDateSuspension(security:list,*args,**kwargs):
    """
	获取基金暂停运作日

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_date_suspension",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundDateResumption(security:list,*args,**kwargs):
    """
	获取基金恢复运作日

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_date_resumption",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundCuStStartDate(security:list,*args,**kwargs):
    """
	获取开始托管日期

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_custstartdate",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundCusTendDate(security:list,*args,**kwargs):
    """
	获取托管结束日期

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_custenddate",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundRecognitionDate(security:list,*args,**kwargs):
    """
	获取互认基金批复日期

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_recognitiondate",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundExpectedEndingDay(security:list,*args,**kwargs):
    """
	获取预计封闭期结束日

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_expectedendingday",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundExpectedOpenDay(security:list,*args,**kwargs):
    """
	获取预计下期开放日

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_expectedopenday",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundStartDateOfClosure(security:list,*args,**kwargs):
    """
	获取定开基金封闭起始日

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_startdateofclosure",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundLastOpenDay(security:list,*args,**kwargs):
    """
	获取定开基金上一开放日

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_lastopenday",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundOpenDays(security:list,*args,**kwargs):
    """
	获取定开基金开放日(支持历史)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_opendays",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundNumOfOpenDays(security:list,*args,**kwargs):
    """
	获取定开基金已开放次数

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_numofopendays",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getListDataDate(security:list,*args,**kwargs):
    """
	获取上市公告数据截止日期

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"listdatadate",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundMGrComp(security:list,*args,**kwargs):
    """
	获取基金管理人

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_mgrcomp",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundCorpFundManagementCompany(security:list,*args,**kwargs):
    """
	获取基金管理人简称

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_corp_fundmanagementcompany",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundCorpNameEng(security:list,*args,**kwargs):
    """
	获取基金管理人英文名称

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_corpnameeng",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundCorpChairman(security:list,*args,**kwargs):
    """
	获取基金管理人法人代表

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_corpchairman",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundCorpPhone(security:list,*args,**kwargs):
    """
	获取基金管理人电话

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_corpphone",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundCorpFax(security:list,*args,**kwargs):
    """
	获取基金管理人传真

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_corpfax",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundCorpEmail(security:list,*args,**kwargs):
    """
	获取基金管理人电子邮箱

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_corpemail",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundCorpWebsite(security:list,*args,**kwargs):
    """
	获取基金管理人主页

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_corpwebsite",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPrtNonMoneyNetAssets(security:list,*args,**kwargs):
    """
	获取基金管理人资产净值合计(非货币)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"prt_nonmoneynetassets",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPrtFundCoTotalNetAssets(security:list,*args,**kwargs):
    """
	获取基金管理人资产净值合计

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"prt_fundcototalnetassets",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPrtFundCoTotalNetAssetsRanking(security:list,*args,**kwargs):
    """
	获取基金管理人资产净值合计排名

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"prt_fundcototalnetassetsranking",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPrtFundCoTnaChangeRatio(security:list,*args,**kwargs):
    """
	获取基金管理人资产净值合计变动率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"prt_fundcotnachangeratio",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundCustodianBank(security:list,*args,**kwargs):
    """
	获取基金托管人

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_custodianbank",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIssueRegistrar(security:list,*args,**kwargs):
    """
	获取基金注册与过户登记人

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"issue_registrar",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getAgencyFAdvisor(security:list,*args,**kwargs):
    """
	获取财务顾问

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"agency_fadvisor",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getStmNoteSec1504(security:list,*args,**kwargs):
    """
	获取手续费及佣金收入:财务顾问业务

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"stmnote_sec_1504",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getStmNoteSec1524(security:list,*args,**kwargs):
    """
	获取手续费及佣金净收入:财务顾问业务

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"stmnote_sec_1524",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundWmIssuer(security:list,*args,**kwargs):
    """
	获取银行理财发行人

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_wmissuer",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundForeignInvestmentAdvisor(security:list,*args,**kwargs):
    """
	获取境外投资顾问

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_foreigninvestmentadvisor",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundForeignCustodian(security:list,*args,**kwargs):
    """
	获取境外托管人

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_foreigncustodian",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundCounselor(security:list,*args,**kwargs):
    """
	获取律师事务所

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_counselor",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundPrimaryDealers(security:list,*args,**kwargs):
    """
	获取一级交易商

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_primarydealers",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundType(security:list,*args,**kwargs):
    """
	获取基金类型

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_type",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundFirstInvestType(security:list,*args,**kwargs):
    """
	获取投资类型(一级分类)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_firstinvesttype",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundInvestType(security:list,*args,**kwargs):
    """
	获取投资类型(二级分类)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_investtype",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundInvestType2(security:list,*args,**kwargs):
    """
	获取投资类型

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_investtype2",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundInvestTypeAnytime(security:list,*args,**kwargs):
    """
	获取投资类型(支持历史)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_investtype_anytime",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundInvestTypeEng(security:list,*args,**kwargs):
    """
	获取投资类型(英文)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_investtypeeng",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundRiskLevel(security:list,*args,**kwargs):
    """
	获取基金风险等级

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_risklevel",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundRiskLevelFiling(security:list,*args,**kwargs):
    """
	获取基金风险等级(公告口径)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_risklevelfiling",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundSMfType2(security:list,*args,**kwargs):
    """
	获取基金分级类型

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_smftype2",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundSimilarFundNo(security:list,*args,**kwargs):
    """
	获取同类基金数量

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_similarfundno",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundThemeType(security:list,*args,**kwargs):
    """
	获取所属主题基金类别

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_themetype",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundThemeTypeConcept(security:list,*args,**kwargs):
    """
	获取所属主题基金类别(Wind概念)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_themetype_concept",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundThemeTypeIndustry(security:list,*args,**kwargs):
    """
	获取所属主题基金类别(Wind行业)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_themetype_industry",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundThemeTypeIndex(security:list,*args,**kwargs):
    """
	获取所属主题基金类别(Wind股票指数)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_themetype_index",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundManagementFeeRatio(security:list,*args,**kwargs):
    """
	获取管理费率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_managementfeeratio",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundManagementFeeRatio2(security:list,*args,**kwargs):
    """
	获取管理费率(支持历史)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_managementfeeratio2",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundFloatingMgNtFeedEScrip(security:list,*args,**kwargs):
    """
	获取浮动管理费率说明

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_floatingmgntfeedescrip",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundTrusteeMgNtFee(security:list,*args,**kwargs):
    """
	获取受托人固定管理费率(信托)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_trusteemgntfee",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundInvAdviserMgNtFee(security:list,*args,**kwargs):
    """
	获取投资顾问固定管理费率(信托)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_invadvisermgntfee",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundFloatingMgNtFeeOrNot(security:list,*args,**kwargs):
    """
	获取是否收取浮动管理费

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_floatingmgntfeeornot",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundCustodianFeeRatio(security:list,*args,**kwargs):
    """
	获取托管费率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_custodianfeeratio",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundCustodianFeeRatio2(security:list,*args,**kwargs):
    """
	获取托管费率(支持历史)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_custodianfeeratio2",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundSaleFeeRatio(security:list,*args,**kwargs):
    """
	获取销售服务费率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_salefeeratio",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundSaleFeeRatio2(security:list,*args,**kwargs):
    """
	获取销售服务费率(支持历史)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_salefeeratio2",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundPurchaseFeeRatio(security:list,*args,**kwargs):
    """
	获取最高申购费率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_purchasefeeratio",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundRedemptionFeeRatio(security:list,*args,**kwargs):
    """
	获取最高赎回费率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_redemptionfeeratio",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundSubscriptionFee(security:list,*args,**kwargs):
    """
	获取认购费率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_subscriptionfee",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundSubscriptionFee2(security:list,*args,**kwargs):
    """
	获取认购费率(支持历史)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_subscriptionfee2",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundPurchaseFee(security:list,*args,**kwargs):
    """
	获取申购费率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_purchasefee",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundPurchaseFee2(security:list,*args,**kwargs):
    """
	获取申购费率(支持历史)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_purchasefee2",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundPChRedMPChMaxFee(security:list,*args,**kwargs):
    """
	获取申购费率上限

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_pchredm_pchmaxfee",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundRedemptionFee(security:list,*args,**kwargs):
    """
	获取赎回费率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_redemptionfee",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundRedemptionFee2(security:list,*args,**kwargs):
    """
	获取赎回费率(支持历史)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_redemptionfee2",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundPChRedMMaxRedMFee(security:list,*args,**kwargs):
    """
	获取赎回费率上限

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_pchredm_maxredmfee",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundIndexUsageFeeRatio(security:list,*args,**kwargs):
    """
	获取指数使用费率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_indexusagefeeratio",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundPurchaseAndRedemptionAbbreviation(security:list,*args,**kwargs):
    """
	获取申购赎回简称

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_purchaseandredemptionabbreviation",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundDQStatus(security:list,*args,**kwargs):
    """
	获取申购赎回状态

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_dq_status",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundPcHmStatus(security:list,*args,**kwargs):
    """
	获取申购状态

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_pchmstatus",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundRedMStatus(security:list,*args,**kwargs):
    """
	获取赎回状态

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_redmstatus",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundPChRedMPChStartDate(security:list,*args,**kwargs):
    """
	获取申购起始日

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_pchredm_pchstartdate",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIpoOpStartDate(security:list,*args,**kwargs):
    """
	获取网下申购起始日期

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"ipo_op_startdate",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundPChRedMLargePChMaxAmt(security:list,*args,**kwargs):
    """
	获取单日大额申购限额

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_pchredm_largepchmaxamt",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundPChRedMPcHmInAmt(security:list,*args,**kwargs):
    """
	获取申购金额下限(场外)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_pchredm_pchminamt",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundPChRedMPcHmInAmtFloor(security:list,*args,**kwargs):
    """
	获取申购金额下限(场内)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_pchredm_pchminamt_floor",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundRedMStartDate(security:list,*args,**kwargs):
    """
	获取赎回起始日

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_redmstartdate",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundPChRedMRedMmInAmt(security:list,*args,**kwargs):
    """
	获取单笔赎回份额下限

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_pchredm_redmminamt",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundPChConfirmDate(security:list,*args,**kwargs):
    """
	获取申购确认日

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_pchconfirmdate",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundRedMConfirmDate(security:list,*args,**kwargs):
    """
	获取赎回确认日

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_redmconfirmdate",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundRedMarriAlDate(security:list,*args,**kwargs):
    """
	获取赎回划款日

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_redmarrialdate",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundCorpFundNo(security:list,*args,**kwargs):
    """
	获取旗下基金数

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_corp_fundno",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundCorpFiveStarFundsProp(security:list,*args,**kwargs):
    """
	获取五星基金占比

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_corp_fivestarfundsprop",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundCorpFourStarFundsProp(security:list,*args,**kwargs):
    """
	获取四星基金占比

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_corp_fourstarfundsprop",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundCorpTeamStability(security:list,*args,**kwargs):
    """
	获取团队稳定性

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_corp_teamstability",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundTrackIndexCode(security:list,*args,**kwargs):
    """
	获取跟踪指数代码

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_trackindexcode",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundTrackIndexName(security:list,*args,**kwargs):
    """
	获取跟踪指数名称

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_trackindexname",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundTrackDeviationThreshold(security:list,*args,**kwargs):
    """
	获取日均跟踪偏离度阈值(业绩基准)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_trackdeviation_threshold",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundTrackErrorThreshold(security:list,*args,**kwargs):
    """
	获取年化跟踪误差阈值(业绩基准)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_trackerror_threshold",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundSMfType(security:list,*args,**kwargs):
    """
	获取分级基金类别

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_smftype",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundSMfCode(security:list,*args,**kwargs):
    """
	获取分级基金母基金代码

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_smfcode",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundSMfaCode(security:list,*args,**kwargs):
    """
	获取分级基金优先级代码

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_smfacode",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundSmFbCode(security:list,*args,**kwargs):
    """
	获取分级基金普通级代码

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_smfbcode",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundSplitRatio(security:list,*args,**kwargs):
    """
	获取拆分比率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_splitratio",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundSubShareProportion(security:list,*args,**kwargs):
    """
	获取分级份额占比

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_subshareproportion",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundInitialLever(security:list,*args,**kwargs):
    """
	获取初始杠杆

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_initiallever",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundAAyeIlDInfo(security:list,*args,**kwargs):
    """
	获取约定年收益率表达式

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_aayeildinfo",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundPairConversion(security:list,*args,**kwargs):
    """
	获取是否配对转换

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_pairconversion",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundDiscountPeriod(security:list,*args,**kwargs):
    """
	获取定期折算周期

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_discountperiod",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundDiscountMethod(security:list,*args,**kwargs):
    """
	获取定期折算条款

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_discountmethod",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundUpDiscount(security:list,*args,**kwargs):
    """
	获取向上触点折算条款

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_updiscount",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundDownDiscount(security:list,*args,**kwargs):
    """
	获取向下触点折算条款

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_downdiscount",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundGuaranteedCycle(security:list,*args,**kwargs):
    """
	获取保本周期

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_guaranteedcycle",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundGuaranteedCycleStartDate(security:list,*args,**kwargs):
    """
	获取保本周期起始日期

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_guaranteedcycle_startdate",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundGuaranteedCycleEnddate(security:list,*args,**kwargs):
    """
	获取保本周期终止日期

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_guaranteedcycle_enddate",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundGuaranteedFeeRate(security:list,*args,**kwargs):
    """
	获取保本费率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_guaranteedfeerate",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundWarrantOr(security:list,*args,**kwargs):
    """
	获取保证人

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_warrantor",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundWarrantOrIntroduction(security:list,*args,**kwargs):
    """
	获取保证人简介

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_warrantorintroduction",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundGuaranteedTriggerRatio(security:list,*args,**kwargs):
    """
	获取保本触发收益率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_guaranteedtriggerratio",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundGuaranteedTriggerTxt(security:list,*args,**kwargs):
    """
	获取保本触发机制说明

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_guaranteedtriggertxt",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundPlanType(security:list,*args,**kwargs):
    """
	获取计划类型(券商集合理财)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_plantype",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundPerformanceFeeOrNot(security:list,*args,**kwargs):
    """
	获取是否提取业绩报酬(券商集合理财)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_performancefeeornot",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundPerformanceFeeMethod(security:list,*args,**kwargs):
    """
	获取业绩报酬提取方法

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_performancefeemethod",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundMgNtFeeExplain(security:list,*args,**kwargs):
    """
	获取管理费说明

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_mgntfeeexplain",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getTrustType(security:list,*args,**kwargs):
    """
	获取信托类别(信托)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"trust_type",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getTrustInvestField(security:list,*args,**kwargs):
    """
	获取信托投资领域

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"trust_investfield",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getTrustSourceType(security:list,*args,**kwargs):
    """
	获取信托产品类别

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"trust_sourcetype",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundExpectedRateOfReturn(security:list,*args,**kwargs):
    """
	获取预计年收益率(信托)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_expectedrateofreturn",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundStructuredOrNot(security:list,*args,**kwargs):
    """
	获取是否结构化产品(信托)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_structuredornot",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundTrustee(security:list,*args,**kwargs):
    """
	获取受托人(信托)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_trustee",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundSecuritiesBroker(security:list,*args,**kwargs):
    """
	获取证券经纪人(信托)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_securitiesbroker",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundIssuingPlace(security:list,*args,**kwargs):
    """
	获取发行地(信托)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_issuingplace",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundFloatingRateNote(security:list,*args,**kwargs):
    """
	获取浮动收益说明(信托)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_floatingratenote",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundGeneralBeneficialAmount(security:list,*args,**kwargs):
    """
	获取一般受益权金额(信托)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_generalbeneficialamount",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundPriorityBeneficialAmount(security:list,*args,**kwargs):
    """
	获取优先受益权金额(信托)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_prioritybeneficialamount",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundPriorityToGeneral(security:list,*args,**kwargs):
    """
	获取委托资金比(优先/一般)(信托)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_prioritytogeneral",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundIssuedContractAmount(security:list,*args,**kwargs):
    """
	获取发行信托合同总数(信托)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_issuedcontractamount",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getAdvanceCreditDesc(security:list,*args,**kwargs):
    """
	获取信用增级情况

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"advancecredit_desc",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getAnticipateYieldDesc(security:list,*args,**kwargs):
    """
	获取预期收益率说明

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"anticipateyield_desc",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getTrustRelatedFirm(security:list,*args,**kwargs):
    """
	获取信托项目关联企业名称

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"trust_relatedfirm",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundSubStartDate(security:list,*args,**kwargs):
    """
	获取销售起始日期

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_substartdate",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundSubEnddate(security:list,*args,**kwargs):
    """
	获取销售截止日期

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_subenddate",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundTargetScale(security:list,*args,**kwargs):
    """
	获取目标规模

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_targetscale",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundEffSubsCrHoleDerNo(security:list,*args,**kwargs):
    """
	获取有效认购户数

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_effsubscrholederno",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundMinBuyAmount(security:list,*args,**kwargs):
    """
	获取最低参与金额

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_minbuyamount",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundMinAddBuyAmount(security:list,*args,**kwargs):
    """
	获取追加认购最低金额

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_minaddbuyamount",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundManagersBuyAmount(security:list,*args,**kwargs):
    """
	获取管理人参与金额

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_managersbuyamount",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundOpenDayIllUs(security:list,*args,**kwargs):
    """
	获取开放日说明

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_opendayillus",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundCloseDayIllUs(security:list,*args,**kwargs):
    """
	获取封闭期说明

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_closedayillus",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundFirstInvestStrategy(security:list,*args,**kwargs):
    """
	获取投资策略分类(一级)(私募)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_firstinveststrategy",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundSecondInvestStrategy(security:list,*args,**kwargs):
    """
	获取投资策略分类(二级)(私募)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_secondinveststrategy",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIssueChannel(security:list,*args,**kwargs):
    """
	获取产品发行渠道

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"issue_channel",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundInvestmentAdvisor(security:list,*args,**kwargs):
    """
	获取投资顾问

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_investmentadvisor",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getNavUpdateFrequency(security:list,*args,**kwargs):
    """
	获取基金净值更新频率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"NAV_updatefrequency",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getNavUpdateCompleteness(security:list,*args,**kwargs):
    """
	获取基金净值完整度

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"NAV_updatecompleteness",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundManageScaleInterval(security:list,*args,**kwargs):
    """
	获取协会备案管理人在管规模

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_managescaleinterval",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundGuaranteedOrNot(security:list,*args,**kwargs):
    """
	获取是否保本

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_guaranteedornot",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundLcRiskLevel(security:list,*args,**kwargs):
    """
	获取银行理财风险等级(银行)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_lcrisklevel",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundOperationMode(security:list,*args,**kwargs):
    """
	获取产品运作方式

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_operationmode",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundBusinessMode(security:list,*args,**kwargs):
    """
	获取业务模式

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_businessmode",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundReturnStartDate(security:list,*args,**kwargs):
    """
	获取收益起始日

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_returnstartdate",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundReturnEnddate(security:list,*args,**kwargs):
    """
	获取收益终止日

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_returnenddate",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundActualDuration(security:list,*args,**kwargs):
    """
	获取实际运作期限

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_actualduration",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundMaxSubScripAmount(security:list,*args,**kwargs):
    """
	获取委托金额上限

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_maxsubscripamount",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundActualAnnualYield(security:list,*args,**kwargs):
    """
	获取实际年化收益率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_actualannualyield",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundActualMaturityDate(security:list,*args,**kwargs):
    """
	获取实际到期日

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_actualmaturitydate",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundInterestPayMethod(security:list,*args,**kwargs):
    """
	获取付息方式说明

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_interestpaymethod",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundFundArrivalDays(security:list,*args,**kwargs):
    """
	获取资金到账天数

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_fundarrivaldays",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundEarlyTerminationOrNot(security:list,*args,**kwargs):
    """
	获取是否可提前终止

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_earlyterminationornot",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundCNdPreTermination(security:list,*args,**kwargs):
    """
	获取提前终止条件

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_cndpretermination",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundCNdpUrchRedemption(security:list,*args,**kwargs):
    """
	获取申购赎回条件

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_cndpurchredemption",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundUnderlyingTarget(security:list,*args,**kwargs):
    """
	获取收益挂钩标的

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_underlyingtarget",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundMainRisk(security:list,*args,**kwargs):
    """
	获取主要风险点

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_mainrisk",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundReItsType(security:list,*args,**kwargs):
    """
	获取资产类型

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund__reitstype",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundReItsInfo(security:list,*args,**kwargs):
    """
	获取项目介绍

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund__reitsinfo",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundReItsPriceMax(security:list,*args,**kwargs):
    """
	获取询价区间上限

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund__reitspricemax",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundReItsPriceMin(security:list,*args,**kwargs):
    """
	获取询价区间下限

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund__reitspricemin",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundReItsSIsTDate(security:list,*args,**kwargs):
    """
	获取战略发售起始日

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund__reitssistdate",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundReItsSienDate(security:list,*args,**kwargs):
    """
	获取战略发售截止日

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund__reitssiendate",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundReItsSiShareSub(security:list,*args,**kwargs):
    """
	获取战略投资方认购份额

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_reitssisharesub",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundReItsSiShare(security:list,*args,**kwargs):
    """
	获取战略配售份额

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund__reitssishare",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundReItsSiShareRa(security:list,*args,**kwargs):
    """
	获取战略配售份额占比

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund__reitssisharera",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundReItsSiRatio(security:list,*args,**kwargs):
    """
	获取战略投资方认购比例

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_reitssiratio",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundReItsOffStDate(security:list,*args,**kwargs):
    """
	获取网下发售起始日

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund__reitsoffstdate",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundReItsOffendAte(security:list,*args,**kwargs):
    """
	获取网下发售截止日

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund__reitsoffendate",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundReItSoIsHare(security:list,*args,**kwargs):
    """
	获取网下认购份额

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_reitsoishare",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundReItsOffShare(security:list,*args,**kwargs):
    """
	获取网下配售份额

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund__reitsoffshare",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundReItsOffShareRa(security:list,*args,**kwargs):
    """
	获取网下配售份额占比

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund__reitsoffsharera",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundReItSoIRatio(security:list,*args,**kwargs):
    """
	获取网下投资方认购比例

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_reitsoiratio",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundReItsPbsTDate(security:list,*args,**kwargs):
    """
	获取公众发售起始日

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund__reitspbstdate",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundReItsPBenDate(security:list,*args,**kwargs):
    """
	获取公众发售截止日

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund__reitspbendate",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundReItsPiShare(security:list,*args,**kwargs):
    """
	获取公众认购份额

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_reitspishare",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundReItsPbShare(security:list,*args,**kwargs):
    """
	获取公众配售份额

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund__reitspbshare",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundReItsPbShareRa(security:list,*args,**kwargs):
    """
	获取公众配售份额占比

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund__reitspbsharera",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundReItsPiRatio(security:list,*args,**kwargs):
    """
	获取公众投资方认购比例

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_reitspiratio",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundReItsOpRisk(security:list,*args,**kwargs):
    """
	获取项目运营风险

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund__reitsoprisk",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundReItsAsName(security:list,*args,**kwargs):
    """
	获取资产名称

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund__reitsasname",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundReItsLocation(security:list,*args,**kwargs):
    """
	获取资产所在地

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund__reitslocation",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundReItsComName(security:list,*args,**kwargs):
    """
	获取项目公司名称

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund__reitscomname",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundReItsPIs(security:list,*args,**kwargs):
    """
	获取网下机构自营投资账户配售数量

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund__reitspis",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundReItsPim(security:list,*args,**kwargs):
    """
	获取网下机构自营投资账户配售金额

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund__reitspim",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundReItsPir(security:list,*args,**kwargs):
    """
	获取网下机构自营投资账户配售份额占比

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund__reitspir",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundReItsPfs(security:list,*args,**kwargs):
    """
	获取网下私募基金配售数量

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund__reitspfs",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundReItsPFm(security:list,*args,**kwargs):
    """
	获取网下私募基金配售金额

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund__reitspfm",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundReItsPFr(security:list,*args,**kwargs):
    """
	获取网下私募基金配售份额占比

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund__reitspfr",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundReItsIsS(security:list,*args,**kwargs):
    """
	获取网下保险资金投资账户配售数量

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund__reitsiss",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundReItsIsM(security:list,*args,**kwargs):
    """
	获取网下保险资金投资账户配售金额

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund__reitsism",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundReItsIsR(security:list,*args,**kwargs):
    """
	获取网下保险资金投资账户配售份额占比

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund__reitsisr",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundReItsTrs(security:list,*args,**kwargs):
    """
	获取网下集合信托计划配售数量

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund__reitstrs",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundReItsTrm(security:list,*args,**kwargs):
    """
	获取网下集合信托计划配售金额

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund__reitstrm",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundReItsTrR(security:list,*args,**kwargs):
    """
	获取网下集合信托计划配售份额占比

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund__reitstrr",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundReItsScS(security:list,*args,**kwargs):
    """
	获取网下证券公司集合资产管理计划配售数量

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund__reitsscs",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundReItsSCm(security:list,*args,**kwargs):
    """
	获取网下证券公司集合资产管理计划配售金额

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund__reitsscm",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundReItsSCr(security:list,*args,**kwargs):
    """
	获取网下证券公司集合资产管理计划配售份额占比

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund__reitsscr",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundReItsSCss(security:list,*args,**kwargs):
    """
	获取网下证券公司单一资产管理计划配售数量

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund__reitsscss",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundReItsScSm(security:list,*args,**kwargs):
    """
	获取网下证券公司单一资产管理计划配售金额

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund__reitsscsm",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundReItsSCsr(security:list,*args,**kwargs):
    """
	获取网下证券公司单一资产管理计划配售份额占比

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund__reitsscsr",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundReItsLimitedShare(security:list,*args,**kwargs):
    """
	获取限售份额

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_reitslimitedshare",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getYieldCnBd(security:list,*args,**kwargs):
    """
	获取估价收益率(%)(中债)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"yield_cnbd",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getNetCnBd(security:list,*args,**kwargs):
    """
	获取估价净价(中债)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"net_cnbd",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getDirtyCnBd(security:list,*args,**kwargs):
    """
	获取估价全价(中债)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"dirty_cnbd",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPriceCnBd(security:list,*args,**kwargs):
    """
	获取日终估价全价(中债)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"price_cnbd",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getModiDuraCnBd(security:list,*args,**kwargs):
    """
	获取估价修正久期(中债)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"modidura_cnbd",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getMatUCnBd(security:list,*args,**kwargs):
    """
	获取待偿年限(年)(中债)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"matu_cnbd",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getAccruedInterestCnBd(security:list,*args,**kwargs):
    """
	获取应计利息(中债)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"accruedinterest_cnbd",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getAccRIntDayEndCnBd(security:list,*args,**kwargs):
    """
	获取日终应计利息(中债)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"accrint_dayend_cnbd",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getSprDuraCnBd(security:list,*args,**kwargs):
    """
	获取估价利差久期(中债)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"sprdura_cnbd",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getInterestDurationCnBd(security:list,*args,**kwargs):
    """
	获取估价利率久期(中债)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"interestduration_cnbd",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getSpreadYieldCnBd(security:list,*args,**kwargs):
    """
	获取点差收益率(中债)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"spreadyield_cnbd",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getCNvXTyCnBd(security:list,*args,**kwargs):
    """
	获取估价凸性(中债)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"cnvxty_cnbd",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getSPrcNxtCnBd(security:list,*args,**kwargs):
    """
	获取估价利差凸性(中债)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"sprcnxt_cnbd",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getInterestCNvXTyCnBd(security:list,*args,**kwargs):
    """
	获取估价利率凸性(中债)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"interestcnvxty_cnbd",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getMcYieldCnBd(security:list,*args,**kwargs):
    """
	获取加权平均结算收益率(%)(中债)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"mcyield_cnbd",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getMCnetCnBd(security:list,*args,**kwargs):
    """
	获取加权平均结算净价(中债)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"mcnet_cnbd",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getMDirtyCnBd(security:list,*args,**kwargs):
    """
	获取加权平均结算全价(中债)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"mdirty_cnbd",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getRateLatestMirCnBd(security:list,*args,**kwargs):
    """
	获取市场隐含评级(中债)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"rate_latestMIR_cnbd",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getRateHistoricalMirCnBd(security:list,*args,**kwargs):
    """
	获取市场历史隐含评级(中债)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"rate_historicalMIR_cnbd",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getLastDateCnBd(security:list,*args,**kwargs):
    """
	获取最新估值日期(中债)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"lastdate_cnbd",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getExerciseCouponRateCnBd(security:list,*args,**kwargs):
    """
	获取估算的行权后票面利率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"exercisecouponrate_cnbd",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getLatestParCnBd(security:list,*args,**kwargs):
    """
	获取剩余本金(中债)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"latestpar_cnbd",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getYieldCsi1(security:list,*args,**kwargs):
    """
	获取估价收益率(中证指数)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"yield_csi1",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getNetCsi1(security:list,*args,**kwargs):
    """
	获取估价净价(中证指数)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"net_csi1",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getDirtyCsi1(security:list,*args,**kwargs):
    """
	获取估价全价(中证指数)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"dirty_csi1",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getModiDuraCsi1(security:list,*args,**kwargs):
    """
	获取估价修正久期(中证指数)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"modidura_csi1",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getAccruedInterestCsi(security:list,*args,**kwargs):
    """
	获取应计利息(中证指数)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"accruedinterest_csi",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getCNvXTyCsi1(security:list,*args,**kwargs):
    """
	获取估价凸性(中证指数)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"cnvxty_csi1",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getLastDateCsi(security:list,*args,**kwargs):
    """
	获取最新估值日期(中证指数)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"lastdate_csi",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getRateLatestMirCsi(security:list,*args,**kwargs):
    """
	获取隐含评级(中证指数)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"rate_latestMIR_csi",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getRateDefaultCsi(security:list,*args,**kwargs):
    """
	获取隐含违约率(中证指数)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"rate_default_csi",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getEbValCsi(security:list,*args,**kwargs):
    """
	获取可交换债估值(中证指数)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"ebval_csi",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getEbOptionValCsi(security:list,*args,**kwargs):
    """
	获取可交换债期权价值(中证指数)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"eboptionval_csi",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getEbBondPreCsi(security:list,*args,**kwargs):
    """
	获取可交换债纯债溢价率(中证指数)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"ebbondpre_csi",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getEbValYieldCsi(security:list,*args,**kwargs):
    """
	获取可交换债估值收益率(中证指数)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"ebvalyield_csi",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getEbConversionPreCsi(security:list,*args,**kwargs):
    """
	获取可交换债转股溢价率(中证指数)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"ebconversionpre_csi",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getYieldShc(security:list,*args,**kwargs):
    """
	获取估价收益率(上清所)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"yield_shc",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getNetShc(security:list,*args,**kwargs):
    """
	获取估价净价(上清所)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"net_shc",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getDirtyShc(security:list,*args,**kwargs):
    """
	获取估价全价(上清所)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"dirty_shc",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getModiDuraShc(security:list,*args,**kwargs):
    """
	获取估价修正久期(上清所)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"modidura_shc",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getAccruedInterestShc(security:list,*args,**kwargs):
    """
	获取应计利息(上清所)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"accruedinterest_shc",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getCNvXTyShc(security:list,*args,**kwargs):
    """
	获取估价凸性(上清所)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"cnvxty_shc",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getLastDateShc(security:list,*args,**kwargs):
    """
	获取最新估值日期(上清所)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"lastdate_shc",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getDQCloseCnBd(security:list,*args,**kwargs):
    """
	获取指数值(中债)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"dq_close_cnbd",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getDQAmountCnBd(security:list,*args,**kwargs):
    """
	获取现券结算量(中债)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"dq_amount_cnbd",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getAnalCapConvexity(security:list,*args,**kwargs):
    """
	获取平均市值法凸性

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"anal_capconvexity",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getAnalCapDuration(security:list,*args,**kwargs):
    """
	获取平均市值法久期

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"anal_capduration",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getAnalCapYTM(security:list,*args,**kwargs):
    """
	获取平均市值法到期收益率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"anal_capytm",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getAnalCashFlowConvexity(security:list,*args,**kwargs):
    """
	获取平均现金流法凸性

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"anal_cashflowconvexity",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getAnalCashFlowDuration(security:list,*args,**kwargs):
    """
	获取平均现金流法久期

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"anal_cashflowduration",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getAnalCashFlowYTM(security:list,*args,**kwargs):
    """
	获取平均现金流法到期收益率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"anal_cashflowytm",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getAnalIpRatio(security:list,*args,**kwargs):
    """
	获取平均派息率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"anal_ipratio",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getAnalPeriod(security:list,*args,**kwargs):
    """
	获取平均待偿期

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"anal_period",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getAmountFixedIncome(security:list,*args,**kwargs):
    """
	获取上证固收平台成交金额

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"amount_fixedincome",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getBinetBidWt(security:list,*args,**kwargs):
    """
	获取双边买入净价(加权平均)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"binetbid_wt",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getBibiDrTWt(security:list,*args,**kwargs):
    """
	获取双边买入收益率(加权平均)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"bibidrt_wt",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getBinetAskWt(security:list,*args,**kwargs):
    """
	获取双边卖出净价(加权平均)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"binetask_wt",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getBiasKrTWt(security:list,*args,**kwargs):
    """
	获取双边卖出收益率(加权平均)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"biaskrt_wt",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getBinetBidBst(security:list,*args,**kwargs):
    """
	获取双边买入净价(最优)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"binetbid_bst",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getBibiDrTBst(security:list,*args,**kwargs):
    """
	获取双边买入收益率(最优)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"bibidrt_bst",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getBinetAskBst(security:list,*args,**kwargs):
    """
	获取双边卖出净价(最优)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"binetask_bst",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getBiasKrTBst(security:list,*args,**kwargs):
    """
	获取双边卖出收益率(最优)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"biaskrt_bst",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getBIqTvOlm(security:list,*args,**kwargs):
    """
	获取双边报价笔数

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"biqtvolm",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getNetBidAvg(security:list,*args,**kwargs):
    """
	获取报价买入净价(算术平均)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"netbid_avg",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getBidRtAvg(security:list,*args,**kwargs):
    """
	获取报价买入收益率(算术平均)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"bidrt_avg",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getNeTaskAvg(security:list,*args,**kwargs):
    """
	获取报价卖出净价(算术平均)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"netask_avg",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getAskRtAvg(security:list,*args,**kwargs):
    """
	获取报价卖出收益率(算术平均)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"askrt_avg",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getNetBidBst(security:list,*args,**kwargs):
    """
	获取报价买入净价(最优)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"netbid_bst",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getBidRtBst(security:list,*args,**kwargs):
    """
	获取报价买入收益率(最优)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"bidrt_bst",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getNeTaskBst(security:list,*args,**kwargs):
    """
	获取报价卖出净价(最优)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"netask_bst",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getAskRtBst(security:list,*args,**kwargs):
    """
	获取报价卖出收益率(最优)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"askrt_bst",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getQtVolM(security:list,*args,**kwargs):
    """
	获取报价总笔数

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"qtvolm",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPqAmount(security:list,*args,**kwargs):
    """
	获取区间成交金额

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"pq_amount",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getNav(security:list,*args,**kwargs):
    """
	获取单位净值

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"nav",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundNavCur(security:list,*args,**kwargs):
    """
	获取单位净值币种

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_navcur",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getNav2(security:list,*args,**kwargs):
    """
	获取单位净值(不前推)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"nav2",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getNavUnitTransform(security:list,*args,**kwargs):
    """
	获取单位净值(支持转型基金)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"NAV_unit_transform",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getNavAdj(security:list,*args,**kwargs):
    """
	获取复权单位净值

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"NAV_adj",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getNavAdj2(security:list,*args,**kwargs):
    """
	获取复权单位净值(不前推)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"NAV_adj2",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getNavAcc(security:list,*args,**kwargs):
    """
	获取累计单位净值

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"NAV_acc",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getNavAccumulatedTransform(security:list,*args,**kwargs):
    """
	获取累计单位净值(支持转型基金)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"NAV_accumulated_transform",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getNavAdjustedTransform(security:list,*args,**kwargs):
    """
	获取复权单位净值(支持转型基金)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"NAV_adjusted_transform",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getNavAdjChg(security:list,*args,**kwargs):
    """
	获取复权单位净值增长

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"NAV_adj_chg",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getNavAccChg(security:list,*args,**kwargs):
    """
	获取累计单位净值增长

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"NAV_acc_chg",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getNavAdjReturn(security:list,*args,**kwargs):
    """
	获取复权单位净值增长率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"NAV_adj_return",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getNavAccReturn(security:list,*args,**kwargs):
    """
	获取累计单位净值增长率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"NAV_acc_return",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getRelNavAdjReturn(security:list,*args,**kwargs):
    """
	获取复权单位净值相对大盘增长率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"rel_NAV_adj_return",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getNavAdjReturn1(security:list,*args,**kwargs):
    """
	获取当期复权单位净值增长率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"NAV_adj_return1",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getNavHighPer(security:list,*args,**kwargs):
    """
	获取区间最高单位净值

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"NAV_high_per",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundHighestNavDate(security:list,*args,**kwargs):
    """
	获取区间最高单位净值日

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_highestnav_date",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getNavLowPer(security:list,*args,**kwargs):
    """
	获取区间最低单位净值

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"NAV_low_per",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundLowestNavDate(security:list,*args,**kwargs):
    """
	获取区间最低单位净值日

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_lowestnav_date",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getNavAdjHighPer(security:list,*args,**kwargs):
    """
	获取区间最高复权单位净值

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"NAV_adj_high_per",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundHighestAdjNavDate(security:list,*args,**kwargs):
    """
	获取区间最高复权单位净值日

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_highestadjnav_date",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getNavAdjLowPer(security:list,*args,**kwargs):
    """
	获取区间最低复权单位净值

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"NAV_adj_low_per",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundLowestAdjNavDate(security:list,*args,**kwargs):
    """
	获取区间最低复权单位净值日

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_lowestadjnav_date",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getNavAccHighPer(security:list,*args,**kwargs):
    """
	获取区间最高累计单位净值

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"NAV_acc_high_per",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundHighestAcCumNavDate(security:list,*args,**kwargs):
    """
	获取区间最高累计单位净值日

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_highestaccumnav_date",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getNavAccLowPer(security:list,*args,**kwargs):
    """
	获取区间最低累计单位净值

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"NAV_acc_low_per",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundLowestAcCumNavDate(security:list,*args,**kwargs):
    """
	获取区间最低累计单位净值日

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_lowestaccumnav_date",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getSiNavAdjReturn(security:list,*args,**kwargs):
    """
	获取自成立日起复权单位净值增长率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"SI_nav_adj_return",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getNavSellPrice(security:list,*args,**kwargs):
    """
	获取投连险卖出价

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"NAV_sellprice",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getNavDate(security:list,*args,**kwargs):
    """
	获取最近基金净值日期

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"NAV_date",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getNavExRightDate(security:list,*args,**kwargs):
    """
	获取最新净值除权日

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"NAV_exrightdate",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getNavPublishType(security:list,*args,**kwargs):
    """
	获取基金净值公布类型

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"NAV_publishtype",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getNavDivReturn(security:list,*args,**kwargs):
    """
	获取现金分红净值增长率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"NAV_div_return",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getNavOverBenchReturnPer(security:list,*args,**kwargs):
    """
	获取区间净值超越基准收益率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"NAV_over_bench_return_per",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getNavOverBenchReturnFrEq(security:list,*args,**kwargs):
    """
	获取区间净值超越基准收益频率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"NAV_over_bench_return_freq",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getNavOverBenchReturnFrEq2(security:list,*args,**kwargs):
    """
	获取区间净值超越基准收益频率(百分比)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"NAV_over_bench_return_freq2",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getReturn1W(security:list,*args,**kwargs):
    """
	获取近1周回报

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"return_1w",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPeriodReturnRanking1W(security:list,*args,**kwargs):
    """
	获取近1周回报排名

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"periodreturnranking_1w",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getReturn1M(security:list,*args,**kwargs):
    """
	获取近1月回报

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"return_1m",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPeriodReturnRanking1M(security:list,*args,**kwargs):
    """
	获取近1月回报排名

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"periodreturnranking_1m",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getReturn3M(security:list,*args,**kwargs):
    """
	获取近3月回报

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"return_3m",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPeriodReturnRanking3M(security:list,*args,**kwargs):
    """
	获取近3月回报排名

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"periodreturnranking_3m",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getReturn6M(security:list,*args,**kwargs):
    """
	获取近6月回报

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"return_6m",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPeriodReturnRanking6M(security:list,*args,**kwargs):
    """
	获取近6月回报排名

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"periodreturnranking_6m",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getReturn1Y(security:list,*args,**kwargs):
    """
	获取近1年回报

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"return_1y",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPeriodReturnRanking1Y(security:list,*args,**kwargs):
    """
	获取近1年回报排名

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"periodreturnranking_1y",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getReturn2Y(security:list,*args,**kwargs):
    """
	获取近2年回报

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"return_2y",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPeriodReturnRanking2Y(security:list,*args,**kwargs):
    """
	获取近2年回报排名

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"periodreturnranking_2y",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getReturn3Y(security:list,*args,**kwargs):
    """
	获取近3年回报

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"return_3y",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPeriodReturnRanking3Y(security:list,*args,**kwargs):
    """
	获取近3年回报排名

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"periodreturnranking_3y",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getReturn5Y(security:list,*args,**kwargs):
    """
	获取近5年回报

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"return_5y",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPeriodReturnRanking5Y(security:list,*args,**kwargs):
    """
	获取近5年回报排名

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"periodreturnranking_5y",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getReturn10Y(security:list,*args,**kwargs):
    """
	获取近10年回报

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"return_10y",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPeriodReturnRanking10Y(security:list,*args,**kwargs):
    """
	获取近10年回报排名

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"periodreturnranking_10y",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getReturnYTd(security:list,*args,**kwargs):
    """
	获取今年以来回报

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"return_ytd",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPeriodReturnRankingYTd(security:list,*args,**kwargs):
    """
	获取今年以来回报排名

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"periodreturnranking_ytd",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getReturnStd(security:list,*args,**kwargs):
    """
	获取成立以来回报

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"return_std",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getReturnM(security:list,*args,**kwargs):
    """
	获取单月度回报

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"return_m",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getReturnQ(security:list,*args,**kwargs):
    """
	获取单季度回报

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"return_q",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getReturnY(security:list,*args,**kwargs):
    """
	获取单年度回报

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"return_y",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPeriodReturnRankingY(security:list,*args,**kwargs):
    """
	获取单年度回报排名

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"periodreturnranking_y",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPeerFundAvgReturnPer(security:list,*args,**kwargs):
    """
	获取同类基金区间平均收益率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"peer_fund_avg_return_per",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPeerFundReturnRankPer(security:list,*args,**kwargs):
    """
	获取同类基金区间收益排名(字符串)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"peer_fund_return_rank_per",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPeerFundReturnRankPropPer(security:list,*args,**kwargs):
    """
	获取同类基金区间收益排名(百分比)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"peer_fund_return_rank_prop_per",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPeerSamReturnRankPropPer(security:list,*args,**kwargs):
    """
	获取同类基金区间收益排名(百分比)(券商集合理财)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"peer_SAM_return_rank_prop_per",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPeerHfReturnRankPropPer(security:list,*args,**kwargs):
    """
	获取同类基金区间收益排名(百分比)(阳光私募)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"peer_HF_return_rank_prop_per",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPeerSamReturnRankPer(security:list,*args,**kwargs):
    """
	获取同类基金区间收益排名(券商集合理财)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"peer_SAM_return_rank_per",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPeerHfReturnRankPer(security:list,*args,**kwargs):
    """
	获取同类基金区间收益排名(阳光私募)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"peer_HF_return_rank_per",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPeerHf2ReturnRankPer(security:list,*args,**kwargs):
    """
	获取同类基金区间收益排名(阳光私募,投资策略)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"peer_HF2_return_rank_per",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getNavReturn(security:list,*args,**kwargs):
    """
	获取报告期净值增长率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"NAV_return",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getNavStdDevReturn(security:list,*args,**kwargs):
    """
	获取报告期净值增长率标准差

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"NAV_stddevreturn",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getNavBenchDevReturn(security:list,*args,**kwargs):
    """
	获取报告期净值增长率减基准增长率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"NAV_benchdevreturn",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getNavStdDevNavBench(security:list,*args,**kwargs):
    """
	获取报告期净值增长率减基准增长率标准差

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"NAV_stddevnavbench",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getMmFCarryOver(security:list,*args,**kwargs):
    """
	获取份额结转方式

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"mmf_carryover",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getMmFCarryOverDate(security:list,*args,**kwargs):
    """
	获取份额结转日期类型

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"mmf_carryoverdate",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getMmFAnnualIZedYield(security:list,*args,**kwargs):
    """
	获取7日年化收益率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"mmf_annualizedyield",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getMmFAvgAnnualIZedYield(security:list,*args,**kwargs):
    """
	获取区间7日年化收益率均值

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"mmf_avgannualizedyield",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getMmFVarAnnualIZedYield(security:list,*args,**kwargs):
    """
	获取区间7日年化收益率方差

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"mmf_varannualizedyield",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getMmFUnitYield(security:list,*args,**kwargs):
    """
	获取万份基金单位收益

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"mmf_unityield",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getMmFAvgUnitYield(security:list,*args,**kwargs):
    """
	获取区间万份基金单位收益均值

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"mmf_avgunityield",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getMmFTotalUnitYield(security:list,*args,**kwargs):
    """
	获取区间万份基金单位收益总值

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"mmf_totalunityield",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getMmFVarUnitYield(security:list,*args,**kwargs):
    """
	获取区间万份基金单位收益方差

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"mmf_varunityield",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getDividendYield(security:list,*args,**kwargs):
    """
	获取股息率(报告期)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"dividendyield",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getDividendYield2(security:list,*args,**kwargs):
    """
	获取股息率(近12个月)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"dividendyield2",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getValDividendYield2Issuer(security:list,*args,**kwargs):
    """
	获取发布方股息率(近12个月)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"val_dividendyield2_issuer",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getValPep2(security:list,*args,**kwargs):
    """
	获取市盈率百分位

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"val_pep2",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getValPePercentile(security:list,*args,**kwargs):
    """
	获取市盈率分位数

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"val_pe_percentile",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getValPbPercentile(security:list,*args,**kwargs):
    """
	获取市净率分位数

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"val_pb_percentile",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getValDividendPercentile(security:list,*args,**kwargs):
    """
	获取股息率分位数

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"val_dividend_percentile",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getValPsPercentile(security:list,*args,**kwargs):
    """
	获取市销率分位数

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"val_ps_percentile",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getValPcfPercentile(security:list,*args,**kwargs):
    """
	获取市现率分位数

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"val_pcf_percentile",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getTargetNp(security:list,*args,**kwargs):
    """
	获取股权激励目标净利润

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"targetnp",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getVolRatio(security:list,*args,**kwargs):
    """
	获取量比

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"vol_ratio",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getOiLoiC(security:list,*args,**kwargs):
    """
	获取持买单量比上交易日增减

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"oi_loic",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getOiSOic(security:list,*args,**kwargs):
    """
	获取持卖单量比上交易日增减

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"oi_soic",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIpoVsSharesPct(security:list,*args,**kwargs):
    """
	获取网下有效报价申购量比例

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"ipo_VSSharesPct",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIpoInvsSharesPctA(security:list,*args,**kwargs):
    """
	获取网下高于有效报价上限的申购量比例

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"ipo_InvSSharesPct_a",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getHistoryLow(security:list,*args,**kwargs):
    """
	获取近期创历史新低

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"history_low",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getHistoryLowDays(security:list,*args,**kwargs):
    """
	获取近期创历史新低次数

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"history_low_days",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getStageHigh(security:list,*args,**kwargs):
    """
	获取近期创阶段新高

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"stage_high",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getHistoryHigh(security:list,*args,**kwargs):
    """
	获取近期创历史新高

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"history_high",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getHistoryHighDays(security:list,*args,**kwargs):
    """
	获取近期创历史新高次数

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"history_high_days",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getStageLow(security:list,*args,**kwargs):
    """
	获取近期创阶段新低

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"stage_low",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getUpDays(security:list,*args,**kwargs):
    """
	获取连涨天数

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"up_days",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getDownDays(security:list,*args,**kwargs):
    """
	获取连跌天数

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"down_days",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getBreakoutMa(security:list,*args,**kwargs):
    """
	获取向上有效突破均线

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"breakout_ma",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getBreakdownMa(security:list,*args,**kwargs):
    """
	获取向下有效突破均线

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"breakdown_ma",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getTechAnalStageHighNum(security:list,*args,**kwargs):
    """
	获取成份创阶段新高数量

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"techanal_stagehigh_num",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getTechAnalStageLowNum(security:list,*args,**kwargs):
    """
	获取成份创阶段新低数量

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"techanal_stagelow_num",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getBullBearMa(security:list,*args,**kwargs):
    """
	获取均线多空头排列看涨看跌

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"bull_bear_ma",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getTechUpNum(security:list,*args,**kwargs):
    """
	获取指数成份上涨数量

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"tech_upnum",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getTechDownNum(security:list,*args,**kwargs):
    """
	获取指数成份下跌数量

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"tech_downnum",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getTechLimitUpNum(security:list,*args,**kwargs):
    """
	获取指数成份涨停数量

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"tech_limitupnum",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getTechLimitDownNum(security:list,*args,**kwargs):
    """
	获取指数成份跌停数量

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"tech_limitdownnum",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getDivCompIndex(security:list,*args,**kwargs):
    """
	获取成份分红对指数影响

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"div_compindex",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getAnnualYeIlD100W(security:list,*args,**kwargs):
    """
	获取平均收益率(年化,最近100周)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"annualyeild_100w",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getAnnualYeIlD24M(security:list,*args,**kwargs):
    """
	获取平均收益率(年化,最近24个月)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"annualyeild_24m",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getAnnualYeIlD60M(security:list,*args,**kwargs):
    """
	获取平均收益率(年化,最近60个月)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"annualyeild_60m",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getAnnualStDeVr100W(security:list,*args,**kwargs):
    """
	获取年化波动率(最近100周)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"annualstdevr_100w",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getAnnualStDeVr24M(security:list,*args,**kwargs):
    """
	获取年化波动率(最近24个月)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"annualstdevr_24m",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getAnnualStDeVr60M(security:list,*args,**kwargs):
    """
	获取年化波动率(最近60个月)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"annualstdevr_60m",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getAvgReturn(security:list,*args,**kwargs):
    """
	获取平均收益率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"avgreturn",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getAvgReturnY(security:list,*args,**kwargs):
    """
	获取平均收益率(年化)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"avgreturny",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getRiskAvgReturn(security:list,*args,**kwargs):
    """
	获取平均收益率_FUND

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"risk_avgreturn",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getRiskGemReturn(security:list,*args,**kwargs):
    """
	获取几何平均收益率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"risk_gemreturn",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getStmNoteBank720(security:list,*args,**kwargs):
    """
	获取贷款平均收益率_总计

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"stmnote_bank_720",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getStmNoteBank731(security:list,*args,**kwargs):
    """
	获取贷款平均收益率_企业贷款及垫款

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"stmnote_bank_731",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getStmNoteBank732(security:list,*args,**kwargs):
    """
	获取贷款平均收益率_个人贷款及垫款

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"stmnote_bank_732",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getStmNoteBank733(security:list,*args,**kwargs):
    """
	获取贷款平均收益率_票据贴现

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"stmnote_bank_733",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getStmNoteBank734(security:list,*args,**kwargs):
    """
	获取贷款平均收益率_个人住房贷款

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"stmnote_bank_734",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getStmNoteBank735(security:list,*args,**kwargs):
    """
	获取贷款平均收益率_个人消费贷款

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"stmnote_bank_735",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getStmNoteBank736(security:list,*args,**kwargs):
    """
	获取贷款平均收益率_信用卡应收账款

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"stmnote_bank_736",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getStmNoteBank737(security:list,*args,**kwargs):
    """
	获取贷款平均收益率_经营性贷款

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"stmnote_bank_737",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getStmNoteBank738(security:list,*args,**kwargs):
    """
	获取贷款平均收益率_汽车贷款

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"stmnote_bank_738",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getStmNoteBank739(security:list,*args,**kwargs):
    """
	获取贷款平均收益率_其他个人贷款

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"stmnote_bank_739",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getStmNoteBank791(security:list,*args,**kwargs):
    """
	获取贷款平均收益率_信用贷款

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"stmnote_bank_791",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getStmNoteBank792(security:list,*args,**kwargs):
    """
	获取贷款平均收益率_保证贷款

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"stmnote_bank_792",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getStmNoteBank793(security:list,*args,**kwargs):
    """
	获取贷款平均收益率_抵押贷款

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"stmnote_bank_793",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getStmNoteBank794(security:list,*args,**kwargs):
    """
	获取贷款平均收益率_质押贷款

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"stmnote_bank_794",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getStmNoteBank47(security:list,*args,**kwargs):
    """
	获取贷款平均收益率_短期贷款

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"stmnote_bank_47",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getStmNoteBank49(security:list,*args,**kwargs):
    """
	获取贷款平均收益率_中长期贷款

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"stmnote_bank_49",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getRiskAnnualIntervalYield(security:list,*args,**kwargs):
    """
	获取区间收益率(年化)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"risk_annualintervalyield",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getRiskMaxDownside(security:list,*args,**kwargs):
    """
	获取最大回撤

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"risk_maxdownside",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getRiskMaxDownsideRecoverDays(security:list,*args,**kwargs):
    """
	获取最大回撤恢复天数

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"risk_maxdownside_recoverdays",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getRiskSimLAvgMaxDownside(security:list,*args,**kwargs):
    """
	获取最大回撤同类平均

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"risk_siml_avgmaxdownside",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getRiskMaxDownsideDate(security:list,*args,**kwargs):
    """
	获取最大回撤区间日期

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"risk_maxdownside_date",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundManagerMaxDrawDown(security:list,*args,**kwargs):
    """
	获取任期最大回撤

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_manager_maxdrawdown",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getStDeVr(security:list,*args,**kwargs):
    """
	获取波动率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"stdevr",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getStDeVry(security:list,*args,**kwargs):
    """
	获取波动率(年化)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"stdevry",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getRiskStDevYearly(security:list,*args,**kwargs):
    """
	获取年化波动率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"risk_stdevyearly",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getRiskSimLAvgStDevYearly(security:list,*args,**kwargs):
    """
	获取年化波动率同类平均

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"risk_siml_avgstdevyearly",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getTechVolumeVolatility(security:list,*args,**kwargs):
    """
	获取交易量波动率_PIT

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"tech_volumevolatility",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getImpliedVol(security:list,*args,**kwargs):
    """
	获取转债隐含波动率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"impliedvol",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getRiskVolatilityRatio(security:list,*args,**kwargs):
    """
	获取个股与市场波动率比值_PIT

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"risk_volatilityratio",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getRiskReSidVol252(security:list,*args,**kwargs):
    """
	获取252日残差收益波动率_PIT

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"risk_residvol252",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getStDcOf(security:list,*args,**kwargs):
    """
	获取标准差系数

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"stdcof",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getRiskNonSYsRisk1(security:list,*args,**kwargs):
    """
	获取非系统风险

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"risk_nonsysrisk1",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getRiskNonSYsRisk(security:list,*args,**kwargs):
    """
	获取非系统风险_FUND

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"risk_nonsysrisk",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getDay(security:list,*args,**kwargs):
    """
	获取剩余期限(天)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"day",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPtMYear(security:list,*args,**kwargs):
    """
	获取剩余期限(年)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"ptmyear",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getTermIfExercise(security:list,*args,**kwargs):
    """
	获取行权剩余期限(年)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"termifexercise",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getTermNote(security:list,*args,**kwargs):
    """
	获取特殊剩余期限说明

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"termnote",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getTermNote1(security:list,*args,**kwargs):
    """
	获取特殊剩余期限

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"termnote1",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWeightedRt(security:list,*args,**kwargs):
    """
	获取加权剩余期限(按本息)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"weightedrt",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWeightedRt2(security:list,*args,**kwargs):
    """
	获取加权剩余期限(按本金)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"weightedrt2",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getAccruedInterest(security:list,*args,**kwargs):
    """
	获取应计利息

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"accruedinterest",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getCalcAccRInt(security:list,*args,**kwargs):
    """
	获取指定日应计利息

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"calc_accrint",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getAccruedDays(security:list,*args,**kwargs):
    """
	获取已计息天数

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"accrueddays",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getAnalPreCupN(security:list,*args,**kwargs):
    """
	获取上一付息日

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"anal_precupn",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getNxcUpn(security:list,*args,**kwargs):
    """
	获取下一付息日

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"nxcupn",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getNxcUpnDuration(security:list,*args,**kwargs):
    """
	获取下一付息日久期

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"nxcupn_duration",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getNxcUpn2(security:list,*args,**kwargs):
    """
	获取距下一付息日天数

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"nxcupn2",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPqSuspendStartDate(security:list,*args,**kwargs):
    """
	获取长期停牌起始日

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"pq_suspendstartdate",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getPqSuspendEnddate(security:list,*args,**kwargs):
    """
	获取长期停牌截止日

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"pq_suspendenddate",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getYTMB(security:list,*args,**kwargs):
    """
	获取收盘到期收益率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"ytm_b",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getYTc(security:list,*args,**kwargs):
    """
	获取赎回收益率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"ytc",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getYTP(security:list,*args,**kwargs):
    """
	获取回售收益率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"ytp",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getBDuration(security:list,*args,**kwargs):
    """
	获取基准久期

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"bduration",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getBDurationIfExe(security:list,*args,**kwargs):
    """
	获取行权基准久期

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"Bduration_ifexe",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getSDuration(security:list,*args,**kwargs):
    """
	获取利差久期

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"sduration",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getSDurationIfExe(security:list,*args,**kwargs):
    """
	获取行权利差久期

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"Sduration_ifexe",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getDailyCf(security:list,*args,**kwargs):
    """
	获取指定日现金流

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"dailycf",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getDailyCfInt(security:list,*args,**kwargs):
    """
	获取指定日利息现金流

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"dailycf_int",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getDailyCfPrIn(security:list,*args,**kwargs):
    """
	获取指定日本金现金流

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"dailycf_prin",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getRCyTm(security:list,*args,**kwargs):
    """
	获取票面调整收益率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"RCYTM",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getCalcAdjYield(security:list,*args,**kwargs):
    """
	获取价格算票面调整收益率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"calc_adjyield",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getNxOptionDate(security:list,*args,**kwargs):
    """
	获取下一行权日

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"nxoptiondate",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getYTMIfExe(security:list,*args,**kwargs):
    """
	获取行权收益率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"YTM_ifexe",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getDurationIfExercise(security:list,*args,**kwargs):
    """
	获取行权久期

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"durationifexercise",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getModiDurationIfExe(security:list,*args,**kwargs):
    """
	获取行权修正久期

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"modiduration_ifexe",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getConvexityIfExe(security:list,*args,**kwargs):
    """
	获取行权凸性

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"convexity_ifexe",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getBConvexityIfExe(security:list,*args,**kwargs):
    """
	获取行权基准凸性

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"Bconvexity_ifexe",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getSConvexityIfExe(security:list,*args,**kwargs):
    """
	获取行权利差凸性

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"Sconvexity_ifexe",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getDuration1M(security:list,*args,**kwargs):
    """
	获取1月久期

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"duration_1m",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getDuration3M(security:list,*args,**kwargs):
    """
	获取3月久期

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"duration_3m",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getDuration6M(security:list,*args,**kwargs):
    """
	获取6月久期

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"duration_6m",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getDuration1Y(security:list,*args,**kwargs):
    """
	获取1年久期

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"duration_1y",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getDuration2Y(security:list,*args,**kwargs):
    """
	获取2年久期

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"duration_2y",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getDuration3Y(security:list,*args,**kwargs):
    """
	获取3年久期

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"duration_3y",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getDuration4Y(security:list,*args,**kwargs):
    """
	获取4年久期

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"duration_4y",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getDuration5Y(security:list,*args,**kwargs):
    """
	获取5年久期

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"duration_5y",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getDuration15Y(security:list,*args,**kwargs):
    """
	获取15年久期

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"duration_15y",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getDuration7Y(security:list,*args,**kwargs):
    """
	获取7年久期

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"duration_7y",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getDuration9Y(security:list,*args,**kwargs):
    """
	获取9年久期

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"duration_9y",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getDuration10Y(security:list,*args,**kwargs):
    """
	获取10年久期

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"duration_10y",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getDuration20Y(security:list,*args,**kwargs):
    """
	获取20年久期

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"duration_20y",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getDuration30Y(security:list,*args,**kwargs):
    """
	获取30年久期

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"duration_30y",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getDurationShort(security:list,*args,**kwargs):
    """
	获取短边久期

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"duration_short",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getDurationLong(security:list,*args,**kwargs):
    """
	获取长边久期

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"duration_long",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getCurYield(security:list,*args,**kwargs):
    """
	获取当期收益率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"curyield",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getYTMCb(security:list,*args,**kwargs):
    """
	获取纯债到期收益率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"ytm_cb",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getStrBValue(security:list,*args,**kwargs):
    """
	获取纯债价值

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"strbvalue",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getStrBPremium(security:list,*args,**kwargs):
    """
	获取纯债溢价

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"strbpremium",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getStrBPremiumRatio(security:list,*args,**kwargs):
    """
	获取纯债溢价率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"strbpremiumratio",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getConVPrice(security:list,*args,**kwargs):
    """
	获取转股价

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"convprice",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getConVRatio(security:list,*args,**kwargs):
    """
	获取转股比例

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"convratio",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getConVValue(security:list,*args,**kwargs):
    """
	获取转换价值

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"convvalue",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getConVPremium(security:list,*args,**kwargs):
    """
	获取转股溢价

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"convpremium",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getConVPremiumRatio(security:list,*args,**kwargs):
    """
	获取转股溢价率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"convpremiumratio",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getConVpE(security:list,*args,**kwargs):
    """
	获取转股市盈率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"convpe",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getConVpB(security:list,*args,**kwargs):
    """
	获取转股市净率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"convpb",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getUnderlyingPe(security:list,*args,**kwargs):
    """
	获取正股市盈率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"underlyingpe",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getUnderlyingPb(security:list,*args,**kwargs):
    """
	获取正股市净率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"underlyingpb",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getDiluteRate(security:list,*args,**kwargs):
    """
	获取转股稀释率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"diluterate",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getLDiluteRate(security:list,*args,**kwargs):
    """
	获取对流通股稀释率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"ldiluterate",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getDoubleLow(security:list,*args,**kwargs):
    """
	获取双低

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"doublelow",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getTBfCVf2(security:list,*args,**kwargs):
    """
	获取转换因子

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"tbf_cvf2",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getTBfCVf(security:list,*args,**kwargs):
    """
	获取转换因子(指定合约)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"tbf_cvf",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getTBfCVf3(security:list,*args,**kwargs):
    """
	获取转换因子(主力合约)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"tbf_cvf3",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getTBfInterest(security:list,*args,**kwargs):
    """
	获取交割利息

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"tbf_interest",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getTBfPayment(security:list,*args,**kwargs):
    """
	获取区间利息

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"tbf_payment",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getTBfDeliverPrice(security:list,*args,**kwargs):
    """
	获取交割成本

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"tbf_deliverprice",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getTBfInvoicePrice(security:list,*args,**kwargs):
    """
	获取发票价格

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"tbf_invoiceprice",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getTBfSpread(security:list,*args,**kwargs):
    """
	获取期现价差

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"tbf_spread",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getTBfBasis(security:list,*args,**kwargs):
    """
	获取基差

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"tbf_basis",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIfBasis(security:list,*args,**kwargs):
    """
	获取基差(股指期货)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"if_basis",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getAnalBasisAnnualYield(security:list,*args,**kwargs):
    """
	获取基差年化收益率(股指期货)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"anal_basisannualyield",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getAnalBasisPercent(security:list,*args,**kwargs):
    """
	获取基差率(股指期货)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"anal_basispercent",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getAnalBasis(security:list,*args,**kwargs):
    """
	获取基差(商品期货)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"anal_basis",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getAnalBasisPercent2(security:list,*args,**kwargs):
    """
	获取基差率(商品期货)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"anal_basispercent2",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getTBfNetBasis(security:list,*args,**kwargs):
    """
	获取净基差

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"tbf_netbasis",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getTBfFyTm(security:list,*args,**kwargs):
    """
	获取远期收益率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"tbf_FYTM",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getCalcClean(security:list,*args,**kwargs):
    """
	获取全价算净价

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"calc_clean",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getCalcDirty(security:list,*args,**kwargs):
    """
	获取净价算全价

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"calc_dirty",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getCalcDuration(security:list,*args,**kwargs):
    """
	获取麦考利久期

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"calc_duration",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getCalcMDuration(security:list,*args,**kwargs):
    """
	获取修正久期

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"calc_mduration",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getCalcConV(security:list,*args,**kwargs):
    """
	获取凸性

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"calc_conv",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getYCCode(security:list,*args,**kwargs):
    """
	获取对应到期收益率曲线代码

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"YCCode",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getCalcChinaBond(security:list,*args,**kwargs):
    """
	获取收益率曲线(中债样本券)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"calc_chinabond",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getRatingShanghaiSharpe3Y(security:list,*args,**kwargs):
    """
	获取上海证券3年评级(夏普比率)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"rating_shanghaisharpe3y",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getRatingShanghaiTiming3Y(security:list,*args,**kwargs):
    """
	获取上海证券3年评级(择时能力)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"rating_shanghaitiming3y",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getRatingShanghaiStocking3Y(security:list,*args,**kwargs):
    """
	获取上海证券3年评级(选证能力)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"rating_shanghaistocking3y",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getRatingShanghaiSharpe5Y(security:list,*args,**kwargs):
    """
	获取上海证券5年评级(夏普比率)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"rating_shanghaisharpe5y",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getRatingShanghaiTiming5Y(security:list,*args,**kwargs):
    """
	获取上海证券5年评级(择时能力)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"rating_shanghaitiming5y",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getRatingShanghaiStocking5Y(security:list,*args,**kwargs):
    """
	获取上海证券5年评级(选证能力)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"rating_shanghaistocking5y",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getRating3Y(security:list,*args,**kwargs):
    """
	获取基金3年评级

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"rating_3y",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getRating5Y(security:list,*args,**kwargs):
    """
	获取基金5年评级

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"rating_5y",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getRiskReturnYearly(security:list,*args,**kwargs):
    """
	获取年化收益率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"risk_returnyearly",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getRiskReturnYearlyTradeDate(security:list,*args,**kwargs):
    """
	获取年化收益率(工作日)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"risk_returnyearly_tradedate",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundManagerGeometricAnnualIZedYield(security:list,*args,**kwargs):
    """
	获取几何平均年化收益率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_manager_geometricannualizedyield",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundManagerArithmeticAnnualIZedYield(security:list,*args,**kwargs):
    """
	获取算术平均年化收益率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_manager_arithmeticannualizedyield",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundManagerGeometricAvgAnnualYieldOverBench(security:list,*args,**kwargs):
    """
	获取超越基准几何平均年化收益率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_manager_geometricavgannualyieldoverbench",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundManagerArithmeticAvgAnnualYieldOverBench(security:list,*args,**kwargs):
    """
	获取超越基准算术平均年化收益率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_manager_arithmeticavgannualyieldoverbench",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getRiskNavOverBenchAnnualReturn(security:list,*args,**kwargs):
    """
	获取区间净值超越基准年化收益率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"risk_navoverbenchannualreturn",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getRiskAnnualIntervalYieldTradeDate(security:list,*args,**kwargs):
    """
	获取区间收益率(工作日年化)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"risk_annualintervalyield_tradedate",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getRiskAvgRiskReturn(security:list,*args,**kwargs):
    """
	获取平均风险收益率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"risk_avgriskreturn",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getRiskGemAvgRiskReturn(security:list,*args,**kwargs):
    """
	获取几何平均风险收益率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"risk_gemavgriskreturn",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getRiskTrackDeviationTrackIndex(security:list,*args,**kwargs):
    """
	获取日跟踪偏离度(跟踪指数)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"risk_trackdeviation_trackindex",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getRiskAvgTrackDeviationBenchmark(security:list,*args,**kwargs):
    """
	获取区间跟踪偏离度均值(业绩基准)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"risk_avgtrackdeviation_benchmark",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getRiskAvgTrackDeviationTrackIndex(security:list,*args,**kwargs):
    """
	获取区间跟踪偏离度均值(跟踪指数)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"risk_avgtrackdeviation_trackindex",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getRiskDownside(security:list,*args,**kwargs):
    """
	获取回撤(相对前期高点)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"risk_downside",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getRiskMaxUpside(security:list,*args,**kwargs):
    """
	获取最大上涨

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"risk_maxupside",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getRiskCorreCoefficient(security:list,*args,**kwargs):
    """
	获取相关系数

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"risk_correcoefficient",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getRiskCorreCoefficientTrackIndex(security:list,*args,**kwargs):
    """
	获取相关系数(跟踪指数)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"risk_correcoefficient_trackindex",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getTechDdNcr(security:list,*args,**kwargs):
    """
	获取下跌相关系数_PIT

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"tech_ddncr",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getRiskHisRelation(security:list,*args,**kwargs):
    """
	获取个股与市场相关系数_PIT

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"risk_hisrelation",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getRiskR2(security:list,*args,**kwargs):
    """
	获取可决系数

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"risk_r2",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getRiskStDev(security:list,*args,**kwargs):
    """
	获取收益标准差

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"risk_stdev",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getRiskAnnUstDev(security:list,*args,**kwargs):
    """
	获取收益标准差(年化)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"risk_annustdev",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getRiskExStDev252(security:list,*args,**kwargs):
    """
	获取252日超额收益标准差_PIT

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"risk_exstdev252",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getRiskDownsideStDev(security:list,*args,**kwargs):
    """
	获取下行标准差

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"risk_downsidestdev",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getRiskUpsideStDev(security:list,*args,**kwargs):
    """
	获取上行标准差

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"risk_upsidestdev",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getRiskDownsideRisk(security:list,*args,**kwargs):
    """
	获取下行风险

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"risk_downsiderisk",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getRiskSimLAvgDownsideRisk(security:list,*args,**kwargs):
    """
	获取下行风险同类平均

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"risk_siml_avgdownsiderisk",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWinRatio(security:list,*args,**kwargs):
    """
	获取区间胜率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"win_ratio",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getRiskDuration(security:list,*args,**kwargs):
    """
	获取基金组合久期

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"risk_duration",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getRiskInterestSensitivity(security:list,*args,**kwargs):
    """
	获取市场利率敏感性

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"risk_interestsensitivity",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getRiskTime(security:list,*args,**kwargs):
    """
	获取选时能力

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"risk_time",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getRiskStock(security:list,*args,**kwargs):
    """
	获取选股能力

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"risk_stock",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getRiskTrackError(security:list,*args,**kwargs):
    """
	获取跟踪误差

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"risk_trackerror",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getRiskTrackErrorTrackIndex(security:list,*args,**kwargs):
    """
	获取跟踪误差(跟踪指数)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"risk_trackerror_trackindex",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getRiskAnNuTrackError(security:list,*args,**kwargs):
    """
	获取跟踪误差(年化)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"risk_annutrackerror",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getRiskInfoRatio(security:list,*args,**kwargs):
    """
	获取信息比率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"risk_inforatio",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getRiskAnNuInfoRatio(security:list,*args,**kwargs):
    """
	获取信息比率(年化)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"risk_annuinforatio",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getStyleStyleCoefficient(security:list,*args,**kwargs):
    """
	获取风格系数

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"style_stylecoefficient",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getStyleStyleAttribute(security:list,*args,**kwargs):
    """
	获取风格属性

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"style_styleattribute",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getStyleMarketValueStyleAttribute(security:list,*args,**kwargs):
    """
	获取市值-风格属性

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"style_marketvaluestyleattribute",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getStyleMarketValueAttribute(security:list,*args,**kwargs):
    """
	获取市值属性

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"style_marketvalueattribute",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getStyleAveragePositionTime(security:list,*args,**kwargs):
    """
	获取平均持仓时间

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"style_averagepositiontime",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getStyleHyAveragePositionTime(security:list,*args,**kwargs):
    """
	获取平均持仓时间(半年)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"style_hy_averagepositiontime",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getStyleInvConcentration(security:list,*args,**kwargs):
    """
	获取投资集中度

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"style_invconcentration",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getStyleComMisAccount(security:list,*args,**kwargs):
    """
	获取佣金规模比

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"style_commisaccount",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getAbsoluteHighestMonthlyReturn(security:list,*args,**kwargs):
    """
	获取最高单月回报

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"absolute_highestmonthlyreturn",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getAbsoluteLowestMonthlyReturn(security:list,*args,**kwargs):
    """
	获取最低单月回报

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"absolute_lowestmonthlyreturn",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getAbsoluteSimLAvgLowestMonthlyReturn(security:list,*args,**kwargs):
    """
	获取最低单月回报同类平均

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"absolute_siml_avglowestmonthlyreturn",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getAbsoluteConUpsMonth(security:list,*args,**kwargs):
    """
	获取连涨月数

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"absolute_conupsmonth",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getAbsoluteCondOwnsMonth(security:list,*args,**kwargs):
    """
	获取连跌月数

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"absolute_condownsmonth",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getAbsoluteLongestConUpMonth(security:list,*args,**kwargs):
    """
	获取最长连续上涨月数

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"absolute_longestconupmonth",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getAbsoluteMaxIncreaseOfUpMonth(security:list,*args,**kwargs):
    """
	获取最长连续上涨整月涨幅

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"absolute_maxincreaseofupmonth",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getAbsoluteLongestConDownMonth(security:list,*args,**kwargs):
    """
	获取最长连续下跌月数

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"absolute_longestcondownmonth",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getAbsoluteMaxFallOfDownMonth(security:list,*args,**kwargs):
    """
	获取最长连续下跌整月跌幅

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"absolute_maxfallofdownmonth",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getAbsoluteUpDownMonthRatio(security:list,*args,**kwargs):
    """
	获取上涨/下跌月数比

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"absolute_updownmonthratio",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getAbsoluteProfitMonthPer(security:list,*args,**kwargs):
    """
	获取盈利百分比

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"absolute_profitmonthper",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getAbsoluteProfitPer(security:list,*args,**kwargs):
    """
	获取区间盈利百分比

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"absolute_profitper",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getAbsoluteAvgIncome(security:list,*args,**kwargs):
    """
	获取平均收益

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"absolute_avgincome",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFaPtToMvAvg5Y(security:list,*args,**kwargs):
    """
	获取5年平均收益市值比_PIT

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fa_pttomvavg5y",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getAbsoluteAvgLoss(security:list,*args,**kwargs):
    """
	获取平均损失

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"absolute_avgloss",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getRiskEspaRam(security:list,*args,**kwargs):
    """
	获取参数平均损失值ES

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"risk_esparam",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getRiskEsHistorical(security:list,*args,**kwargs):
    """
	获取历史平均损失值ES

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"risk_eshistorical",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getAbsoluteMonthlyCompositeReturn(security:list,*args,**kwargs):
    """
	获取月度复合回报

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"absolute_monthlycompositereturn",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getAbsoluteAvgMonthlyReturn(security:list,*args,**kwargs):
    """
	获取平均月度回报

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"absolute_avgmonthlyreturn",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getAbsoluteHighestQuatreTurn(security:list,*args,**kwargs):
    """
	获取最高季度回报

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"absolute_highestquatreturn",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getAbsoluteLowestQuatreTurn(security:list,*args,**kwargs):
    """
	获取最低季度回报

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"absolute_lowestquatreturn",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundDaysToConversion(security:list,*args,**kwargs):
    """
	获取剩余折算天数

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_daystoconversion",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getAnalSMfEarning(security:list,*args,**kwargs):
    """
	获取分级基金收益分配方式

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"anal_smfearning",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getAnalImpliedYield(security:list,*args,**kwargs):
    """
	获取隐含收益率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"anal_impliedyield",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getAnalTDiscountRatio(security:list,*args,**kwargs):
    """
	获取整体折溢价率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"anal_tdiscountratio",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getAnalDIsRatioDevi(security:list,*args,**kwargs):
    """
	获取折溢价比率偏离系数

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"anal_disratiodevi",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getAnalNavLever(security:list,*args,**kwargs):
    """
	获取净值杠杆

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"anal_navlever",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getAnalPriceLever(security:list,*args,**kwargs):
    """
	获取价格杠杆

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"anal_pricelever",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getAnalSmFbNamedCost(security:list,*args,**kwargs):
    """
	获取名义资金成本

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"anal_smfbnamedcost",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getAnalSmFbFactualCost(security:list,*args,**kwargs):
    """
	获取实际资金成本

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"anal_smfbfactualcost",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getAnalNextDiscountDate(security:list,*args,**kwargs):
    """
	获取下一定期折算日

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"anal_nextdiscountdate",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFundAgreedAnNuYield(security:list,*args,**kwargs):
    """
	获取本期约定年收益率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fund_agreedannuyield",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getAnalNextAAYield(security:list,*args,**kwargs):
    """
	获取下期约定年收益率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"anal_nextaayield",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getAnalUpDiscountThreshold(security:list,*args,**kwargs):
    """
	获取上折阈值

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"anal_updiscount_threshold",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getAnalDownDiscountThreshold(security:list,*args,**kwargs):
    """
	获取下折阈值

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"anal_downdiscount_threshold",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getAnalUpDiscountPctChange(security:list,*args,**kwargs):
    """
	获取上折母基金需涨

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"anal_updiscount_pctchange",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getAnalDownDiscountPctChange(security:list,*args,**kwargs):
    """
	获取下折母基金需跌

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"anal_downdiscount_pctchange",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getOiLoi(security:list,*args,**kwargs):
    """
	获取持买单量

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"oi_loi",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getOiLvOi(security:list,*args,**kwargs):
    """
	获取持买单量(品种)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"oi_lvoi",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getOiLName(security:list,*args,**kwargs):
    """
	获取持买单量进榜会员名称

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"oi_lname",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getOiLvName(security:list,*args,**kwargs):
    """
	获取持买单量(品种)会员名称

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"oi_lvname",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getOiSoI(security:list,*args,**kwargs):
    """
	获取持卖单量

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"oi_soi",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getOiSvOi(security:list,*args,**kwargs):
    """
	获取持卖单量(品种)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"oi_svoi",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getOiSName(security:list,*args,**kwargs):
    """
	获取持卖单量进榜会员名称

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"oi_sname",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getOiSvName(security:list,*args,**kwargs):
    """
	获取持卖单量(品种)会员名称

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"oi_svname",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getOiNvOi(security:list,*args,**kwargs):
    """
	获取净持仓(品种)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"oi_nvoi",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getGrpS(security:list,*args,**kwargs):
    """
	获取每股营业总收入

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"grps",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWgsDGrpS2(security:list,*args,**kwargs):
    """
	获取每股营业总收入_GSD

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"wgsd_grps2",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFaGrpS(security:list,*args,**kwargs):
    """
	获取每股营业总收入_PIT

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fa_grps",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getOrPsTtM(security:list,*args,**kwargs):
    """
	获取每股营业收入(TTM)_PIT

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"orps_ttm",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getOrPs(security:list,*args,**kwargs):
    """
	获取每股营业收入

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"orps",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWgsDOrPs(security:list,*args,**kwargs):
    """
	获取每股营业收入_GSD

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"wgsd_orps",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFaOrPs(security:list,*args,**kwargs):
    """
	获取每股营业收入_PIT

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fa_orps",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getSurplusCapitalPs(security:list,*args,**kwargs):
    """
	获取每股资本公积

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"surpluscapitalps",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFaCapSurPpS(security:list,*args,**kwargs):
    """
	获取每股资本公积_PIT

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fa_capsurpps",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getSurplusReservePs(security:list,*args,**kwargs):
    """
	获取每股盈余公积

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"surplusreserveps",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFaSppS(security:list,*args,**kwargs):
    """
	获取每股盈余公积_PIT

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fa_spps",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getUnDistributedPs(security:list,*args,**kwargs):
    """
	获取每股未分配利润

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"undistributedps",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFaUnDistributedPs(security:list,*args,**kwargs):
    """
	获取每股未分配利润_PIT

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fa_undistributedps",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getRetainedPs(security:list,*args,**kwargs):
    """
	获取每股留存收益

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"retainedps",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWgsDRetainedPs2(security:list,*args,**kwargs):
    """
	获取每股留存收益_GSD

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"wgsd_retainedps2",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFaRetainedPs(security:list,*args,**kwargs):
    """
	获取每股留存收益_PIT

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fa_retainedps",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getEbItPs(security:list,*args,**kwargs):
    """
	获取每股息税前利润

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"ebitps",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWgsDEbItPs2(security:list,*args,**kwargs):
    """
	获取每股息税前利润_GSD

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"wgsd_ebitps2",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getRoeYearly(security:list,*args,**kwargs):
    """
	获取年化净资产收益率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"roe_yearly",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getRoa2Yearly(security:list,*args,**kwargs):
    """
	获取年化总资产报酬率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"roa2_yearly",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getRoaYearly(security:list,*args,**kwargs):
    """
	获取年化总资产净利率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"roa_yearly",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getNetProfitMargin(security:list,*args,**kwargs):
    """
	获取销售净利率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"netprofitmargin",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getNetProfitMarginTtM2(security:list,*args,**kwargs):
    """
	获取销售净利率(TTM)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"netprofitmargin_ttm2",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWgsDNetProfitMargin(security:list,*args,**kwargs):
    """
	获取销售净利率_GSD

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"wgsd_netprofitmargin",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getNetProfitMarginTtM3(security:list,*args,**kwargs):
    """
	获取销售净利率(TTM)_GSD

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"netprofitmargin_ttm3",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFaNetProfitMarginTtM(security:list,*args,**kwargs):
    """
	获取销售净利率(TTM)_PIT

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fa_netprofitmargin_ttm",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getNetProfitMarginTtM(security:list,*args,**kwargs):
    """
	获取销售净利率(TTM,只有最新数据)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"netprofitmargin_ttm",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getNetProfitMarginDeducted(security:list,*args,**kwargs):
    """
	获取扣非后销售净利率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"netprofitmargin_deducted",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getQfaNetProfitMargin(security:list,*args,**kwargs):
    """
	获取单季度.销售净利率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"qfa_netprofitmargin",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWgsDQfaNetProfitMargin(security:list,*args,**kwargs):
    """
	获取单季度.销售净利率_GSD

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"wgsd_qfa_netprofitmargin",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getGrossProfitMargin(security:list,*args,**kwargs):
    """
	获取销售毛利率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"grossprofitmargin",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getGrossProfitMarginTtM2(security:list,*args,**kwargs):
    """
	获取销售毛利率(TTM)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"grossprofitmargin_ttm2",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWgsDGrossProfitMargin(security:list,*args,**kwargs):
    """
	获取销售毛利率_GSD

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"wgsd_grossprofitmargin",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getGrossProfitMarginTtM3(security:list,*args,**kwargs):
    """
	获取销售毛利率(TTM)_GSD

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"grossprofitmargin_ttm3",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFaGrossProfitMarginTtM(security:list,*args,**kwargs):
    """
	获取销售毛利率(TTM)_PIT

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fa_grossprofitmargin_ttm",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getGrossProfitMarginTtM(security:list,*args,**kwargs):
    """
	获取销售毛利率(TTM,只有最新数据)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"grossprofitmargin_ttm",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWestAvgGm(security:list,*args,**kwargs):
    """
	获取预测销售毛利率(GM)平均值(可选类型)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"west_avggm",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWestMaxGm(security:list,*args,**kwargs):
    """
	获取预测销售毛利率(GM)最大值(可选类型)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"west_maxgm",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWestMingM(security:list,*args,**kwargs):
    """
	获取预测销售毛利率(GM)最小值(可选类型)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"west_mingm",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWestMediaGm(security:list,*args,**kwargs):
    """
	获取预测销售毛利率(GM)中值(可选类型)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"west_mediagm",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWestStdGm(security:list,*args,**kwargs):
    """
	获取预测销售毛利率(GM)标准差值(可选类型)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"west_stdgm",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getQfaGrossProfitMargin(security:list,*args,**kwargs):
    """
	获取单季度.销售毛利率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"qfa_grossprofitmargin",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWgsDQfaGrossProfitMargin(security:list,*args,**kwargs):
    """
	获取单季度.销售毛利率_GSD

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"wgsd_qfa_grossprofitmargin",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getCogsToSales(security:list,*args,**kwargs):
    """
	获取销售成本率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"cogstosales",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWgsDCogsToSales(security:list,*args,**kwargs):
    """
	获取销售成本率_GSD

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"wgsd_cogstosales",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFaSalesToCostTtM(security:list,*args,**kwargs):
    """
	获取销售成本率(TTM)_PIT

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fa_salestocost_ttm",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getNpToCostExpense(security:list,*args,**kwargs):
    """
	获取成本费用利润率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"nptocostexpense",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFaProtoCostTtM(security:list,*args,**kwargs):
    """
	获取成本费用利润率(TTM)_PIT

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fa_protocost_ttm",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getNpToCostExpenseQfa(security:list,*args,**kwargs):
    """
	获取单季度.成本费用利润率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"nptocostexpense_qfa",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getExpenseToSales(security:list,*args,**kwargs):
    """
	获取销售期间费用率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"expensetosales",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getExpenseToSalesTtM2(security:list,*args,**kwargs):
    """
	获取销售期间费用率(TTM)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"expensetosales_ttm2",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getExpenseToSalesTtM3(security:list,*args,**kwargs):
    """
	获取销售期间费用率(TTM)_GSD

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"expensetosales_ttm3",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFaExpenseToSalesTtM(security:list,*args,**kwargs):
    """
	获取销售期间费用率(TTM)_PIT

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fa_expensetosales_ttm",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getExpenseToSalesTtM(security:list,*args,**kwargs):
    """
	获取销售期间费用率(TTM,只有最新数据)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"expensetosales_ttm",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getOpToEBT(security:list,*args,**kwargs):
    """
	获取主营业务比率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"optoebt",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getOpToEBTQfa(security:list,*args,**kwargs):
    """
	获取单季度.主营业务比率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"optoebt_qfa",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getProfitToGr(security:list,*args,**kwargs):
    """
	获取净利润/营业总收入

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"profittogr",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getProfitToGrTtM2(security:list,*args,**kwargs):
    """
	获取净利润/营业总收入(TTM)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"profittogr_ttm2",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWgsDDupontNpToSales(security:list,*args,**kwargs):
    """
	获取净利润/营业总收入_GSD

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"wgsd_dupont_nptosales",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getProfitToGrTtM3(security:list,*args,**kwargs):
    """
	获取净利润/营业总收入(TTM)_GSD

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"profittogr_ttm3",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFaProfitToGrTtM(security:list,*args,**kwargs):
    """
	获取净利润/营业总收入(TTM)_PIT

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fa_profittogr_ttm",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getProfitToGrTtM(security:list,*args,**kwargs):
    """
	获取净利润/营业总收入(TTM,只有最新数据)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"profittogr_ttm",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getQfaProfitToGr(security:list,*args,**kwargs):
    """
	获取单季度.净利润/营业总收入

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"qfa_profittogr",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getOpToGr(security:list,*args,**kwargs):
    """
	获取营业利润/营业总收入

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"optogr",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getOpToGrTtM2(security:list,*args,**kwargs):
    """
	获取营业利润/营业总收入(TTM)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"optogr_ttm2",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWgsDOpToGr(security:list,*args,**kwargs):
    """
	获取营业利润/营业总收入_GSD

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"wgsd_optogr",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getOpToGrTtM3(security:list,*args,**kwargs):
    """
	获取营业利润/营业总收入(TTM)_GSD

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"optogr_ttm3",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFaOpToGrTtM(security:list,*args,**kwargs):
    """
	获取营业利润/营业总收入(TTM)_PIT

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fa_optogr_ttm",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getOpToGrTtM(security:list,*args,**kwargs):
    """
	获取营业利润/营业总收入(TTM,只有最新数据)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"optogr_ttm",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getQfaOpToGr(security:list,*args,**kwargs):
    """
	获取单季度.营业利润/营业总收入

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"qfa_optogr",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getEbItToGr(security:list,*args,**kwargs):
    """
	获取息税前利润/营业总收入

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"ebittogr",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWgsDDupontEbItToSales(security:list,*args,**kwargs):
    """
	获取息税前利润/营业总收入_GSD

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"wgsd_dupont_ebittosales",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFaEbItToGrTtM(security:list,*args,**kwargs):
    """
	获取息税前利润/营业总收入(TTM)_PIT

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fa_ebittogr_ttm",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getGcToGr(security:list,*args,**kwargs):
    """
	获取营业总成本/营业总收入

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"gctogr",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getGcToGrTtM2(security:list,*args,**kwargs):
    """
	获取营业总成本/营业总收入(TTM)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"gctogr_ttm2",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWgsDGcToGr(security:list,*args,**kwargs):
    """
	获取营业总成本/营业总收入_GSD

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"wgsd_gctogr",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getGcToGrTtM3(security:list,*args,**kwargs):
    """
	获取营业总成本/营业总收入(TTM)_GSD

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"gctogr_ttm3",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFaOctoGrTtM(security:list,*args,**kwargs):
    """
	获取营业总成本/营业总收入(TTM)_PIT

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fa_octogr_ttm",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getGcToGrTtM(security:list,*args,**kwargs):
    """
	获取营业总成本/营业总收入(TTM,只有最新数据)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"gctogr_ttm",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getQfaGcToGr(security:list,*args,**kwargs):
    """
	获取单季度.营业总成本/营业总收入

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"qfa_gctogr",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getOperateExpenseToGr(security:list,*args,**kwargs):
    """
	获取销售费用/营业总收入

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"operateexpensetogr",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getOperateExpenseToGrTtM2(security:list,*args,**kwargs):
    """
	获取销售费用/营业总收入(TTM)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"operateexpensetogr_ttm2",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWgsDOperateExpenseToGr(security:list,*args,**kwargs):
    """
	获取销售费用/营业总收入_GSD

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"wgsd_operateexpensetogr",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getOperateExpenseToGrTtM3(security:list,*args,**kwargs):
    """
	获取销售费用/营业总收入(TTM)_GSD

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"operateexpensetogr_ttm3",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFaSellExpenseToGrTtM(security:list,*args,**kwargs):
    """
	获取销售费用/营业总收入(TTM)_PIT

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fa_sellexpensetogr_ttm",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getOperateExpenseToGrTtM(security:list,*args,**kwargs):
    """
	获取销售费用/营业总收入(TTM,只有最新数据)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"operateexpensetogr_ttm",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getQfaSaleExpenseToGr(security:list,*args,**kwargs):
    """
	获取单季度.销售费用/营业总收入

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"qfa_saleexpensetogr",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getAdminExpenseToGr(security:list,*args,**kwargs):
    """
	获取管理费用/营业总收入

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"adminexpensetogr",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getAdminExpenseToGrTtM2(security:list,*args,**kwargs):
    """
	获取管理费用/营业总收入(TTM)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"adminexpensetogr_ttm2",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWgsDAdminExpenseToGr(security:list,*args,**kwargs):
    """
	获取管理费用/营业总收入_GSD

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"wgsd_adminexpensetogr",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getAdminExpenseToGrTtM3(security:list,*args,**kwargs):
    """
	获取管理费用/营业总收入(TTM)_GSD

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"adminexpensetogr_ttm3",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFaAdminExpenseToGrTtM(security:list,*args,**kwargs):
    """
	获取管理费用/营业总收入(TTM)_PIT

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fa_adminexpensetogr_ttm",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getAdminExpenseToGrTtM(security:list,*args,**kwargs):
    """
	获取管理费用/营业总收入(TTM,只有最新数据)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"adminexpensetogr_ttm",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getQfaAdminExpenseToGr(security:list,*args,**kwargs):
    """
	获取单季度.管理费用/营业总收入

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"qfa_adminexpensetogr",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFinaExpenseToGr(security:list,*args,**kwargs):
    """
	获取财务费用/营业总收入

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"finaexpensetogr",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFinaExpenseToGrTtM2(security:list,*args,**kwargs):
    """
	获取财务费用/营业总收入(TTM)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"finaexpensetogr_ttm2",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWgsDFinaExpenseToGr(security:list,*args,**kwargs):
    """
	获取财务费用/营业总收入_GSD

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"wgsd_finaexpensetogr",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFinaExpenseToGrTtM3(security:list,*args,**kwargs):
    """
	获取财务费用/营业总收入(TTM)_GSD

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"finaexpensetogr_ttm3",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFaFinaExpenseToGrTtM(security:list,*args,**kwargs):
    """
	获取财务费用/营业总收入(TTM)_PIT

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fa_finaexpensetogr_ttm",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFinaExpenseToGrTtM(security:list,*args,**kwargs):
    """
	获取财务费用/营业总收入(TTM,只有最新数据)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"finaexpensetogr_ttm",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getQfaFinaExpenseToGr(security:list,*args,**kwargs):
    """
	获取单季度.财务费用/营业总收入

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"qfa_finaexpensetogr",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getOperateIncomeToEBT(security:list,*args,**kwargs):
    """
	获取经营活动净收益/利润总额

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"operateincometoebt",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getOperateIncomeToEBTTtM2(security:list,*args,**kwargs):
    """
	获取经营活动净收益/利润总额(TTM)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"operateincometoebt_ttm2",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWgsDOperateIncomeToEBT(security:list,*args,**kwargs):
    """
	获取经营活动净收益/利润总额_GSD

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"wgsd_operateincometoebt",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getOperateIncomeToEBTTtM3(security:list,*args,**kwargs):
    """
	获取经营活动净收益/利润总额(TTM)_GSD

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"operateincometoebt_ttm3",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFaOperIncomeToPbt(security:list,*args,**kwargs):
    """
	获取经营活动净收益/利润总额_PIT

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fa_operincometopbt",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFaOperIncomeToPbtTtM(security:list,*args,**kwargs):
    """
	获取经营活动净收益/利润总额(TTM)_PIT

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fa_operincometopbt_ttm",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getOperateIncomeToEBTTtM(security:list,*args,**kwargs):
    """
	获取经营活动净收益/利润总额(TTM,只有最新数据)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"operateincometoebt_ttm",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getQfaOperateIncomeToEBT(security:list,*args,**kwargs):
    """
	获取单季度.经营活动净收益/利润总额

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"qfa_operateincometoebt",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getInvestIncomeToEBT(security:list,*args,**kwargs):
    """
	获取价值变动净收益/利润总额

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"investincometoebt",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getInvestIncomeToEBTTtM2(security:list,*args,**kwargs):
    """
	获取价值变动净收益/利润总额(TTM)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"investincometoebt_ttm2",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWgsDInvestIncomeToEBT(security:list,*args,**kwargs):
    """
	获取价值变动净收益/利润总额_GSD

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"wgsd_investincometoebt",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getInvestIncomeToEBTTtM3(security:list,*args,**kwargs):
    """
	获取价值变动净收益/利润总额(TTM)_GSD

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"investincometoebt_ttm3",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFaChgValueToPbtTtM(security:list,*args,**kwargs):
    """
	获取价值变动净收益/利润总额(TTM)_PIT

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fa_chgvaluetopbt_ttm",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getInvestIncomeToEBTTtM(security:list,*args,**kwargs):
    """
	获取价值变动净收益/利润总额(TTM,只有最新数据)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"investincometoebt_ttm",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getQfaInvestIncomeToEBT(security:list,*args,**kwargs):
    """
	获取单季度.价值变动净收益/利润总额

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"qfa_investincometoebt",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getNonOperateProfitToEBT(security:list,*args,**kwargs):
    """
	获取营业外收支净额/利润总额

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"nonoperateprofittoebt",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getNonOperateProfitToEBTTtM2(security:list,*args,**kwargs):
    """
	获取营业外收支净额/利润总额(TTM)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"nonoperateprofittoebt_ttm2",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWgsDNonOperateProfitToEBT(security:list,*args,**kwargs):
    """
	获取营业外收支净额/利润总额_GSD

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"wgsd_nonoperateprofittoebt",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getNonOperateProfitToEBTTtM3(security:list,*args,**kwargs):
    """
	获取营业外收支净额/利润总额(TTM)_GSD

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"nonoperateprofittoebt_ttm3",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFaNonOperProfitToPbtTtM(security:list,*args,**kwargs):
    """
	获取营业外收支净额/利润总额(TTM)_PIT

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fa_nonoperprofittopbt_ttm",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getNonOperateProfitToEBTTtM(security:list,*args,**kwargs):
    """
	获取营业外收支净额/利润总额(TTM,只有最新数据)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"nonoperateprofittoebt_ttm",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getDeductedProfitToProfit(security:list,*args,**kwargs):
    """
	获取扣除非经常损益后的净利润/净利润

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"deductedprofittoprofit",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWgsDDeductedProfitToProfit(security:list,*args,**kwargs):
    """
	获取扣除非经常损益后的净利润/净利润_GSD

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"wgsd_deductedprofittoprofit",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getQfaDeductedProfitToProfit(security:list,*args,**kwargs):
    """
	获取单季度.扣除非经常损益后的净利润/净利润

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"qfa_deductedprofittoprofit",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getSalesCashIntoOr(security:list,*args,**kwargs):
    """
	获取销售商品提供劳务收到的现金/营业收入

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"salescashintoor",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getSalesCashIntoOrTtM2(security:list,*args,**kwargs):
    """
	获取销售商品提供劳务收到的现金/营业收入(TTM)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"salescashintoor_ttm2",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFaSalesCashToOr(security:list,*args,**kwargs):
    """
	获取销售商品提供劳务收到的现金/营业收入_PIT

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fa_salescashtoor",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFaSalesCashToOrTtM(security:list,*args,**kwargs):
    """
	获取销售商品提供劳务收到的现金/营业收入(TTM)_PIT

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fa_salescashtoor_ttm",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getSalesCashIntoOrTtM(security:list,*args,**kwargs):
    """
	获取销售商品提供劳务收到的现金/营业收入(TTM,只有最新数据)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"salescashintoor_ttm",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getQfaSalesCashIntoOr(security:list,*args,**kwargs):
    """
	获取单季度.销售商品提供劳务收到的现金/营业收入

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"qfa_salescashintoor",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFaNetProfitCashCover(security:list,*args,**kwargs):
    """
	获取净利润现金含量

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fa_netprofitcashcover",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getCapitalizedToda(security:list,*args,**kwargs):
    """
	获取资本支出/折旧和摊销

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"capitalizedtoda",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWgsDCapitalizedToda(security:list,*args,**kwargs):
    """
	获取资本支出/折旧和摊销_GSD

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"wgsd_capitalizedtoda",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getOCFToSales(security:list,*args,**kwargs):
    """
	获取经营性现金净流量/营业总收入

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"ocftosales",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getOCFToInvestStockDividend(security:list,*args,**kwargs):
    """
	获取现金满足投资比率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"ocftoinveststockdividend",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getOCFToOp(security:list,*args,**kwargs):
    """
	获取现金营运指数

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"ocftoop",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getOCFToAssets(security:list,*args,**kwargs):
    """
	获取全部资产现金回收率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"ocftoassets",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getOCFToDividend(security:list,*args,**kwargs):
    """
	获取现金股利保障倍数

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"ocftodividend",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFaCashDivCoverTtM(security:list,*args,**kwargs):
    """
	获取现金股利保障倍数(TTM)_PIT

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fa_cashdivcover_ttm",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getDebtToAssets(security:list,*args,**kwargs):
    """
	获取资产负债率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"debttoassets",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWgsDDebtToAssets(security:list,*args,**kwargs):
    """
	获取资产负债率_GSD

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"wgsd_debttoassets",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFaDebtToAsset(security:list,*args,**kwargs):
    """
	获取资产负债率_PIT

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fa_debttoasset",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFaDebtToEqY(security:list,*args,**kwargs):
    """
	获取净资产负债率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fa_debttoeqy",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWgsDAnnouncedDeductedDebtToAssets(security:list,*args,**kwargs):
    """
	获取剔除预收账款的资产负债率(公告值)_GSD

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"wgsd_announceddeducteddebttoassets",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getDeductedDebtToAssets2(security:list,*args,**kwargs):
    """
	获取剔除预收款项后的资产负债率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"deducteddebttoassets2",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getDeductedDebtToAssets(security:list,*args,**kwargs):
    """
	获取剔除预收款项后的资产负债率(公告口径)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"deducteddebttoassets",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWgsDDeductedDebtToAssets(security:list,*args,**kwargs):
    """
	获取剔除预收账款后的资产负债率_GSD

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"wgsd_deducteddebttoassets",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getLongDebtToLongCaptIAl(security:list,*args,**kwargs):
    """
	获取长期资本负债率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"longdebttolongcaptial",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getLongCapitalToInvestment(security:list,*args,**kwargs):
    """
	获取长期资产适合率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"longcapitaltoinvestment",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getAssetsToEquity(security:list,*args,**kwargs):
    """
	获取权益乘数

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"assetstoequity",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWgsDAssetsToEquity(security:list,*args,**kwargs):
    """
	获取权益乘数_GSD

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"wgsd_assetstoequity",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getEquityToAsset(security:list,*args,**kwargs):
    """
	获取股东权益比

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"equity_to_asset",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFaEquityAssetRadio(security:list,*args,**kwargs):
    """
	获取股东权益比率_PIT

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fa_equityassetradio",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getCatoAssets(security:list,*args,**kwargs):
    """
	获取流动资产/总资产

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"catoassets",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWgsDCatoAssets(security:list,*args,**kwargs):
    """
	获取流动资产/总资产_GSD

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"wgsd_catoassets",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getNcaToAssets(security:list,*args,**kwargs):
    """
	获取非流动资产/总资产

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"ncatoassets",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWgsDNcaToAssets(security:list,*args,**kwargs):
    """
	获取非流动资产/总资产_GSD

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"wgsd_ncatoassets",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getCurrentDebtToEquity(security:list,*args,**kwargs):
    """
	获取流动负债权益比率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"currentdebttoequity",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getLongDebtToEquity(security:list,*args,**kwargs):
    """
	获取非流动负债权益比率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"longdebttoequity",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getTangibleAssetsToAssets(security:list,*args,**kwargs):
    """
	获取有形资产/总资产

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"tangibleassetstoassets",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWgsDTangibleAssetsToAssets(security:list,*args,**kwargs):
    """
	获取有形资产/总资产_GSD

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"wgsd_tangibleassetstoassets",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getEquityToTotalCapital(security:list,*args,**kwargs):
    """
	获取归属母公司股东的权益/全部投入资本

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"equitytototalcapital",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIntDebtToTotalCap(security:list,*args,**kwargs):
    """
	获取带息债务/全部投入资本

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"intdebttototalcap",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWgsDInterestDebtToTotalCapital(security:list,*args,**kwargs):
    """
	获取带息债务/全部投入资本_GSD

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"wgsd_interestdebttototalcapital",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFaInterestDebtToCapital(security:list,*args,**kwargs):
    """
	获取带息债务/全部投入资本_PIT

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fa_interestdebttocapital",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getCurrentDebtToDebt(security:list,*args,**kwargs):
    """
	获取流动负债/负债合计

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"currentdebttodebt",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWgsDCurrentDebtToDebt(security:list,*args,**kwargs):
    """
	获取流动负债/负债合计_GSD

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"wgsd_currentdebttodebt",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getLongDebToDebt(security:list,*args,**kwargs):
    """
	获取非流动负债/负债合计

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"longdebtodebt",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWgsDLongDebToDebt(security:list,*args,**kwargs):
    """
	获取非流动负债/负债合计_GSD

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"wgsd_longdebtodebt",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getNcaToEquity(security:list,*args,**kwargs):
    """
	获取资本固定化比率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"ncatoequity",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getIbDebtRatio(security:list,*args,**kwargs):
    """
	获取有息负债率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"ibdebtratio",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getCurrent(security:list,*args,**kwargs):
    """
	获取流动比率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"current",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWgsDCurrent(security:list,*args,**kwargs):
    """
	获取流动比率_GSD

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"wgsd_current",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFaCurrent(security:list,*args,**kwargs):
    """
	获取流动比率_PIT

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fa_current",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getQuick(security:list,*args,**kwargs):
    """
	获取速动比率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"quick",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWgsDQuick(security:list,*args,**kwargs):
    """
	获取速动比率_GSD

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"wgsd_quick",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFaQuick(security:list,*args,**kwargs):
    """
	获取速动比率_PIT

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fa_quick",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFaSuperQuick(security:list,*args,**kwargs):
    """
	获取超速动比率_PIT

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fa_superquick",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getCashRatio(security:list,*args,**kwargs):
    """
	获取保守速动比率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"cashratio",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWgsDCashRatio(security:list,*args,**kwargs):
    """
	获取保守速动比率_GSD

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"wgsd_cashratio",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getCashToCurrentDebt(security:list,*args,**kwargs):
    """
	获取现金比率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"cashtocurrentdebt",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getOCFToQuickDebt(security:list,*args,**kwargs):
    """
	获取现金到期债务比

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"ocftoquickdebt",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getDebtToEquity(security:list,*args,**kwargs):
    """
	获取产权比率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"debttoequity",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWgsDDebtToEquity(security:list,*args,**kwargs):
    """
	获取产权比率_GSD

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"wgsd_debttoequity",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFaDebtToEquity(security:list,*args,**kwargs):
    """
	获取产权比率_PIT

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fa_debttoequity",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFaNetDebtRatio(security:list,*args,**kwargs):
    """
	获取净负债率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fa_netdebtratio",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWgsDNetDebtRatio(security:list,*args,**kwargs):
    """
	获取净负债率_GSD

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"wgsd_netdebtratio",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWgsDNetDebtRatioArd(security:list,*args,**kwargs):
    """
	获取净负债率(公告值)_GSD

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"wgsd_netdebtratio_ard",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getEquityToDebt(security:list,*args,**kwargs):
    """
	获取归属母公司股东的权益/负债合计

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"equitytodebt",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWgsDEquityToDebt(security:list,*args,**kwargs):
    """
	获取归属母公司股东的权益/负债合计_GSD

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"wgsd_equitytodebt",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getEquityToInterestDebt(security:list,*args,**kwargs):
    """
	获取归属母公司股东的权益/带息债务

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"equitytointerestdebt",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWgsDEquityToInterestDebt(security:list,*args,**kwargs):
    """
	获取归属母公司股东的权益/带息债务_GSD

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"wgsd_equitytointerestdebt",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFaEquityToInterestDebt(security:list,*args,**kwargs):
    """
	获取归属母公司股东的权益/带息债务_PIT

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fa_equitytointerestdebt",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getTangibleAssetToDebt(security:list,*args,**kwargs):
    """
	获取有形资产/负债合计

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"tangibleassettodebt",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWgsDTangibleAssetToDebt(security:list,*args,**kwargs):
    """
	获取有形资产/负债合计_GSD

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"wgsd_tangibleassettodebt",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getTangAssetToIntDebt(security:list,*args,**kwargs):
    """
	获取有形资产/带息债务

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"tangassettointdebt",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWgsDTangibleAssetToInterestDebt(security:list,*args,**kwargs):
    """
	获取有形资产/带息债务_GSD

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"wgsd_tangibleassettointerestdebt",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getTangibleAssetToNetDebt(security:list,*args,**kwargs):
    """
	获取有形资产/净债务

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"tangibleassettonetdebt",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWgsDTangibleAssetToNetDebt(security:list,*args,**kwargs):
    """
	获取有形资产/净债务_GSD

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"wgsd_tangibleassettonetdebt",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getDebtToTangibleEquity(security:list,*args,**kwargs):
    """
	获取有形净值债务率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"debttotangibleequity",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFaDebtToTangibleAFyBl(security:list,*args,**kwargs):
    """
	获取有形净值债务率_PIT

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fa_debttotangibleafybl",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getEbItDatoDebt(security:list,*args,**kwargs):
    """
	获取息税折旧摊销前利润/负债合计

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"ebitdatodebt",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWgsDEbItDatoDebt(security:list,*args,**kwargs):
    """
	获取息税折旧摊销前利润/负债合计_GSD

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"wgsd_ebitdatodebt",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getOcFicFToCurrentDebt(security:list,*args,**kwargs):
    """
	获取非筹资性现金净流量与流动负债的比率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"ocficftocurrentdebt",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getOcFicFToDebt(security:list,*args,**kwargs):
    """
	获取非筹资性现金净流量与负债总额的比率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"ocficftodebt",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getLongDebtToWorkingCapital(security:list,*args,**kwargs):
    """
	获取长期债务与营运资金比率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"longdebttoworkingcapital",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWgsDLongDebtToWorkingCapital(security:list,*args,**kwargs):
    """
	获取长期债务与营运资金比率_GSD

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"wgsd_longdebttoworkingcapital",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getLongDebtToDebt(security:list,*args,**kwargs):
    """
	获取长期负债占比

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"longdebttodebt",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getNetDebtToEv(security:list,*args,**kwargs):
    """
	获取净债务/股权价值

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"netdebttoev",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getInterestDebtToEv(security:list,*args,**kwargs):
    """
	获取带息债务/股权价值

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"interestdebttoev",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getTurnDays(security:list,*args,**kwargs):
    """
	获取营业周期

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"turndays",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWgsDTurnDays(security:list,*args,**kwargs):
    """
	获取营业周期_GSD

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"wgsd_turndays",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFaTurnDaysTtM(security:list,*args,**kwargs):
    """
	获取营业周期(TTM)_PIT

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fa_turndays_ttm",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getNetTurnDays(security:list,*args,**kwargs):
    """
	获取净营业周期

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"netturndays",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getInvTurnDays(security:list,*args,**kwargs):
    """
	获取存货周转天数

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"invturndays",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWgsDInvTurnDays(security:list,*args,**kwargs):
    """
	获取存货周转天数_GSD

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"wgsd_invturndays",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFaInvTurnDaysTtM(security:list,*args,**kwargs):
    """
	获取存货周转天数(TTM)_PIT

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fa_invturndays_ttm",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getArturNDays(security:list,*args,**kwargs):
    """
	获取应收账款周转天数

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"arturndays",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWgsDArturNDays(security:list,*args,**kwargs):
    """
	获取应收账款周转天数_GSD

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"wgsd_arturndays",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFaArturNDaysTtM(security:list,*args,**kwargs):
    """
	获取应收账款周转天数(TTM)_PIT

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fa_arturndays_ttm",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getApTurnDays(security:list,*args,**kwargs):
    """
	获取应付账款周转天数

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"apturndays",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWgsDApTurnDays(security:list,*args,**kwargs):
    """
	获取应付账款周转天数_GSD

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"wgsd_apturndays",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFaApTurnDaysTtM(security:list,*args,**kwargs):
    """
	获取应付账款周转天数(TTM)_PIT

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fa_apturndays_ttm",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getInvTurn(security:list,*args,**kwargs):
    """
	获取存货周转率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"invturn",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWgsDInvTurn(security:list,*args,**kwargs):
    """
	获取存货周转率_GSD

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"wgsd_invturn",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFaInvTurnTtM(security:list,*args,**kwargs):
    """
	获取存货周转率(TTM)_PIT

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fa_invturn_ttm",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getArturN(security:list,*args,**kwargs):
    """
	获取应收账款周转率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"arturn",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFaArturNReserve(security:list,*args,**kwargs):
    """
	获取应收账款周转率(含坏账准备)

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fa_arturn_reserve",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getWgsDArturN(security:list,*args,**kwargs):
    """
	获取应收账款周转率_GSD

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"wgsd_arturn",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFaArturNTtM(security:list,*args,**kwargs):
    """
	获取应收账款周转率(TTM)_PIT

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fa_arturn_ttm",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getFaArnRTurn(security:list,*args,**kwargs):
    """
	获取应收账款及应收票据周转率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
    return w.wss(security,"fa_arnrturn",*args,**kwargs,usedf=True)
@convertInputSecurityType
def getCaTurn(security:list,*args,**kwargs):
    """
	获取流动资产周转率

	Parameters
	----------
	security : list
		The list whose elements are security code.

	Returns
	-------
	pd.DataFrame
	"""
@convertInputSecurityType
    """
	获取流动资产周转率_GSD


	"""