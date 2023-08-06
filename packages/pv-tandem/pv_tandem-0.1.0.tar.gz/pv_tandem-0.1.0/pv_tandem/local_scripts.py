# -*- coding: utf-8 -*-

import pandas as pd

import pv_tandem



# df = pd.read_csv('data/2020-702799-fixed_tilt.csv', skiprows=2)
# meta_data = pd.read_csv('data/2020-702799-fixed_tilt.csv', nrows=1).iloc[0]

# spec_irrad_ts = df.loc[:,df.columns.to_series().str.contains(' um')]
# meta_ts = df.loc[:,~df.columns.to_series().str.contains(' um')]

# spec_irrad_ts.columns = spec_irrad_ts.columns.to_series().str.extract('([\d.]*) um', expand=False).astype(float)
# spec_irrad_ts = spec_irrad_ts.loc[:,:1250]
# spec_irrad_ts = spec_irrad_ts.loc[meta_ts['Solar Zenith Angle']>0]

# meta_ts = meta_ts.loc[meta_ts['Solar Zenith Angle']>0]
# meta_ts['dt'] = pd.to_datetime(meta_ts[['Year', 'Month', 'Day', 'Hour', 'Minute']])

# spec_irrad_ts.index = meta_ts['dt']

# spec_irrad_ts.columns = spec_irrad_ts.columns * 1000
# spec_irrad_ts = spec_irrad_ts.loc[:,300:1200:5]

# spec_irrad_ts.to_csv('./data/spec_poa_dallas_2020.csv')

# meta_ts = meta_ts.set_index('dt')
# meta_ts.to_csv('./data/meta_ts_dallas_2020.csv')

if __name__ == "__main__":

    spec = pd.read_csv("../examples/data/tiny_spec.csv", index_col=0)
    spec.columns = spec.columns.astype(float)
    eqe = pd.read_csv("../examples/data/eqe_tandem_2t.csv", index_col=0)

    eqe_new = pv_tandem.utils.interp_eqe_to_spec(eqe, spec)
    eqe.plot()