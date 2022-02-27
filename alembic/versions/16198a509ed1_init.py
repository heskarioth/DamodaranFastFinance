"""init

Revision ID: 16198a509ed1
Revises: 
Create Date: 2022-02-25 15:56:30.136900

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '16198a509ed1'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('backend_schedules',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('datafeed_name', sa.String(), nullable=False),
    sa.Column('lastupdate_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.Column('datefeed_url', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('backend_users',
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('password', sa.String(), nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.Column('role', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('email')
    )
    op.create_table('betas',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('industry_name', sa.String(), nullable=False),
    sa.Column('number_of_firms', sa.Integer(), nullable=False),
    sa.Column('beta', sa.Float(), nullable=False),
    sa.Column('debt_to_equity_ratio_percentage', sa.Float(), nullable=False),
    sa.Column('effective_tax_rate_percentage', sa.Float(), nullable=False),
    sa.Column('unlevered_beta', sa.Float(), nullable=False),
    sa.Column('cash_to_firm_value_percentage', sa.Float(), nullable=False),
    sa.Column('unlevered_beta_corrected_for_cash', sa.Float(), nullable=False),
    sa.Column('hilo_risk_percentage', sa.Float(), nullable=False),
    sa.Column('std_of_equity_percentage', sa.Float(), nullable=False),
    sa.Column('std_in_operating_income_last_10_years', sa.Float(), nullable=False),
    sa.Column('year_2018', sa.Float(), nullable=False),
    sa.Column('year_2019', sa.Float(), nullable=False),
    sa.Column('year_2020', sa.Float(), nullable=False),
    sa.Column('year_2021', sa.Float(), nullable=False),
    sa.Column('average_2017_22', sa.Float(), nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('capex',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('industry_name', sa.String(), nullable=False),
    sa.Column('number_of_firms', sa.Integer(), nullable=False),
    sa.Column('capital_expenditures_in_usd_millions', sa.Float(), nullable=False),
    sa.Column('depreciation_and_ammortization_in_usd_millions', sa.Float(), nullable=False),
    sa.Column('cap_ex_deprecn_in_percentage', sa.Float(), nullable=False),
    sa.Column('acquisitions_in_usd_millions', sa.Float(), nullable=False),
    sa.Column('net_r_d_in_usd_millions', sa.Float(), nullable=False),
    sa.Column('net_cap_exp_divided_by_sales_percentage', sa.Float(), nullable=False),
    sa.Column('net_cap_ex_divided_by_ebit_1_minus_t', sa.Float(), nullable=False),
    sa.Column('sales_invested_capital_ratio', sa.Float(), nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('countrytaxrates',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('country', sa.String(), nullable=False),
    sa.Column('year_2016_percentage', sa.Float(), nullable=False),
    sa.Column('year_2017_percentage', sa.Float(), nullable=False),
    sa.Column('year_2018_percentage', sa.Float(), nullable=False),
    sa.Column('year_2019_percentage', sa.Float(), nullable=False),
    sa.Column('year_2020_percentage', sa.Float(), nullable=False),
    sa.Column('year_2021_percentage', sa.Float(), nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('ctryprem',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('country', sa.String(), nullable=False),
    sa.Column('moodys_rating', sa.String(), nullable=False),
    sa.Column('adj_default_spread', sa.Float(), nullable=False),
    sa.Column('country_risk_premium', sa.Float(), nullable=False),
    sa.Column('equity_risk_premium', sa.Float(), nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('dbtfund',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('industry_name', sa.String(), nullable=False),
    sa.Column('number_of_firms', sa.Integer(), nullable=False),
    sa.Column('book_deposit_to_capital_percentage', sa.Float(), nullable=False),
    sa.Column('market_debt_to_capital_unadjusted_percentage', sa.Float(), nullable=False),
    sa.Column('market_debt_equity_unadjusted_percentage', sa.Float(), nullable=False),
    sa.Column('market_debt_to_capital_adjusted_for_leases_percentage', sa.Float(), nullable=False),
    sa.Column('market_debt_equity_adjusted_for_leases_percentage', sa.Float(), nullable=False),
    sa.Column('effective_tax_rate_percentage', sa.Float(), nullable=False),
    sa.Column('institutional_holdings_percentage', sa.Float(), nullable=False),
    sa.Column('std_dev_in_stock_prices_percentage', sa.Float(), nullable=False),
    sa.Column('ebitda_divided_by_ev_percentage', sa.Float(), nullable=False),
    sa.Column('net_ppe_divided_by_total_assets_percentage', sa.Float(), nullable=False),
    sa.Column('capital_spending_divided_by_total_assets_percentage', sa.Float(), nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('debtdetails',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('industry_name', sa.String(), nullable=False),
    sa.Column('number_of_firms', sa.Integer(), nullable=False),
    sa.Column('lease_debt_my_estimate_usd', sa.Float(), nullable=False),
    sa.Column('conventional_debt_usd', sa.Float(), nullable=False),
    sa.Column('total_debt_with_leases_usd', sa.Float(), nullable=False),
    sa.Column('interest_expense_usd', sa.Float(), nullable=False),
    sa.Column('book_interest_rate_percentage', sa.Float(), nullable=False),
    sa.Column('short_term_debt_as_percentage_of_total_debt', sa.Float(), nullable=False),
    sa.Column('lease_debt_accounting_usd', sa.Float(), nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('divfcfe',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('industry_name', sa.String(), nullable=False),
    sa.Column('number_of_firms', sa.Integer(), nullable=False),
    sa.Column('dividends', sa.Float(), nullable=False),
    sa.Column('net_income_usd', sa.Float(), nullable=False),
    sa.Column('payout_in_percentage', sa.Float(), nullable=False),
    sa.Column('dividends_plus_buybacks_usd', sa.Float(), nullable=False),
    sa.Column('cash_returns_as_percentage_of_net_income', sa.Float(), nullable=False),
    sa.Column('dividends_plus_buybacks_minus_stock_issuances_usd', sa.Float(), nullable=False),
    sa.Column('fcfe_before_debt_cash_flows_usd', sa.Float(), nullable=False),
    sa.Column('fcfe_after_debt_cash_flows_usd', sa.Float(), nullable=False),
    sa.Column('net_cash_returned_fcfe_pre_debt_percentage', sa.Float(), nullable=False),
    sa.Column('net_cash_returned_divided_by_fcfe_post_debt_percentage', sa.Float(), nullable=False),
    sa.Column('cash_divided_by_frim_value_percentage', sa.Float(), nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('divfund',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('industry_name', sa.String(), nullable=False),
    sa.Column('number_of_firms', sa.Integer(), nullable=False),
    sa.Column('total_dividends_usd_millions', sa.Float(), nullable=False),
    sa.Column('special_dividends_as_percentage_of_total_dividends', sa.Float(), nullable=False),
    sa.Column('dividend_payout_percentage', sa.Float(), nullable=False),
    sa.Column('dividend_yield_percentage', sa.Float(), nullable=False),
    sa.Column('market_cap_usd_millions', sa.Float(), nullable=False),
    sa.Column('roe_percentage', sa.Float(), nullable=False),
    sa.Column('institutional_holdings_percentage', sa.Float(), nullable=False),
    sa.Column('std_dev_in_stock_prices', sa.Float(), nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('finflows',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('industry_name', sa.String(), nullable=False),
    sa.Column('number_of_firms', sa.Integer(), nullable=False),
    sa.Column('dividends_in_usd_millions', sa.Float(), nullable=False),
    sa.Column('buybacks_in_usd_millions', sa.Float(), nullable=False),
    sa.Column('equity_issuance_in_usd_millions', sa.Float(), nullable=False),
    sa.Column('net_equity_change_in_usd_millions', sa.Float(), nullable=False),
    sa.Column('net_equity_change_as_percentage_of_book_equity', sa.Float(), nullable=False),
    sa.Column('debt_repaid_in_usd_millions', sa.Float(), nullable=False),
    sa.Column('debt_raised_in_usd_millions', sa.Float(), nullable=False),
    sa.Column('net_debt_change_in_usd_millions', sa.Float(), nullable=False),
    sa.Column('net_change_in_debt_as_percentage_of_total_debt', sa.Float(), nullable=False),
    sa.Column('change_in_lease_debt_in_usd_millions', sa.Float(), nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('fundgr',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('industry_name', sa.String(), nullable=False),
    sa.Column('number_of_firms', sa.Integer(), nullable=False),
    sa.Column('retention_rate_percentage', sa.Float(), nullable=False),
    sa.Column('fundamental_growth_percentage', sa.Float(), nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('fundgrEB',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('industry_name', sa.String(), nullable=False),
    sa.Column('number_of_firms', sa.Integer(), nullable=False),
    sa.Column('roc_percentage', sa.Float(), nullable=False),
    sa.Column('reinvestment_rate_percentage', sa.Float(), nullable=False),
    sa.Column('expected_growth_in_ebit_percentage', sa.Float(), nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('goodwill',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('industry_name', sa.String(), nullable=False),
    sa.Column('number_of_firms', sa.Integer(), nullable=False),
    sa.Column('goodwill_in_usd_millions', sa.Float(), nullable=False),
    sa.Column('change_in_goodwill_in_last_year_in_millions', sa.Float(), nullable=False),
    sa.Column('goodwill_as_percentage_of_total_asset', sa.Float(), nullable=False),
    sa.Column('impairment_of_goodwill_in_ltm_in_usd_millions', sa.Float(), nullable=False),
    sa.Column('impairment_as_percentage_of_goodwill', sa.Float(), nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('histgr',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('industry_name', sa.String(), nullable=False),
    sa.Column('number_of_firms', sa.Integer(), nullable=False),
    sa.Column('cagr_in_net_income_last_5_years_percentage', sa.Float(), nullable=False),
    sa.Column('cagr_in_revenues_last_5_years_percentage', sa.Float(), nullable=False),
    sa.Column('expected_growth_in_revenues_next_2_years_percentage', sa.Float(), nullable=False),
    sa.Column('expected_growth_in_eps_next_5_years_percentage', sa.Float(), nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('histimpl',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('year', sa.Integer(), nullable=False),
    sa.Column('earnings_yield_percentage', sa.Float(), nullable=False),
    sa.Column('dividend_yield_percentage', sa.Float(), nullable=False),
    sa.Column('sp_500', sa.Float(), nullable=False),
    sa.Column('earnings', sa.Float(), nullable=False),
    sa.Column('dividends', sa.Float(), nullable=False),
    sa.Column('dividends_plus_buybacks', sa.Float(), nullable=False),
    sa.Column('change_in_earnings_percentage', sa.Float(), nullable=False),
    sa.Column('change_in_dividends_percentage', sa.Float(), nullable=False),
    sa.Column('t_bill_rate_percentage', sa.Float(), nullable=False),
    sa.Column('t_bond_rate_percentage', sa.Float(), nullable=False),
    sa.Column('bond_bill', sa.Float(), nullable=False),
    sa.Column('smoothed_growth_percentage', sa.Float(), nullable=False),
    sa.Column('implied_premium_ddm_percentage', sa.Float(), nullable=False),
    sa.Column('analytst_growth_estimate_percentage', sa.Float(), nullable=False),
    sa.Column('impled_erp_for_fcfe_percentage', sa.Float(), nullable=False),
    sa.Column('implied_premium_for_fcfe_with_sustainable_payout_percentage', sa.Float(), nullable=False),
    sa.Column('erp_riskfree_rate', sa.Float(), nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('histretSP',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('year', sa.Integer(), nullable=False),
    sa.Column('annual_roi_in_sp_500_includes_dividend_percentage', sa.Float(), nullable=False),
    sa.Column('annual_roi_in_3_month_t_bill_percentage', sa.Float(), nullable=False),
    sa.Column('annual_roi_in_us_t_bond_percentage', sa.Float(), nullable=False),
    sa.Column('annual_roi_in_baa_corporate_bond_percentage', sa.Float(), nullable=False),
    sa.Column('annual_roi_in_real_estate_percentage', sa.Float(), nullable=False),
    sa.Column('value_of_100_usd_invested_in_1928_sp_500_includes_dividends_usd', sa.Float(), nullable=False),
    sa.Column('value_of_100_usd_invested_in_1928_sp_3_moth_t_bill_4_usd', sa.Float(), nullable=False),
    sa.Column('value_of_100_usd_invested_in_1928_sp_us_t_bond_usd', sa.Float(), nullable=False),
    sa.Column('value_of_100_usd_invested_in_1928_sp_baa_corporate_bond_usd', sa.Float(), nullable=False),
    sa.Column('annual_risk_premium_real_estate_usd', sa.Float(), nullable=False),
    sa.Column('annual_risk_premium_stocks_minus_bills_percentage', sa.Float(), nullable=False),
    sa.Column('annual_risk_premium_stocks_minus_bonds_percentage', sa.Float(), nullable=False),
    sa.Column('annual_risk_premium_stocks_minus_baa_corporate_bond_percentage', sa.Float(), nullable=False),
    sa.Column('annual_risk_premium_historical_risk_premium_percentage', sa.Float(), nullable=False),
    sa.Column('inflation_rate_percentage', sa.Float(), nullable=False),
    sa.Column('annual_real_returns_on_sp_500_includes_dividend_percentage', sa.Float(), nullable=False),
    sa.Column('annual_real_returns_on_three_month_t_bill_real_percentage', sa.Float(), nullable=False),
    sa.Column('annual_real_returns_on_zero_year_t_bonds_percentage', sa.Float(), nullable=False),
    sa.Column('annual_real_returns_on_baa_corporate_bonds_percentage', sa.Float(), nullable=False),
    sa.Column('annual_real_returns_on_real_estate_percentage', sa.Float(), nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('inhold',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('industry_name', sa.String(), nullable=False),
    sa.Column('number_of_firms', sa.Integer(), nullable=False),
    sa.Column('ceo_holding', sa.Float(), nullable=False),
    sa.Column('institutional_holdings', sa.Float(), nullable=False),
    sa.Column('insider_holdings', sa.Float(), nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('leaseeffect',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('industry_name', sa.String(), nullable=False),
    sa.Column('number_of_firms', sa.Integer(), nullable=False),
    sa.Column('lease_expenses_divided_by_sales_percentage', sa.Float(), nullable=False),
    sa.Column('total_debt_without_leases_usd', sa.Float(), nullable=False),
    sa.Column('lease_debt_as_percentage_of_total_debt', sa.Float(), nullable=False),
    sa.Column('market_debt_to_capital_without_leases_percentage', sa.Float(), nullable=False),
    sa.Column('market_debt_to_capital_with_leases_percentage', sa.Float(), nullable=False),
    sa.Column('book_debt_to_capital_without_leases_percentage', sa.Float(), nullable=False),
    sa.Column('book_debt_to_capital_with_leases_percentage', sa.Float(), nullable=False),
    sa.Column('operating_income_before_lease_adj_usd', sa.Float(), nullable=False),
    sa.Column('operating_income_after_lease_adj_usd', sa.Float(), nullable=False),
    sa.Column('roic_without_leases_percentage', sa.Float(), nullable=False),
    sa.Column('roic_with_leases_percentage', sa.Float(), nullable=False),
    sa.Column('pre_tax_operating_margin_before_lease_adj_percentage', sa.Float(), nullable=False),
    sa.Column('pre_tax_operating_margin_after_lease_adj', sa.Float(), nullable=False),
    sa.Column('lease_debt_my_estimate_usd', sa.Float(), nullable=False),
    sa.Column('lease_debt_accounting_usd', sa.Float(), nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('macro',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date', sa.Integer(), nullable=False),
    sa.Column('t_bond_rate_percentage', sa.Float(), nullable=False),
    sa.Column('change_in_rete_percentage', sa.Float(), nullable=False),
    sa.Column('real_gdp', sa.Float(), nullable=False),
    sa.Column('percentage_chg_in_gdp', sa.Float(), nullable=False),
    sa.Column('cpi_percentage', sa.Float(), nullable=False),
    sa.Column('change_in_cpi', sa.Float(), nullable=False),
    sa.Column('weighted_dollar', sa.Float(), nullable=False),
    sa.Column('percentage_change_in_dollar', sa.Float(), nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('margin',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('industry_name', sa.String(), nullable=False),
    sa.Column('number_of_firms', sa.Integer(), nullable=False),
    sa.Column('gross_margin_percentage', sa.Float(), nullable=False),
    sa.Column('net_margin_percentage', sa.Float(), nullable=False),
    sa.Column('pre_tax_pre_stock_compensation_operating_margin_percentage', sa.Float(), nullable=False),
    sa.Column('pre_tax_unadjusted_operating_margin_percentage', sa.Float(), nullable=False),
    sa.Column('after_tax_unadjusted_operating_margin_percentage', sa.Float(), nullable=False),
    sa.Column('pre_tax_lease_adjusted_margin_percentage', sa.Float(), nullable=False),
    sa.Column('after_tax_lease_adjusted_margin_percentage', sa.Float(), nullable=False),
    sa.Column('pre_tax_lease_r_d_adj_margin_percentage', sa.Float(), nullable=False),
    sa.Column('after_tax_lease_and_r_d_adj_margin_percentage', sa.Float(), nullable=False),
    sa.Column('ebitda_divided_by_sales_percentage', sa.Float(), nullable=False),
    sa.Column('ebitda_sga_dividend_by_sales_percentage', sa.Float(), nullable=False),
    sa.Column('ebitda_r_d_divided_by_sales_percentage', sa.Float(), nullable=False),
    sa.Column('cogs_divided_by_sales_percentage', sa.Float(), nullable=False),
    sa.Column('r_d_divided_by_sales', sa.Float(), nullable=False),
    sa.Column('sga_divided_by_sales_percentage', sa.Float(), nullable=False),
    sa.Column('stock_based_compensation_divided_by_sales_percentage', sa.Float(), nullable=False),
    sa.Column('lease_expense_divided_by_sales_percentage', sa.Float(), nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('r_d',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('industry_name', sa.String(), nullable=False),
    sa.Column('number_of_firms', sa.Integer(), nullable=False),
    sa.Column('r_d_capitalized_my_estimate_in_millions', sa.Float(), nullable=False),
    sa.Column('capitalized_r_d_as_percentage_of_invested_capital', sa.Float(), nullable=False),
    sa.Column('r_d_ltm_in_millions', sa.Float(), nullable=False),
    sa.Column('current_r_d_as_percentage_of_revenue', sa.Float(), nullable=False),
    sa.Column('r_d_one_year_ago_in_usd_millions', sa.Float(), nullable=False),
    sa.Column('r_d_two_years_ago_in_usd_millions', sa.Float(), nullable=False),
    sa.Column('r_d_three_years_ago_in_usd_millions', sa.Float(), nullable=False),
    sa.Column('r_d_four_years_ago_in_usd_millions', sa.Float(), nullable=False),
    sa.Column('r_d_five_years_ago_in_usd_millions', sa.Float(), nullable=False),
    sa.Column('cagr_in_r_d_last_five_years_in_percentage', sa.Float(), nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('roe',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('industry_name', sa.String(), nullable=False),
    sa.Column('number_of_firms', sa.Integer(), nullable=False),
    sa.Column('roe_unadjusted', sa.Float(), nullable=False),
    sa.Column('roe_adjusted_for_r_and_d', sa.Float(), nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('taxrate',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('industry_name', sa.String(), nullable=False),
    sa.Column('number_of_firms', sa.Integer(), nullable=False),
    sa.Column('total_taxable_income_usd', sa.Float(), nullable=False),
    sa.Column('taxes_total_taxes_paid_accrual_usd', sa.Float(), nullable=False),
    sa.Column('taxes_total_cash_taxes_paid_usd', sa.Float(), nullable=False),
    sa.Column('cash_taxes_divided_by_accrual_taxes_percentage', sa.Float(), nullable=False),
    sa.Column('effect_tax_rates_avg_all_companies_percent', sa.Float(), nullable=False),
    sa.Column('effect_tax_rates_avg_money_making_firms_percent', sa.Float(), nullable=False),
    sa.Column('effect_tax_rates_aggregate_tax_rate_percentage', sa.Float(), nullable=False),
    sa.Column('cash_tax_rates_avg_money_making_firms_percent', sa.Float(), nullable=False),
    sa.Column('cash_tax_rates_aggregate_tax_rate_percentage', sa.Float(), nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('totalbeta',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('industry_name', sa.String(), nullable=False),
    sa.Column('number_of_firms', sa.Integer(), nullable=False),
    sa.Column('average_unlevered_beta', sa.Float(), nullable=False),
    sa.Column('average_levered_beta', sa.Float(), nullable=False),
    sa.Column('average_correlation_with_market_percentage', sa.Float(), nullable=False),
    sa.Column('total_unlevered_beta', sa.Float(), nullable=False),
    sa.Column('total_levered_beta', sa.Float(), nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('wacc',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('industry_name', sa.String(), nullable=False),
    sa.Column('number_of_firms', sa.Integer(), nullable=False),
    sa.Column('beta', sa.Float(), nullable=False),
    sa.Column('cost_of_equity_percentage', sa.Float(), nullable=False),
    sa.Column('equity_divided_by_debt_plus_equity_percentage', sa.Float(), nullable=False),
    sa.Column('std_dev_in_stock_percentage', sa.Float(), nullable=False),
    sa.Column('cost_of_debt_percentage', sa.Float(), nullable=False),
    sa.Column('tax_rate_percentage', sa.Float(), nullable=False),
    sa.Column('after_tax_cost_of_debt_percentage', sa.Float(), nullable=False),
    sa.Column('debt_divided_by_debt_plus_equity_percentage', sa.Float(), nullable=False),
    sa.Column('cost_of_capital_percentage', sa.Float(), nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('wcdata',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('industry_name', sa.String(), nullable=False),
    sa.Column('number_of_firms', sa.Integer(), nullable=False),
    sa.Column('accounts_receivable_sales', sa.Float(), nullable=False),
    sa.Column('inventory_sales', sa.Float(), nullable=False),
    sa.Column('accounts_payable_sales', sa.Float(), nullable=False),
    sa.Column('non_cash_wc_sales', sa.Float(), nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('wcdata')
    op.drop_table('wacc')
    op.drop_table('totalbeta')
    op.drop_table('taxrate')
    op.drop_table('roe')
    op.drop_table('r_d')
    op.drop_table('margin')
    op.drop_table('macro')
    op.drop_table('leaseeffect')
    op.drop_table('inhold')
    op.drop_table('histretSP')
    op.drop_table('histimpl')
    op.drop_table('histgr')
    op.drop_table('goodwill')
    op.drop_table('fundgrEB')
    op.drop_table('fundgr')
    op.drop_table('finflows')
    op.drop_table('divfund')
    op.drop_table('divfcfe')
    op.drop_table('debtdetails')
    op.drop_table('dbtfund')
    op.drop_table('ctryprem')
    op.drop_table('countrytaxrates')
    op.drop_table('capex')
    op.drop_table('betas')
    op.drop_table('backend_users')
    op.drop_table('backend_schedules')
    # ### end Alembic commands ###
