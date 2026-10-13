import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="SmartStock AI",
    page_icon="📦",
    layout="wide",
)

st.title("📦NTHABI-SmartStock AI")
st.write("Intelligent Inventory Management System")

st.sidebar.header("Navigation")
page = st.sidebar.radio(
    "Select a page",
    ["Dashboard", "Inventory", "AI Insights"],
)

# Temporary sample inventory.
# We will connect a permanent database next.
inventory = pd.DataFrame([
    {
        "SKU": "ELEC001",
        "Product": "Laptop",
        "Category": "Electronics",
        "Quantity": 15,
        "Unit Price": 12500.00,
        "Reorder Level": 5,
    },
    {
        "SKU": "ACC001",
        "Product": "Wireless Mouse",
        "Category": "Accessories",
        "Quantity": 4,
        "Unit Price": 250.00,
        "Reorder Level": 10,
    },
    {
        "SKU": "FURN001",
        "Product": "Office Chair",
        "Category": "Furniture",
        "Quantity": 8,
        "Unit Price": 1800.00,
        "Reorder Level": 5,
    },
])

inventory["Stock Value"] = (
    inventory["Quantity"] * inventory["Unit Price"]
)

low_stock = inventory[
    inventory["Quantity"] <= inventory["Reorder Level"]
]

if page == "Dashboard":
    st.header("Business Overview")

    col1, col2, col3 = st.columns(3)

    col1.metric("Product Types", len(inventory))
    col2.metric("Total Units", int(inventory["Quantity"].sum()))
    col3.metric(
        "Inventory Value",
        f"R {inventory['Stock Value'].sum():,.2f}",
    )

    st.subheader("Inventory Value by Product")

    chart_data = inventory.set_index("Product")["Stock Value"]
    st.bar_chart(chart_data)

    st.subheader("Low-Stock Alerts")

    if low_stock.empty:
        st.success("All products have sufficient stock.")
    else:
        st.warning(f"{len(low_stock)} product(s) need attention.")
        st.dataframe(low_stock, hide_index=True)

elif page == "Inventory":
    st.header("Inventory Register")
    st.dataframe(
        inventory,
        use_container_width=True,
        hide_index=True,
    )

elif page == "AI Insights":
    st.header("Smart Stock Insights")

    st.info(
        "AI forecasting will be added after we connect "
        "the database and collect sales history."
    )

    if low_stock.empty:
        st.success("No reorder alerts based on current thresholds.")
    else:
        st.write("Products that have reached their reorder level:")

        for _, product in low_stock.iterrows():
            st.write(
                f"- **{product['Product']}**: "
                f"{product['Quantity']} units remaining; "
                f"reorder level is {product['Reorder Level']}."
            )

st.caption("SmartStock AI | Development Version 0.1")