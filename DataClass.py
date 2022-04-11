from unicodedata import category


class Data:

    def __init__(self):
        pass

    @staticmethod
    def minheights(filename):
        import pandas as pd
        df = pd.read_csv(filename, header = 0)
        df = df.dropna(axis=0, subset=['Insulation Type'])
        df = df['Size'].reset_index(drop=True)

        df_split = df.str.split('-',expand=True)

        df_s1 = df_split[0].str.split('x',expand=True)
        df_s2 = df_split[1].str.split('x',expand=True)
        df_s3 = df_split[2].str.split('x',expand=True)

        # Joining width dimensions into single dataframe
        df_width = df_s1[0].to_frame()
        df_width = df_width.join(df_s2[0], lsuffix='1', rsuffix='2')
        df_width = df_width.join(df_s3[0])
        df_width = df_width.fillna(99999) # To convert null values into integers
        df_width = df_width.astype(int)


        # Joining height dimensions into single dataframe
        df_height = df_s1[1].to_frame()
        df_height = df_height.join(df_s2[1], lsuffix='1', rsuffix='2')
        df_height = df_height.join(df_s3[1])
        df_height = df_height.fillna(99999) # To convert null values into integers
        df_height = df_height.astype(int)

        # Getting minimum widths and heights from dataframe
        df_minW = df_width.min(axis=1)
        df_minH = df_height.min(axis=1)

        # Final output is datafram with minimum width and height

        dimensions = pd.concat([df_minW, df_minH], axis = 1)
        return dimensions

    def getdimensions(self, filename):
        import pandas as pd
        df = pd.read_csv(filename, header = 0)
        df = df.dropna(axis=0, subset=['Insulation Type'])
        df = df['Size'].reset_index(drop=True)

        df_split = df.str.split('-',expand=True)
        shape = df_split.shape[1]

        for i in range(1, shape+1, 1):
            globals()[f"df_s{i}"] = df_split[i-1].str.split('x',expand=True)

        df_width = pd.concat([df_s1[0]], axis=1)
        df_height = pd.concat([df_s1[1]], axis=1)

        for i in range(1, shape, 1):
            seriesW = globals()[f"df_s{i+1}"][0]
            seriesH = globals()[f"df_s{i+1}"][1]
            df_width[i] = pd.concat([seriesW], axis=1)
            df_height[i+1] = pd.concat([seriesH], axis=1)

        df_width = df_width.fillna(99999)
        df_height = df_height.fillna(99999)

        df_width = df_width.astype(int)
        df_height = df_height.astype(int)

        df_minW = df_width.min(axis=1)
        df_minH = df_height.min(axis=1)

        dimensions = pd.concat([df_minW, df_minH], axis = 1) 

        return dimensions
        

    
    def getarea(self, filename):
        import pandas as pd
        df = pd.read_csv(filename, header = 0)
        act_area = []
        area = 0
        surface_area = 0
        if df.columns.values[5] == 'Length':
            for i in range(0,len(df.iloc[:,[6]])):
                area = float(df.iat[i,6])
                surface_area = float(df.iat[i,7])
                act_area.append(max(area,surface_area))

        else:
            for i in range(0,len(df.iloc[:,[5]])):
                area = float(df.iat[i,5][:-3])
                surface_area = float(df.iat[i,6][:-3])
                act_area.append(max(area,surface_area))
        
        return act_area
    
    def getcount(self, filename):
        import pandas as pd
        df = pd.read_csv(filename, header = 0)
        counts = []

        for i in range(0,df.shape[0]):
            #counts.append(0)
            counts.append(float(df.iat[i,4]))

        return counts

    def generateoutput(self, cat_list, cost_list):
            import pandas as pd
            category_l = [1,2,3,4,5]
            rate = ['R1.0', 'R2.0', 'R3.0', 'R3.0', 'R5.0']
            out_df = pd.DataFrame(
                 {
                     'Category': category_l,
                     'Total Area': cat_list,
                     'Rate (R/m2)': rate,
                     'Cost': cost_list
                 })
            
            out_df.to_csv('Total BoQ.csv')
            out_df.to_excel('Total BoQ Excel.xlsx')

