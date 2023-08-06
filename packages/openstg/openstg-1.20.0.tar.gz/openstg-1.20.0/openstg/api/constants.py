supported_reports = {
    'instant-data': ['sync', 'reg_only'],  # PRIME code: S01
    'daily-incremental': ['async', 'reg_n_cnc'],  # PRIME code: S02
    'monthly-billing': ['async', 'reg_n_cnc'],  # PRIME code: S04
    'daily-absolute': ['async', 'reg_n_cnc'],  # PRIME code: S05
    'meter-parameters': ['async', 'reg_only'],  # PRIME code: S06
    'meter-events': ['async', 'reg_n_cnc'],  # PRIME code: S09
    'cnc-parameters': ['async', 'cnc_only'],  # PRIME code: S12
    'voltage-current-profile': ['async', 'reg_only'], # PRIME code: S14
    'cutoffs-status': ['async', 'reg_n_cnc'], # PRIME code: S18
    'advanced-instant-data': ['sync', 'reg_only'],  # PRIME code: S21
    'contract-definition': ['async', 'reg_n_cnc'],  # PRIME code: S23
    'cnc-meters': ['async', 'cnc_only'],  # PRIME code: S24
}

supported_orders = {
    'cutoff-reconnect': ['async', 'reg_only'],  # PRIME code: B03
    'order-request': ['async', 'cnc_only'],  # PRIME code: B11
}

supported_rtu_reports = {
    'get-ls-parameters-extended': ['async', 'reg_n_cnc'],  # PRIME code: G50
    'get-rtu-hourly-energy-curve': ['async', 'reg_n_cnc'],  # PRIME code: S52
    'get-ls-parameters': ['async', 'reg_n_cnc'],  # PRIME code: S56
    'get-rtu-parameters': ['async', 'reg_n_cnc'],  # PRIME code: S62
    'get-ls-voltage-current-profile': ['async', 'reg_n_cnc'],  # PRIME code: S64
}