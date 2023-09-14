from classNovo.getData import manageData, getTable, manageTable
import pandas as pd

class nv(manageData,getTable,manageTable):

    def report(self,dash):
        report = manageData.extractData(self.path[dash],self.sheet[dash])
        customs,customers = getTable.getCustomers(report,
                                                  self.rangeCustoms[dash]['start_act'],
                                                  self.rangeCustoms[dash]['end_act'],
                                                  self.rangeCustoms[dash]['start_des'],
                                                  self.rangeCustoms[dash]['end_des'])
        use_type = getTable.getUseType(report,self.rangeCustoms[dash]['use_type'])
        date_spec = getTable.getDates()
        output = manageTable.genTable(customs,date_spec,use_type)
        report = manageTable.outputTable(report,output,customers,self.year[dash],self.tipo[dash])
        return report
    
    def reportN8(self,dash):
        report = manageData.extractDataN8(self.pathN8[dash])
        customs,customers = getTable.getCustomersN8(report,
                                                  self.rangeCustomsN8['start_act'],
                                                  self.rangeCustomsN8['end_act'])
        date_spec = getTable.getDates()
        output = manageTable.genTableN8(customs,date_spec)
        report = manageTable.outputTableN8(report,output,customers,self.yearN8,self.tipo[dash])
        return report
    
    def reportQuota(self,dash):
        report = manageData.extractDataQuota(self.path[dash])
        customs,customers = getTable.getCustomers(report,
                                                  self.rangeCustoms[dash]['start_act'],
                                                  self.rangeCustoms[dash]['end_act'],
                                                  self.rangeCustoms[dash]['start_des'],
                                                  self.rangeCustoms[dash]['end_des'])
        use_type = getTable.getUseType(report,self.rangeCustoms[dash]['use_type'])
        date_spec = getTable.getDates()
        output = manageTable.genTable(customs,date_spec,use_type)
        report = manageTable.outputTableQuota(report,output,customers,self.year[dash])
        return report


    
if __name__=='__main__':
    nv_instance = nv() 
    output_ab = nv_instance.report('ab')
    output_re = nv_instance.report('re')
    outputN7 = pd.concat([output_ab,output_re],ignore_index=True)
    output_abn8 = nv_instance.reportN8('ab')
    output_ren8 = nv_instance.reportN8('re')
    output_quota= nv_instance.reportQuota('qu')
    outputN8 = pd.concat([output_abn8,output_ren8],ignore_index=True)
    output = pd.concat([outputN7,outputN8],ignore_index=True)
    manageData.loadData(output, 'N7-N8_AB-RE')
    manageData.loadData(output_quota, 'N7_QUOTA')

        