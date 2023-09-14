import pandas as pd
from .varData import structureData


class manageData(structureData):

    def __init__(self):
        super().__init__()

    def extractData(files,sheets):
        df = pd.read_excel(files, sheet_name=sheets)
        df.columns = df.columns.map(lambda x: '')
        return df
    
    def extractDataQuota(files):
        df = pd.read_excel(files)
        df.columns = df.columns.map(lambda x: '')
        return df
    
    def extractDataN8(files):
        df = pd.read_csv(files)
        df.columns = df.columns.map(lambda x: '')
        return df

    def loadData(output,output_name):
        output.to_csv('C:/Users/mateo/Documents/NovoAuto/NovoAuto/Output/' + output_name + '.csv', index=False)


class getTable(structureData):

    def getCustomers(df,start_act,end_act,start_des,end_des):
        customers_name = df.iloc[:,0]
        customs = []
        rangos = []
        for i in range(start_act,end_act,11):
            rango = slice(i+1,i+10)
            rangos.append(rango)
            customs.append(customers_name[i])
        for i in range(start_des,end_des):
            customs.append(customers_name[i])
        customs = [x for x in customs if customs.count(x) == 1] 
        customers = {custom: rango for custom, rango in zip(customs, rangos)}
        return customs,customers
    
    def getCustomersN8(df,start_act,end_act):
        customers_name = df.iloc[:,2]
        customs = []
        rangos = []
        for i in range(start_act,end_act):
            rangos.append(i)
            customs.append(customers_name[i])
        customs = [x for x in customs if customs.count(x) == 1] 
        customers = {custom: rango for custom, rango in zip(customs, rangos)}
        return customs,customers
    
    def getUseType(df,use_type):
        use_type = list(df.iloc[use_type,0])
        return use_type
    
    def getDates():
        date_spec = []
        for a in range(2022,2028):
            for m in range(1,13):
                if m < 10:
                    date = '01' + '/' + '0' + str(m) + '/' + str(a)
                    date_spec.append(date)
                else:
                    date = '01' + '/' +  str(m) + '/' + str(a)
                    date_spec.append(date)
        return date_spec
    
class manageTable:

    def genTable(customs,date_spec,use_type):
        combinaciones = [(cliente, dates, ut) for cliente in customs for dates in date_spec for ut in use_type]
        output = pd.DataFrame(combinaciones, columns=['customer_name','date_spec','use_type'])
        return output
    
    def genTableN8(customs,date_spec):
        combinaciones = [(cliente, dates) for cliente in customs for dates in date_spec]
        output = pd.DataFrame(combinaciones, columns=['customer_name','date_spec'])
        return output
    
    def outputTable(df,output,customers,years,tipo):
        report = []
        for custom in customers:
            volumenes = []
            volume = []
            for year in years:
                volumenes.append(df.iloc[customers[custom],years[year]])
            volumenes = pd.concat(volumenes, ignore_index=True)
            volumenes.columns = columna=['01','02','03','04','05','06','07','08','09','10','11','12']
            data = output.loc[output['customer_name'] == custom].reset_index(drop=True)
            for columna in volumenes.columns:
                for valor in volumenes[columna]:
                    volume.append(valor)
            data.loc[:,'volume'] = pd.DataFrame(volume)
            report.append(data)
        report = pd.concat(report, ignore_index=True)
        report['brand_name'] = 'N7'
        report['uom_code'] = 'MG'
        report['version_type'] = tipo
        return report
    
    def outputTableN8(df,output,customers,years,tipo):
        volumenes = {}
        datas = []
        for custom in customers:
            datayear = []
            for year in years:
                datayear.append(df.iloc[customers[custom],years[year]])
            volumenes[custom] = datayear
            report = pd.concat(volumenes[custom],ignore_index=True)
            data = output.loc[output['customer_name'] == custom].reset_index(drop=True)
            for row_indexer, value in enumerate(report):
                data.loc[row_indexer, 'volume'] = value
            datas.append(data)
        datas = pd.concat(datas,ignore_index=True)
        datas['use_type'] = 'null'
        datas['brand_name'] = 'N8'
        datas['uom_code'] = 'UI'
        datas['version_type'] = tipo
        datas = datas[['customer_name', 'date_spec', 'use_type','volume','brand_name','uom_code','version_type']]
        return datas
    
    def outputTableQuota(df,output,customers,years):
        ab_report = []
        for custom in customers:
            ab_volumenes = []
            ab_volume = []

            for year in years:
                ab_volumenes.append(df.iloc[customers[custom],years[year]])
            ab_volumenes = pd.concat(ab_volumenes, ignore_index=True)
            ab_volumenes.columns = columna=['01','02','03','04','05','06','07','08','09','10','11','12']
            data = output.loc[output['customer_name'] == custom].reset_index(drop=True)
            for columna in ab_volumenes.columns:
                for valor in ab_volumenes[columna]:
                    ab_volume.append(valor)
            data.loc[:, 'volume'] = pd.DataFrame(ab_volume)
            ab_report.append(data)
        ab_report = pd.concat(ab_report, ignore_index=True)
        ab_report['brand_name'] = 'N7'
        ab_report['uom_code'] = 'MG'
        ab_report['sales_rep_code'] = 'null'
        ab_report['region_name'] = 'null'
        ab_report = ab_report[['date_spec','sales_rep_code','region_name','customer_name', 'use_type','volume','brand_name','uom_code']]
        return ab_report
