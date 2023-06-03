import pandas as pd
import numpy as np
import json
import pickle
import config
import warnings
warnings.filterwarnings("ignore")

class Sales_Data():
    print("We are in Sales Data")
    def __init__(self,Item_Weight,Item_Fat_Content,Item_Visibility,Item_Type,
                 Item_MRP,Outlet_Establishment_Year,Outlet_Size,
                 Outlet_Location_Type,Outlet_Type):
        print("we are in init method")
        self.Item_Weight=Item_Weight
        self.Item_Fat_Content = Item_Fat_Content
        self.Item_Visibility = Item_Visibility
        self.Item_Type =  Item_Type
        self.Item_MRP = Item_MRP
        self.Outlet_Establishment_Year = Outlet_Establishment_Year
        self.Outlet_Size = Outlet_Size
        self.Outlet_Location_Type = Outlet_Location_Type
        self.Outlet_Type = Outlet_Type

    def load_models(self):
        print("we are in load model method")
        with open(config.JSON_PATH,"r") as j :
            self.json_data=json.load(j)

            print("json created")

        with open(config.MODEL_PATH,"rb") as m :
            self.model=pickle.load(m)

            print("pickle imported sucessfuly")

    def get_sales_price(self):
        print("we are in get sales price method")

        self.load_models() #create instance to use another method in one method

        Item_type_input = "Item_Type_" + self.Item_Type
        Item_Type_Index = list(self.json_data["columns"]).index(Item_type_input)
        # Item_Type_Index

        test_array =np.zeros(len(self.json_data["columns"]))
        test_array[0]=self.Item_Weight
        test_array[1] =self.json_data["Item_Fat_Content"][self.Item_Fat_Content]
        test_array[2] =self.Item_Visibility
        test_array[3] =self.Item_MRP
        test_array[4] =self.Outlet_Establishment_Year
        test_array[5] =self.json_data["Outlet_Size"][self.Outlet_Size]
        test_array[6] =self.json_data["Outlet_Location_Type"][self.Outlet_Location_Type]
        test_array[Item_Type_Index] = 1

        price = round(self.model.predict([test_array])[0])
        return price
    
if __name__== "__main__":
    Item_Weight=19
    Item_Fat_Content='Regular'
    Item_Visibility=0.016047
    Item_Type = "Breakfast"
    Item_MRP=141.6180
    Outlet_Establishment_Year=1998
    Outlet_Size='High'
    Outlet_Location_Type='Tier 1'
    Outlet_Type='Supermarket Type1'
    

    object = Sales_Data(Item_Weight,Item_Fat_Content,Item_Visibility,Item_Type,
                 Item_MRP,Outlet_Establishment_Year,Outlet_Size,Outlet_Location_Type,Outlet_Type)
    
    price = object.get_sales_price()
    print("Predicte Sales is -->",price)