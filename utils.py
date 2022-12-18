import pickle
import json
import config
import numpy as np

class SelPrice():


    def __init__(self,user_data):
        self.model_path=config.model_path
        self.user_data=user_data


    def load_saved_data(self):
        with open(self.model_path,"rb") as f:
            self.model=pickle.load(f)
        
        with open(config.project_data_path,"r") as f:
            self.project_data=json.load(f)


    def predict_selling_price(self):

        self.load_saved_data()
        Fuel_Type         = self.user_data['Fuel_Type']
        Seller_Type= self.user_data['Seller_Type']
        Transmission	 = self.user_data['Transmission']
        Owner        =self.user_data['Owner']

        Fuel_Type    =self.project_data['Fuel_Type'][Fuel_Type]
        Seller_Type  =self.project_data['Seller_Type'][Seller_Type]
        Transmission =self.project_data['Transmission'][Transmission]
        Owner        =self.project_data['Owner'][Owner]
        

        cnt= len(self.project_data['columns'])
        test = np.zeros(cnt)
        test[0] = eval(self.user_data['Year'])
        test[1] = eval(self.user_data['Present_Price'])
        test[2] = eval(self.user_data['Kms_Driven'])
        test[3] = Fuel_Type
        test[4] = Seller_Type
        test[5] = Transmission
        test[6] = Owner


        pre_selling_price= np.around(self.model.predict([test])[0],3)
        print('precicted selling_price is :',pre_selling_price)
        return pre_selling_price

if __name__=="__main__":
    selling_price=SelPrice()
    selling_price

