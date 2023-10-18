estado_financiero2021 = {}

estado_financiero2021["cuentasxcobrar"] = 629
estado_financiero2021["efectivo"] = 454
estado_financiero2021["inventarios"] = 361
estado_financiero2021["inversiones"] = 85
estado_financiero2021["depreciacionacumuladaactivosfijos"] = 2291
estado_financiero2021["equipodecomputo"] = 123
estado_financiero2021["equipodetransporte"] = 344
estado_financiero2021["maquinariayequipo"] = 1750
estado_financiero2021["mobiliarioyaccesorios"] = 448
estado_financiero2021["terrenoyedificios"] = 2590
estado_financiero2021["aportacionesparafuturosaumentosdecapital"] = 535
estado_financiero2021["capitalsocial"] = 460
estado_financiero2021["reservalegal"] = 30
estado_financiero2021["utilidadesyejerciciosanteriores"] = 1130
estado_financiero2021["costodeventas"] = 2610
estado_financiero2021["gastosdeadministracion"] = 243
estado_financiero2021["gastosdeventas"] = 125
estado_financiero2021["gastosfinancieros"] = 116
estado_financiero2021["gastospordepreciacion"] = 299
estado_financiero2021["otrosgastos"] = 44
estado_financiero2021["otrosproductos"] = 10
estado_financiero2021["productosfinancieros"] = 5
estado_financiero2021["ventas"] = 3843
estado_financiero2021["gastospreoperativos"] = 138
estado_financiero2021["acreedoresdiversos"] = 65
estado_financiero2021["cuentasporpagar"] = 478
estado_financiero2021["documentosporpagar"] = 99
estado_financiero2021["impuestos"] = 134
estado_financiero2021["hipotecasporpagarlargoplazo"] = 1279


estado_financiero2022 = {}

estado_financiero2022["cuentasxcobrar"] = 456
estado_financiero2022["efectivo"] = 393
estado_financiero2022["inventarios"] = 375
estado_financiero2022["inversiones"] = 64
estado_financiero2022["depreciacionacumuladaactivosfijos"] = 2570
estado_financiero2022["equipodecomputo"] = 120
estado_financiero2022["equipodetransporte"] = 393
estado_financiero2022["maquinariayequipo"] = 2110
estado_financiero2022["mobiliarioyaccesorios"] = 395
estado_financiero2022["terrenoyedificios"] = 2379
estado_financiero2022["aportacionesparafuturosaumentosdecapital"] = 545
estado_financiero2022["capitalsocial"] = 460
estado_financiero2022["reservalegal"] = 35
estado_financiero2022["utilidadesyejerciciosanteriores"] = 1080
estado_financiero2022["costodeventas"] = 2139
estado_financiero2022["gastosdeadministracion"] = 234
estado_financiero2022["gastosdeventas"] = 135
estado_financiero2022["gastosfinancieros"] = 114
estado_financiero2022["gastospordepreciacion"] = 279
estado_financiero2022["otrosgastos"] = 44
estado_financiero2022["otrosproductos"] = 45
estado_financiero2022["productosfinancieros"] = 10
estado_financiero2022["ventas"] = 3209
estado_financiero2022["gastospreoperativos"] = 138
estado_financiero2022["acreedoresdiversos"] = 50
estado_financiero2022["cuentasporpagar"] = 338
estado_financiero2022["documentosporpagar"] = 124
estado_financiero2022["impuestos"] = 93
estado_financiero2022["hipotecasporpagarlargoplazo"] = 1209

estado_de_resultados2021 = {
    "utilidad_bruta": estado_financiero2021["ventas"] - estado_financiero2021["costodeventas"]
}

estado_de_resultados2021["resultado_integral_financiamento"] = estado_financiero2021["gastosfinancieros"] - \
                                                               estado_financiero2021["productosfinancieros"]

estado_de_resultados2021["total_gastos_operacion"] = estado_financiero2021["gastosdeadministracion"] + \
                                                     estado_financiero2021[
                                                         "gastosdeventas"] + estado_financiero2021[
                                                         "gastospordepreciacion"] + estado_de_resultados2021[
                                                         "resultado_integral_financiamento"]
estado_de_resultados2021["utilidad_operativa"] = estado_de_resultados2021["utilidad_bruta"] - estado_de_resultados2021[
    "total_gastos_operacion"]
estado_de_resultados2021["total_otros_gastos"] = estado_financiero2021["otrosgastos"] - estado_financiero2021[
    "otrosproductos"]
estado_de_resultados2021["utilidad_antes_impuestos"] = estado_de_resultados2021["utilidad_operativa"] - \
                                                       estado_de_resultados2021["total_otros_gastos"]
estado_de_resultados2021["isr"] = estado_de_resultados2021["utilidad_antes_impuestos"] * 0.30
estado_de_resultados2021["ptu"] = estado_de_resultados2021["utilidad_antes_impuestos"] * 0.10
estado_de_resultados2021["impuestos_por_pagar"] = estado_de_resultados2021["isr"] + estado_de_resultados2021["ptu"]
estado_de_resultados2021["utilidad_del_ejercicio"] = estado_de_resultados2021["utilidad_antes_impuestos"] - \
                                                     estado_de_resultados2021["impuestos_por_pagar"]

balance_general2021 = {
    "activo_circulante": estado_financiero2021["cuentasxcobrar"] + estado_financiero2021["efectivo"] +
                         estado_financiero2021["inventarios"] + estado_financiero2021["inversiones"],
    "activo_no_circulante": estado_financiero2021["terrenoyedificios"] + estado_financiero2021["maquinariayequipo"] +
                            estado_financiero2021["equipodetransporte"] + estado_financiero2021["equipodecomputo"] +
                            estado_financiero2021["mobiliarioyaccesorios"] -
                            estado_financiero2021["depreciacionacumuladaactivosfijos"],
    "otros_activos": estado_financiero2021["gastospreoperativos"],
    "pasivo_corto_plazo": estado_financiero2021["acreedoresdiversos"] + estado_financiero2021["cuentasporpagar"] +
                          estado_financiero2021["documentosporpagar"] + estado_financiero2021["impuestos"] + estado_de_resultados2021["impuestos_por_pagar"],
    "pasivo_largo_plazo": estado_financiero2021["hipotecasporpagarlargoplazo"],
    "capital_contribuido": estado_financiero2021["capitalsocial"] + estado_financiero2021["reservalegal"] +
                           estado_financiero2021["aportacionesparafuturosaumentosdecapital"],
    "capital_ganado": estado_financiero2021["utilidadesyejerciciosanteriores"] + estado_de_resultados2021[
        "utilidad_del_ejercicio"]
}

balance_general2021["total_activos"] = balance_general2021["activo_circulante"] + balance_general2021["activo_no_circulante"] + balance_general2021["otros_activos"]
balance_general2021["total_pasivos"] = balance_general2021["pasivo_corto_plazo"] + balance_general2021["pasivo_largo_plazo"]
balance_general2021["total_capital_contable"] = balance_general2021["capital_contribuido"] + balance_general2021["capital_ganado"]


#print(estado_de_resultados2021)
#print(balance_general2021)
#print(balance_general2021["total_activos"] == (balance_general2021["total_pasivos"] + balance_general2021["total_capital_contable"]))

#**No se si asi esta bien, o si era usando .get y almacenando en valor a imprimir en una variable.
print("Balance General 2021\n")
#Mostrar Activos
print(f'Activo Circulante:$ {balance_general2021["activo_circulante"]}')
print(f'Activo No circulante:$ {balance_general2021["activo_no_circulante"]}')
print(f'Total de Activos:$ {balance_general2021["total_activos"]}\n')

#Mostrar Pasivos
print(f'Pasivos a Corto plazo:$ {balance_general2021["pasivo_corto_plazo"]}')
print(f'Pasivos a Largo plazo:$ {balance_general2021["pasivo_largo_plazo"]}')
print(f'Total de Pasivos:$ {balance_general2021["total_pasivos"]}\n')

#Mostrar Capital Contable
print(f'Capital Contribuido:$ {balance_general2021["capital_contribuido"]}')
print(f'Capital Ganado:$ {balance_general2021["capital_ganado"]}')
print(f'Total de Capital Contable:$ {balance_general2021["total_capital_contable"]}\n')

estado_de_resultados2022 = {
    "utilidad_bruta": estado_financiero2022["ventas"] - estado_financiero2022["costodeventas"]
}

estado_de_resultados2022["resultado_integral_financiamento"] = estado_financiero2022["gastosfinancieros"] - \
                                                               estado_financiero2022["productosfinancieros"]

estado_de_resultados2022["total_gastos_operacion"] = estado_financiero2022["gastosdeadministracion"] + \
                                                     estado_financiero2022[
                                                         "gastosdeventas"] + estado_financiero2022[
                                                         "gastospordepreciacion"] + estado_de_resultados2022[
                                                         "resultado_integral_financiamento"]
estado_de_resultados2022["utilidad_operativa"] = estado_de_resultados2022["utilidad_bruta"] - estado_de_resultados2022[
    "total_gastos_operacion"]
estado_de_resultados2022["total_otros_gastos"] = estado_financiero2022["otrosgastos"] - estado_financiero2022[
    "otrosproductos"]
estado_de_resultados2022["utilidad_antes_impuestos"] = estado_de_resultados2022["utilidad_operativa"] - \
                                                       estado_de_resultados2022["total_otros_gastos"]
estado_de_resultados2022["isr"] = estado_de_resultados2022["utilidad_antes_impuestos"] * 0.30
estado_de_resultados2022["ptu"] = estado_de_resultados2022["utilidad_antes_impuestos"] * 0.10
estado_de_resultados2022["impuestos_por_pagar"] = estado_de_resultados2022["isr"] + estado_de_resultados2022["ptu"]
estado_de_resultados2022["utilidad_del_ejercicio"] = estado_de_resultados2022["utilidad_antes_impuestos"] - \
                                                     estado_de_resultados2022["impuestos_por_pagar"]

balance_general2022 = {
    "activo_circulante": estado_financiero2022["cuentasxcobrar"] + estado_financiero2022["efectivo"] +
                         estado_financiero2022["inventarios"] + estado_financiero2022["inversiones"],
    "activo_no_circulante": estado_financiero2022["terrenoyedificios"] + estado_financiero2022["maquinariayequipo"] +
                            estado_financiero2022["equipodetransporte"] + estado_financiero2022["equipodecomputo"] +
                            estado_financiero2022["mobiliarioyaccesorios"] -
                            estado_financiero2022["depreciacionacumuladaactivosfijos"],
    "otros_activos": estado_financiero2022["gastospreoperativos"],
    "pasivo_corto_plazo": estado_financiero2022["acreedoresdiversos"] + estado_financiero2022["cuentasporpagar"] +
                          estado_financiero2022["documentosporpagar"] + estado_financiero2022["impuestos"] + estado_de_resultados2022["impuestos_por_pagar"],
    "pasivo_largo_plazo": estado_financiero2022["hipotecasporpagarlargoplazo"],
    "capital_contribuido": estado_financiero2022["capitalsocial"] + estado_financiero2022["reservalegal"] +
                           estado_financiero2022["aportacionesparafuturosaumentosdecapital"],
    "capital_ganado": estado_financiero2022["utilidadesyejerciciosanteriores"] + estado_de_resultados2022[
        "utilidad_del_ejercicio"]
}

balance_general2022["total_activos"] = balance_general2022["activo_circulante"] + balance_general2022["activo_no_circulante"] + balance_general2022["otros_activos"]
balance_general2022["total_pasivos"] = balance_general2022["pasivo_corto_plazo"] + balance_general2022["pasivo_largo_plazo"]
balance_general2022["total_capital_contable"] = balance_general2022["capital_contribuido"] + balance_general2022["capital_ganado"]


#print(estado_de_resultados2022)
#print(balance_general2022)
#print(balance_general2022["total_activos"] == (balance_general2022["total_pasivos"] + balance_general2022["total_capital_contable"]))

print("Balance General 2022\n")
#Mostrar Activos
print(f'Activo Circulante:$ {balance_general2022["activo_circulante"]}')
print(f'Activo No circulante:$ {balance_general2022["activo_no_circulante"]}')
print(f'Total de Activos:$ {balance_general2022["total_activos"]}\n')

#Mostrar Pasivos
print(f'Pasivos a Corto plazo:$ {balance_general2022["pasivo_corto_plazo"]}')
print(f'Pasivos a Largo plazo:$ {balance_general2022["pasivo_largo_plazo"]}')
print(f'Total de Pasivos:$ {balance_general2022["total_pasivos"]}\n')

#Mostrar Capital Contable
print(f'Capital Contribuido:$ {balance_general2022["capital_contribuido"]}')
print(f'Capital Ganado:$ {balance_general2022["capital_ganado"]}')
print(f'Total de Capital Contable:$ {balance_general2022["total_capital_contable"]}\n')