# EDA -> 

# UI -> file upload -> 
# pandas
# matplotlib
# streamlit -> used to generate UI for Web application 

# pip install streamlit


# streamlit run file_name.py
# python -m streamlit run file_name.py


import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(layout = "wide")

st.title("Automating EDA....")

uploader = st.file_uploader(label = "Upload your DataSet : ", type = ["csv", "xlsx"])

if uploader is not None:
    # print(uploader)
    if str(uploader.name).endswith(".csv"):
        data = pd.read_csv(uploader)
        st.dataframe(data.head())

        st.subheader("ALL Columns")
        st.write(data.columns)

        st.subheader("Rows Index")
        st.write(data.index[0:])

        st.subheader("All Statistics")
        st.write(data.describe())
        
        # Missing Values
        st.subheader("Missing Values")
        missing = data.isnull().sum()
        missing_df = pd.DataFrame({
        "Missing Count": missing,
        "Missing %": (missing / len(data) * 100).round(2)
        })
        st.write(missing_df)
        st.write(f"Total missing values in dataset: {data.isnull().sum().sum()}")
        
        missing_nonzero = missing[missing > 0]
        if len(missing_nonzero) > 0:
            fig, ax = plt.subplots(figsize = (10, 4))
            missing_nonzero.sort_values().plot(kind = "barh", ax = ax, color = "tomato")
            ax.set_title("Missing Values per Column")
            ax.set_xlabel("Count")
            st.pyplot(fig)
            plt.close(fig)
        else:
            st.info("No missing values found")

        st.subheader("Correlation of Each Columns")
        corr = data.corr(numeric_only = True)
        st.write(corr)
        last_col = data.columns[-1]
        
        if len(corr) > 1:
            fig, ax = plt.subplots(figsize = (10, 8))
            im = ax.imshow(corr, cmap = "coolwarm", vmin = -1, vmax = 1)
            ax.set_xticks(range(len(corr.columns)))
            ax.set_yticks(range(len(corr.columns)))
            ax.set_xticklabels(corr.columns, rotation = 45, ha = "right")
            ax.set_yticklabels(corr.columns)
            for i in range(len(corr)):
                for j in range(len(corr)):
                    ax.text(j, i, f"{corr.iloc[i, j]:.2f}", ha = "center", va = "center", fontsize = 8)
            fig.colorbar(im, ax = ax)
            ax.set_title("Correlation Heatmap")
            st.pyplot(fig)
            plt.close(fig)

        num_cols = data.select_dtypes(include = "number").columns
        cat_cols = data.select_dtypes(exclude = "number").columns

        # Graph -> Histograms
        if st.checkbox("Show Histograms"):
            for col in num_cols:
                fig, ax = plt.subplots(figsize = (8, 5))
                ax.hist(data[col].dropna(), bins = 30, color = "steelblue", edgecolor = "white")
                ax.set_title(f"Distribution of {col}")
                ax.set_xlabel(col)
                ax.set_ylabel("Frequency")
                st.pyplot(fig)
                plt.close(fig)
                
        if st.checkbox("Show Box Plots"):
            for col in num_cols:
                fig, ax = plt.subplots(figsize = (8, 5))
                ax.boxplot(data[col].dropna(), vert = False)
                ax.set_title(f"Box Plot of {col}")
                ax.set_yticklabels([col])
                st.pyplot(fig)
                plt.close(fig)


        st.subheader("Correlation of Each Columns")
        st.write(data.corr(numeric_only = True))
        last_col = data.columns[-1]

        if st.checkbox("Check Trend"):
            for col in data.columns:  
                if data[col].dtype == "str":
                    continue
                else:      
                    plt.figure(figsize = (8, 8))
                    fig, ax = plt.subplots()
                    plt.plot(data[col][:100], data[last_col][:100], marker = "o")
                    plt.title(f"relation between {col} VS {last_col}")
                    st.pyplot(fig)
                    
                    
        # print(last_col)



    elif str(uploader.name).endswith(".xlsx"):
        data = pd.read_excel(uploader)
        st.dataframe(data.head())



    else:
        st.success("unsupported file", icon = "📈")