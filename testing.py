from tabulate import tabulate

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
                          estado_financiero2021["documentosporpagar"] + estado_financiero2021["impuestos"] +
                          estado_de_resultados2021["impuestos_por_pagar"],
    "pasivo_largo_plazo": estado_financiero2021["hipotecasporpagarlargoplazo"],
    "capital_contribuido": estado_financiero2021["capitalsocial"] + estado_financiero2021["reservalegal"] +
                           estado_financiero2021["aportacionesparafuturosaumentosdecapital"],
    "capital_ganado": estado_financiero2021["utilidadesyejerciciosanteriores"] + estado_de_resultados2021[
        "utilidad_del_ejercicio"]
}

balance_general2021["total_activos"] = balance_general2021["activo_circulante"] + balance_general2021[
    "activo_no_circulante"] + balance_general2021["otros_activos"]
balance_general2021["total_pasivos"] = balance_general2021["pasivo_corto_plazo"] + balance_general2021[
    "pasivo_largo_plazo"]
balance_general2021["total_capital_contable"] = balance_general2021["capital_contribuido"] + balance_general2021[
    "capital_ganado"]

tabla_er2021 = [[" ESTADO DE RESULTADOS 2021 ","","","",""],
                ["","1","2","3","4"],
                ["Ventas","","","",f"${estado_financiero2021['ventas']}"],
                ["Costo de Ventas","","","",f"${estado_financiero2021['costodeventas']}"],
                ["","","","Utilidad Bruta",f"${estado_de_resultados2021['utilidad_bruta']}"],
                ["","","","",""],
                ["Gastos de venta","","",f"${estado_financiero2021['gastosdeventas']}",""],
                ["Gastos de Administracion","","",f"${estado_financiero2021['gastosdeadministracion']}",""],
                ["Gastos x Depreciación","","",f"${estado_financiero2021['gastospordepreciacion']}",""],
                ["Gastos Financieros","",f"${estado_financiero2021['gastosfinancieros']}","",""],
                ["Productos Financieros","",f"${estado_financiero2021['productosfinancieros']}","",""],
                ["Resul. Intgrl d Finan.","",f"${estado_de_resultados2021['resultado_integral_financiamento']}","",""],
                ["","","","Total de Gastos Operativos",f"${estado_de_resultados2021['total_gastos_operacion']}"],
                ["","","","Utilidad Operativa",f"${estado_de_resultados2021['utilidad_operativa']}"],
                ["","","","",""],
                ["Otros Gastos","","",f"${estado_financiero2021['otrosgastos']}",""],
                ["Otros Productos","","",f"${estado_financiero2021['otrosproductos']}",""],
                ["","","","Total de Otros Gastos y Productos",f"${estado_de_resultados2021['total_otros_gastos']}"],
                ["","","","Utilidad Antes de Impuestos",f"${estado_de_resultados2021['utilidad_antes_impuestos']}"],
                ["","","","",""],
                ["ISR","","30%",f"${estado_de_resultados2021['isr']}",""],
                ["PTU","","10%",f"${estado_de_resultados2021['ptu']}",""],
                ["","","","Total de Impuestos x Pagar",f"${estado_de_resultados2021['impuestos_por_pagar']}"],
                ["","","","Utilidad Neta del Ejercicio",f"${estado_de_resultados2021['utilidad_del_ejercicio']}"]
                ]

tabla_bg2021 = [["BALANCE GENERAL 2021", "", "", "", ""],
                ["Efectivo", "", f"${estado_financiero2021['efectivo']:,.2f}", "", ""],
                ["Cuentas por Cobrar", "", f"${estado_financiero2021['cuentasxcobrar']:,.2f}", "", ""],
                ["Inventarios", "", f"${estado_financiero2021['inventarios']:,.2f}", "", ""],
                ["Inversiones", "", f"${estado_financiero2021['inversiones']:,.2f}",
                 f"${balance_general2021['activo_circulante']:,.2f}", ""],
                ["", "", "", "", ""],
                ["Terrenos y Edificios", "", f"${estado_financiero2021['terrenoyedificios']:,.2f}", "", ""],
                ["Maq. y Equipo", "", f"${estado_financiero2021['maquinariayequipo']:,.2f}", "", ""],
                ["Mobiliario y Accesorios", "", f"${estado_financiero2021['mobiliarioyaccesorios']:,.2f}", "", ""],
                ["Eq. de Computo", "", f"${estado_financiero2021['equipodecomputo']:,.2f}", "", ""],
                ["Eq. de Transporte", "", f"${estado_financiero2021['equipodetransporte']:,.2f}", "", ""],
                ["Depr. Acumulada de Activos Fijos", "",
                 f"${estado_financiero2021['depreciacionacumuladaactivosfijos']:,.2f}",
                 f"${balance_general2021['activo_no_circulante']:,.2f}", ""],
                ["", "", "", "", ""],
                ["Gastos Preoperatorios", "", f"${estado_financiero2021['gastospreoperativos']:,.2f}",
                 f"${balance_general2021['otros_activos']:,.2f}", ""],
                ["", "", "", "Total Activos", f"${balance_general2021['total_activos']:,.2f}"],
                ["Acreedores Diversos", "", f"${estado_financiero2021['acreedoresdiversos']:,.2f}", "", ""],
                ["Cuentas por pagar", "", f"${estado_financiero2021['cuentasporpagar']:,.2f}", "", ""],
                ["Documentos por pagar", "", f"${estado_financiero2021['documentosporpagar']:,.2f}", "", ""],
                ["Impuestos", "", f"${estado_financiero2021['impuestos']:,.2f}",
                 f"${balance_general2021['pasivo_corto_plazo']:,.2f}", ""],
                ["", "", "", "", ""],
                ["Hipotecas por pagar a largo plazo", "",
                 f"${estado_financiero2021['hipotecasporpagarlargoplazo']:,.2f}",
                 f"${balance_general2021['pasivo_largo_plazo']:,.2f}", ""],
                ["", "", "", "Total Pasivos", f"${balance_general2021['total_pasivos']:,.2f}"],
                ["Capital Social", "", f"${estado_financiero2021['capitalsocial']:,.2f}", "", ""],
                ["Reserva Legal", "", f"${estado_financiero2021['reservalegal']:,.2f}", "", ""],
                ["Aportaciones para futuros aumentos de capital", "",
                 f"${estado_financiero2021['aportacionesparafuturosaumentosdecapital']:,.2f}",
                 f"${balance_general2021['capital_contribuido']:,.2f}", ""],
                ["", "", "", "", ""],
                ["Utilidades ejercicios anteriores", "",
                 f"${estado_financiero2021['utilidadesyejerciciosanteriores']:,.2f}", "", ""],
                ["Utilidad del ejercicio", "", f"${estado_de_resultados2021['utilidad_del_ejercicio']:,.2f}",
                 f"${balance_general2021['capital_ganado']:,.2f}", ""],
                ["", "", "", "Total Capital Contable", f"${balance_general2021['total_capital_contable']:,.2f}"]]

estado_de_resultados2022 = {
    "utilidad_bruta": estado_financiero2022["ventas"] - estado_financiero2022["costodeventas"]
}

estado_de_resultados2022["resultado_integral_financiamento"] = estado_financiero2022["gastosfinancieros"] - \
                                                               estado_financiero2022["productosfinancieros"]

estado_de_resultados2022["total_gastos_operacion"] = (
        estado_financiero2022["gastosdeadministracion"] + estado_financiero2022["gastosdeventas"] +
        estado_financiero2022["gastospordepreciacion"] + estado_de_resultados2022["resultado_integral_financiamento"]
)
estado_de_resultados2022["utilidad_operativa"] = estado_de_resultados2022["utilidad_bruta"] - estado_de_resultados2022[
    "total_gastos_operacion"]
estado_de_resultados2022["total_otros_gastos"] = (
        estado_financiero2022["otrosgastos"] - estado_financiero2022["otrosproductos"]
)
estado_de_resultados2022["utilidad_antes_impuestos"] = estado_de_resultados2022["utilidad_operativa"] - \
                                                       estado_de_resultados2022["total_otros_gastos"]
estado_de_resultados2022["isr"] = estado_de_resultados2022["utilidad_antes_impuestos"] * 0.30
estado_de_resultados2022["ptu"] = round(estado_de_resultados2022["utilidad_antes_impuestos"] * 0.10,2)
estado_de_resultados2022["impuestos_por_pagar"] = round(estado_de_resultados2022["isr"] + estado_de_resultados2022["ptu"],2)
estado_de_resultados2022["utilidad_del_ejercicio"] = round(estado_de_resultados2022["utilidad_antes_impuestos"] - \
                                                     estado_de_resultados2022["impuestos_por_pagar"],2)

balance_general2022 = {
    "activo_circulante": estado_financiero2022["cuentasxcobrar"] + estado_financiero2022["efectivo"] +
                         estado_financiero2022["inventarios"] + estado_financiero2022["inversiones"],
    "activo_no_circulante": estado_financiero2022["terrenoyedificios"] + estado_financiero2022["maquinariayequipo"] +
                            estado_financiero2022["equipodetransporte"] + estado_financiero2022["equipodecomputo"] +
                            estado_financiero2022["mobiliarioyaccesorios"] -
                            estado_financiero2022["depreciacionacumuladaactivosfijos"],
    "otros_activos": estado_financiero2022["gastospreoperativos"],
    "pasivo_corto_plazo": estado_financiero2022["acreedoresdiversos"] + estado_financiero2022["cuentasporpagar"] +
                          estado_financiero2022["documentosporpagar"] + estado_financiero2022["impuestos"] +
                          estado_de_resultados2022["impuestos_por_pagar"],
    "pasivo_largo_plazo": estado_financiero2022["hipotecasporpagarlargoplazo"],
    "capital_contribuido": estado_financiero2022["capitalsocial"] + estado_financiero2022["reservalegal"] +
                           estado_financiero2022["aportacionesparafuturosaumentosdecapital"],
    "capital_ganado": estado_financiero2022["utilidadesyejerciciosanteriores"] + estado_de_resultados2022[
        "utilidad_del_ejercicio"]
}

balance_general2022["total_activos"] = balance_general2022["activo_circulante"] + balance_general2022[
    "activo_no_circulante"] + balance_general2022["otros_activos"]
balance_general2022["total_pasivos"] = balance_general2022["pasivo_corto_plazo"] + balance_general2022[
    "pasivo_largo_plazo"]
balance_general2022["total_capital_contable"] = balance_general2022["capital_contribuido"] + balance_general2022[
    "capital_ganado"]

# print(tabulate(tabla_bg2021, headers="firstrow", tablefmt="fancy_grid"))
print(tabulate(tabla_er2021, headers="firstrow", tablefmt="fancy_grid"))

tabla_er2022 = [[" ESTADO DE RESULTADOS 2022 ","","","",""],
                ["","1","2","3","4"],
                ["Ventas","","","",f"${estado_financiero2022['ventas']}"],
                ["Costo de Ventas","","","",f"${estado_financiero2022['costodeventas']}"],
                ["","","","Utilidad Bruta",f"${estado_de_resultados2022['utilidad_bruta']}"],
                ["","","","",""],
                ["Gastos de venta","","",f"${estado_financiero2022['gastosdeventas']}",""],
                ["Gastos de Administracion","","",f"${estado_financiero2022['gastosdeadministracion']}",""],
                ["Gastos x Depreciación","","",f"${estado_financiero2022['gastospordepreciacion']}",""],
                ["Gastos Financieros","",f"${estado_financiero2022['gastosfinancieros']}","",""],
                ["Productos Financieros","",f"${estado_financiero2022['productosfinancieros']}","",""],
                ["Resul. Intgrl d Finan.","",f"${estado_de_resultados2022['resultado_integral_financiamento']}","",""],
                ["","","","Total de Gastos Operativos",f"${estado_de_resultados2022['total_gastos_operacion']}"],
                ["","","","Utilidad Operativa",f"${estado_de_resultados2022['utilidad_operativa']}"],
                ["","","","",""],
                ["Otros Gastos","","",f"${estado_financiero2022['otrosgastos']}",""],
                ["Otros Productos","","",f"${estado_financiero2022['otrosproductos']}",""],
                ["","","","Total de Otros Gastos y Productos",f"${estado_de_resultados2022['total_otros_gastos']}"],
                ["","","","Utilidad Antes de Impuestos",f"${estado_de_resultados2022['utilidad_antes_impuestos']}"],
                ["","","","",""],
                ["ISR","","30%",f"${estado_de_resultados2022['isr']}",""],
                ["PTU","","10%",f"${estado_de_resultados2022['ptu']}",""],
                ["","","","Total de Impuestos x Pagar",f"${estado_de_resultados2022['impuestos_por_pagar']}"],
                ["","","","Utilidad Neta del Ejercicio",f"${estado_de_resultados2022['utilidad_del_ejercicio']}"]
                ]

tabla_bg2022 = [["BALANCE GENERAL 2022", "", "", "", ""],
                ["Efectivo", "", f"${estado_financiero2022['efectivo']:,.2f}", "", ""],
                ["Cuentas por Cobrar", "", f"${estado_financiero2022['cuentasxcobrar']:,.2f}", "", ""],
                ["Inventarios", "", f"${estado_financiero2022['inventarios']:,.2f}", "", ""],
                ["Inversiones", "", f"${estado_financiero2022['inversiones']:,.2f}",
                 f"${balance_general2022['activo_circulante']:,.2f}", ""],
                ["", "", "", "", ""],
                ["Terrenos y Edificios", "", f"${estado_financiero2022['terrenoyedificios']:,.2f}", "", ""],
                ["Maq. y Equipo", "", f"${estado_financiero2022['maquinariayequipo']:,.2f}", "", ""],
                ["Mobiliario y Accesorios", "", f"${estado_financiero2022['mobiliarioyaccesorios']:,.2f}", "", ""],
                ["Eq. de Computo", "", f"${estado_financiero2022['equipodecomputo']:,.2f}", "", ""],
                ["Eq. de Transporte", "", f"${estado_financiero2022['equipodetransporte']:,.2f}", "", ""],
                ["Depr. Acumulada de Activos Fijos", "",
                 f"${estado_financiero2022['depreciacionacumuladaactivosfijos']:,.2f}",
                 f"${balance_general2022['activo_no_circulante']:,.2f}", ""],
                ["", "", "", "", ""],
                ["Gastos Preoperatorios", "", f"${estado_financiero2022['gastospreoperativos']:,.2f}",
                 f"${balance_general2022['otros_activos']:,.2f}", ""],
                ["", "", "", "Total Activos", f"${balance_general2022['total_activos']:,.2f}"],
                ["Acreedores Diversos", "", f"${estado_financiero2022['acreedoresdiversos']:,.2f}", "", ""],
                ["Cuentas por pagar", "", f"${estado_financiero2022['cuentasporpagar']:,.2f}", "", ""],
                ["Documentos por pagar", "", f"${estado_financiero2022['documentosporpagar']:,.2f}", "", ""],
                ["Impuestos", "", f"${estado_financiero2022['impuestos']:,.2f}",
                 f"${balance_general2022['pasivo_corto_plazo']:,.2f}", ""],
                ["", "", "", "", ""],
                ["Hipotecas por pagar a largo plazo", "",
                 f"${estado_financiero2022['hipotecasporpagarlargoplazo']:,.2f}",
                 f"${balance_general2022['pasivo_largo_plazo']:,.2f}", ""],
                ["", "", "", "Total Pasivos", f"${balance_general2022['total_pasivos']:,.2f}"],
                ["Capital Social", "", f"${estado_financiero2022['capitalsocial']:,.2f}", "", ""],
                ["Reserva Legal", "", f"${estado_financiero2022['reservalegal']:,.2f}", "", ""],
                ["Aportaciones para futuros aumentos de capital", "",
                 f"${estado_financiero2022['aportacionesparafuturosaumentosdecapital']:,.2f}",
                 f"${balance_general2022['capital_contribuido']:,.2f}", ""],
                ["", "", "", "", ""],
                ["Utilidades ejercicios anteriores", "",
                 f"${estado_financiero2022['utilidadesyejerciciosanteriores']:,.2f}", "", ""],
                ["Utilidad del ejercicio", "", f"${estado_de_resultados2022['utilidad_del_ejercicio']:,.2f}",
                 f"${balance_general2022['capital_ganado']:,.2f}", ""],
                ["", "", "", "Total Capital Contable", f"${balance_general2022['total_capital_contable']:,.2f}"]]

# print(tabulate(tabla_bg2022, headers="firstrow", tablefmt="fancy_grid"))
print(tabulate(tabla_er2022, headers="firstrow", tablefmt="fancy_grid"))

bg = [["LA COSTEÑITA.COM SA DE CV ", "", "", "", ""],
      ["Balance General", "", "", "", ""],
      ["Activo Circulante", "", "$200", "", ""],
      ["Efectivo", "", f"${estado_financiero2021['efectivo']:.2f}", "", ""]]

# print(tabulate(bg, headers="firstrow", tablefmt="fancy_grid"))

# Razones Financieras

# Actividad

rotacion_inv2021 = estado_financiero2021["costodeventas"] / estado_financiero2021["inventarios"]
rotacion_inv2022 = estado_financiero2022["costodeventas"] / estado_financiero2022["inventarios"]
rotacion_cxc2021 = estado_financiero2021["ventas"] / estado_financiero2021["cuentasxcobrar"]
rotacion_cxc2022 = estado_financiero2022["ventas"] / estado_financiero2022["cuentasxcobrar"]
rotacioncxp2021 = estado_financiero2021["costodeventas"] / estado_financiero2021["cuentasporpagar"]
rotacioncxp2022 = estado_financiero2022["costodeventas"] / estado_financiero2022["cuentasporpagar"]
rotacion_anc2021 = estado_financiero2021["ventas"] / balance_general2021["activo_no_circulante"]
rotacion_anc2022 = estado_financiero2022["ventas"] / balance_general2022["activo_no_circulante"]
rotacion_at2021 = estado_financiero2021["ventas"] / balance_general2021["total_activos"]
rotacion_at2022 = estado_financiero2022["ventas"] / balance_general2022["total_activos"]

# Liquidez

liquidez2021 = balance_general2021["activo_circulante"] / balance_general2021["pasivo_corto_plazo"]
liquidez2022 = balance_general2022["activo_circulante"] / balance_general2022["pasivo_corto_plazo"]
prueba_acida2021 = (balance_general2021["activo_circulante"] - estado_financiero2021["inventarios"]) / \
                   balance_general2021["pasivo_corto_plazo"]
prueba_acida2022 = (balance_general2022["activo_circulante"] - estado_financiero2022["inventarios"]) / \
                   balance_general2022["pasivo_corto_plazo"]
efectivo2021 = estado_financiero2021["efectivo"] / balance_general2021["pasivo_corto_plazo"]
efectivo2022 = estado_financiero2022["efectivo"] / balance_general2022["pasivo_corto_plazo"]

# Endeudamiento

razon_endeudamiento2021 = balance_general2021["total_pasivos"] / balance_general2021["total_activos"]
razon_endeudamiento2022 = balance_general2022["total_pasivos"] / balance_general2022["total_activos"]
razon_capital2021 = balance_general2021["total_capital_contable"] / balance_general2021["total_activos"]
razon_capital2022 = balance_general2022["total_capital_contable"] / balance_general2022["total_activos"]
razon_deuda_capital2021 = balance_general2021["pasivo_largo_plazo"] / balance_general2021["total_capital_contable"]
razon_deuda_capital2022 = balance_general2022["pasivo_largo_plazo"] / balance_general2022["total_capital_contable"]
razon_cargo_interes2021 = estado_de_resultados2021["utilidad_antes_impuestos"] / estado_de_resultados2021[
    "impuestos_por_pagar"]
razon_cargo_interes2022 = estado_de_resultados2022["utilidad_antes_impuestos"] / estado_de_resultados2022[
    "impuestos_por_pagar"]

# Rentabilidad

margen_utilidad2021 = estado_de_resultados2021["utilidad_del_ejercicio"] / estado_financiero2021["ventas"]
margen_utilidad2022 = estado_de_resultados2022["utilidad_del_ejercicio"] / estado_financiero2022["ventas"]
margen_bruto2021 = estado_de_resultados2021["utilidad_bruta"] / estado_financiero2021["ventas"]
margen_bruto2022 = estado_de_resultados2022["utilidad_bruta"] / estado_financiero2022["ventas"]
margen_operativo2021 = estado_de_resultados2021["utilidad_operativa"] / estado_financiero2021["ventas"]
margen_operativo2022 = estado_de_resultados2022["utilidad_operativa"] / estado_financiero2022["ventas"]
rendimiento_activos2021 = estado_de_resultados2021["utilidad_del_ejercicio"] / balance_general2021["total_activos"]
rendimiento_activos2022 = estado_de_resultados2022["utilidad_del_ejercicio"] / balance_general2022["total_activos"]
rendimiento_patrimonio2021 = estado_de_resultados2021["utilidad_del_ejercicio"] / balance_general2021[
    "total_capital_contable"]
rendimiento_patrimonio2022 = estado_de_resultados2022["utilidad_del_ejercicio"] / balance_general2022[
    "total_capital_contable"]
rendimiento_capital2021 = estado_de_resultados2021["utilidad_del_ejercicio"] / balance_general2021[
    "capital_contribuido"]
rendimiento_capital2022 = estado_de_resultados2022["utilidad_del_ejercicio"] / balance_general2022[
    "capital_contribuido"]

razones_financieras = [["Razones Financieras", "", "2021", "2022"],
                          ["Razones de Actividad", "", "", ""],
                            ["Rotacion de Inventario", "", f"{rotacion_inv2021:.2f}", f"{rotacion_inv2022:.2f}"],
                            ["Rotacion de Cuentas por Cobrar", "", f"{rotacion_cxc2021:.2f}",
                                f"{rotacion_cxc2022:.2f}"],
                            ["Rotacion de Cuentas por Pagar", "", f"{rotacioncxp2021:.2f}",
                                f"{rotacioncxp2022:.2f}"],
                            ["Rotacion de Activos No Circulante", "", f"{rotacion_anc2021:.2f}",
                                f"{rotacion_anc2022:.2f}"],
                            ["Rotacion de Activos Totales", "", f"{rotacion_at2021:.2f}",
                                f"{rotacion_at2022:.2f}"],
                       ["", "", "", ""],
                            ["Razones de Liquidez", "", "2021", "2022"],
                            ["Liquidez", "", f"{liquidez2021:.2f}", f"{liquidez2022:.2f}"],
                            ["Prueba Acida", "", f"{prueba_acida2021:.2f}", f"{prueba_acida2022:.2f}"],
                            ["Efectivo", "", f"{efectivo2021:.2f}", f"{efectivo2022:.2f}"],
                            ["", "", "", ""],
                            ["Razones de Endeudamiento", "", "2021", "2022"],
                            ["Razon de Endeudamiento", "", f"{razon_endeudamiento2021:.2f}",
                                f"{razon_endeudamiento2022:.2f}"],
                            ["Razon de Capital", "", f"{razon_capital2021:.2f}", f"{razon_capital2022:.2f}"],
                            ["Razón de Endeudamiento sobre Capital", "", f"{razon_deuda_capital2021:.2f}",
                                f"{razon_deuda_capital2022:.2f}"],
                            ["Razon de Cargos de Intereses Fijos", "", f"{razon_cargo_interes2021:.2f}",
                                f"{razon_cargo_interes2022:.2f}"],
                            ["", "", "", ""],
                            ["Razones de Rentabilidad", "", "2021", "2022"],
                            ["Margen de Utilidad", "", f"{margen_utilidad2021:.2f}", f"{margen_utilidad2022:.2f}"],
                            ["Margen Bruto", "", f"{margen_bruto2021:.2f}", f"{margen_bruto2022:.2f}"],
                            ["Margen Operativo", "", f"{margen_operativo2021:.2f}", f"{margen_operativo2022:.2f}"],
                            ["Rendimiento sobre Activos", "", f"{rendimiento_activos2021:.2f}",
                                f"{rendimiento_activos2022:.2f}"],
                            ["Rendimiento sobre Patrimonio", "", f"{rendimiento_patrimonio2021:.2f}",
                                f"{rendimiento_patrimonio2022:.2f}"],
                            ["Rendimiento sobre Capital", "", f"{rendimiento_capital2021:.2f}",
                                f"{rendimiento_capital2022:.2f}"]]

print(tabulate(razones_financieras, headers="firstrow", tablefmt="fancy_grid"))

# Analisis DuPont

ros2021 = estado_de_resultados2021["utilidad_del_ejercicio"] / estado_financiero2021["ventas"]
ros2022 = estado_de_resultados2022["utilidad_del_ejercicio"] / estado_financiero2022["ventas"]
rota2021 = estado_de_resultados2021["utilidad_del_ejercicio"] / balance_general2021["total_activos"]
rota2022 = estado_de_resultados2022["utilidad_del_ejercicio"] / balance_general2022["total_activos"]
maf2021 = balance_general2022["total_activos"] / balance_general2021["total_capital_contable"]
maf2022 = balance_general2022["total_activos"] / balance_general2022["total_capital_contable"]
roa2021 = ros2021 * rota2021
roa2022 = ros2022 * rota2022
roe = roa2021 * maf2021
roe2022 = roa2022 * maf2022

analisis_dupont = [["Analisis DuPont", "", "2021", "2022"],
                     ["Margen de Utilidad Neta", "", f"{ros2021:.2%}", f"{ros2022:.2%}"],
                        ["Rotacion de Activos", "", f"{rota2021:.2%}", f"{rota2022:.2%}"],
                        ["Multiplicador de Apalancamiento Financiero", "", f"{maf2021:.2%}", f"{maf2022:.2%}"],
                        ["Rendimiento sobre Activos", "", f"{roa2021:.2%}", f"{roa2022:.2%}"],
                        ["Rendimiento sobre Capital", "", f"{roe:.2%}", f"{roe2022:.2%}"]]
print(tabulate(analisis_dupont, headers="firstrow", tablefmt="fancy_grid"))
