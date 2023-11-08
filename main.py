from tabulate import tabulate


def validacionFloat(pregunta):
    while True:
        try:
            respuesta = float(input(pregunta))
            break
        except ValueError:
            print("Error, ingrese un valor numérico.")
    return respuesta


def validacionInt(pregunta):
    while True:
        try:
            respuesta = int(input(pregunta))
            break
        except ValueError:
            print("Error, ingrese un valor numérico sin decimales.")
    return respuesta


def validacionSN(pregunta):
    while True:
        respuesta = input(pregunta).upper()
        if respuesta == "S" or respuesta == "N":
            break
        else:
            print("Error, ingrese S o N.")
    return respuesta


starting_year = validacionInt("Ingrese el año de inicio del análisis: ")
ending_year = validacionInt("Ingrese el año de fin del análisis: ")
header = [[f"Analisis Financiero de la Empresa La Costeñita.com SA de CV {starting_year} - {ending_year}"]]
print(tabulate(header, tablefmt="fancy_grid"))

estado_financiero2021 = {
    "cuentasxcobrar": validacionInt(f"Ingrese el monto de la cuenta Cuentas por Cobrar del {starting_year}: "),
    "efectivo": validacionInt(f"Ingrese el monto de la cuenta Efectivo del {starting_year} "),
    "inventarios": validacionInt(f"Ingrese el monto de la cuenta Inventarios del {starting_year} "),
    "inversiones": validacionInt(f"Ingrese el monto de la cuenta Inversiones del {starting_year} "),
    "depreciacionacumuladaactivosfijos": validacionInt(
        f"Ingrese el monto de la cuenta Depreciación Acumulada de Activos Fijos del {starting_year} "),
    "equipodecomputo": validacionInt(f"Ingrese el monto de la cuenta Equipo de Computo del {starting_year} "),
    "equipodetransporte": validacionInt(
        f"Ingrese el monto de la cuenta Equipo de Transporte del {starting_year} "),
    "maquinariayequipo": validacionInt(
        f"Ingrese el monto de la cuenta Maquinaria y Equipo del {starting_year} "),
    "mobiliarioyaccesorios": validacionInt(
        f"Ingrese el monto de la cuenta Mobiliario y Accesorios del {starting_year} "),
    "terrenoyedificios": validacionInt(
        f"Ingrese el monto de la cuenta Terreno y Edificios del {starting_year} "),
    "aportacionesparafuturosaumentosdecapital": validacionInt(
        f"Ingrese el monto de la cuenta Aportaciones para Futuros "
        f"Aumentos de Capital del {starting_year} "),
    "capitalsocial": validacionInt(f"Ingrese el monto de la cuenta Capital Social del {starting_year} "),
    "reservalegal": validacionInt(f"Ingrese el monto de la cuenta Reserva Legal del {starting_year} "),
    "utilidadesyejerciciosanteriores": validacionInt(
        f"Ingrese el monto de la cuenta Utilidades Ejercicios Anteriores del {starting_year} "),
    "costodeventas": validacionInt(f"Ingrese el monto de la cuenta Costo de Ventas del {starting_year} "),
    "gastosdeadministracion": validacionInt(
        f"Ingrese el monto de la cuenta Gastos de Administración del {starting_year} "),
    "gastosdeventas": validacionInt(f"Ingrese el monto de la cuenta Gastos de Ventas del {starting_year} "),
    "gastosfinancieros": validacionInt(
        f"Ingrese el monto de la cuenta Gastos Financieros del {starting_year} "),
    "gastospordepreciacion": validacionInt(
        f"Ingrese el monto de la cuenta Gastos por Depreciación del {starting_year} "),
    "otrosgastos": validacionInt(f"Ingrese el monto de la cuenta Otros Gastos del {starting_year} "),
    "otrosproductos": validacionInt(f"Ingrese el monto de la cuenta Otros Productos del {starting_year} "),
    "productosfinancieros": validacionInt(
        "Ingrese el monto de la cuenta Productos Financieros del {starting_year} "),
    "ventas": validacionInt(f"Ingrese el monto de la cuenta Ventas del {starting_year} "),
    "gastospreoperativos": validacionInt(
        f"Ingrese el monto de la cuenta Gastos Preoperativos del {starting_year} "),
    "acreedoresdiversos": validacionInt(
        f"Ingrese el monto de la cuenta Acreedores Diversos del {starting_year} "),
    "cuentasporpagar": validacionInt(f"Ingrese el monto de la cuenta Cuentas por Pagar del {starting_year} "),
    "documentosporpagar": validacionInt(
        f"Ingrese el monto de la cuenta Documentos por Pagar del {starting_year} "),
    "impuestos": validacionInt(f"Ingrese el monto de la cuenta Impuestos del {starting_year} "),
    "hipotecasporpagarlargoplazo": validacionInt(
        f"Ingrese el monto de la cuenta Hipotecas por Pagar Largo Plazo del {starting_year} ")
}

estado_financiero2022 = {
    "cuentasxcobrar": validacionInt(f"Ingrese el monto de la cuenta Cuentas por Cobrar del {ending_year}: "),
    "efectivo": validacionInt(f"Ingrese el monto de la cuenta Efectivo del {ending_year}: "),
    "inventarios": validacionInt(f"Ingrese el monto de la cuenta Inventarios del {ending_year}: "),
    "inversiones": validacionInt(f"Ingrese el monto de la cuenta Inversiones del {ending_year}: "),
    "depreciacionacumuladaactivosfijos": validacionInt(f"Ingrese el monto de la cuenta "
                                                       "Depreciación Acumulada de Activos Fijos del {ending_year}: "),
    "equipodecomputo": validacionInt(f"Ingrese el monto de la cuenta Equipo de Computo del {ending_year}: "),
    "equipodetransporte": validacionInt(f"Ingrese el monto de la cuenta Equipo de Transporte del {ending_year}: "),
    "maquinariayequipo": validacionInt(f"Ingrese el monto de la cuenta Maquinaria y Equipo del {ending_year}: "),
    "mobiliarioyaccesorios": validacionInt(
        f"Ingrese el monto de la cuenta Mobiliario y Accesorios del {ending_year}: "),
    "terrenoyedificios": validacionInt(f"Ingrese el monto de la cuenta Terreno y Edificios del {ending_year}: "),
    "aportacionesparafuturosaumentosdecapital": validacionInt(f"Ingrese el monto de la cuenta Aportaciones para Futuros"
                                                              " Aumentos de Capital del {ending_year}: "),
    "capitalsocial": validacionInt(f"Ingrese el monto de la cuenta Capital Social del {ending_year}: "),
    "reservalegal": validacionInt(f"Ingrese el monto de la cuenta Reserva Legal del {ending_year}: "),
    "utilidadesyejerciciosanteriores": validacionInt(
        "Ingrese el monto de la cuenta Utilidades Ejercicios Anteriores del {ending_year}: "),
    "costodeventas": validacionInt(f"Ingrese el monto de la cuenta Costo de Ventas del {ending_year}: "),
    "gastosdeadministracion": validacionInt(
        "Ingrese el monto de la cuenta Gastos de Administración del {ending_year}: "),
    "gastosdeventas": validacionInt(f"Ingrese el monto de la cuenta Gastos de Ventas del {ending_year}: "),
    "gastosfinancieros": validacionInt(f"Ingrese el monto de la cuenta Gastos Financieros del {ending_year}: "),
    "gastospordepreciacion": validacionInt(
        f"Ingrese el monto de la cuenta Gastos por Depreciación del {ending_year}: "),
    "otrosgastos": validacionInt(f"Ingrese el monto de la cuenta Otros Gastos del {ending_year}: "),
    "otrosproductos": validacionInt(f"Ingrese el monto de la cuenta Otros Productos del {ending_year}: "),
    "productosfinancieros": validacionInt(f"Ingrese el monto de la cuenta Productos Financieros del {ending_year}: "),
    "ventas": validacionInt(f"Ingrese el monto de la cuenta Ventas del {ending_year}: "),
    "gastospreoperativos": validacionInt(
        "Ingrese el monto de la cuenta Gastos Preoperativos del {ending_year}: "),
    "acreedoresdiversos": validacionInt(
        "Ingrese el monto de la cuenta Acreedores Diversos del {ending_year}: "),
    "cuentasporpagar": validacionInt(f"Ingrese el monto de la cuenta Cuentas por Pagar del {ending_year}: "),
    "documentosporpagar": validacionInt(
        "Ingrese el monto de la cuenta Documentos por Pagar del {ending_year}: "),
    "impuestos": validacionInt(f"Ingrese el monto de la cuenta Impuestos del {ending_year}: "),
    "hipotecasporpagarlargoplazo": validacionInt(
        "Ingrese el monto de la cuenta Hipotecas por Pagar Largo Plazo del {ending_year}: ")
}

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

tabla_er2021 = [[" ESTADO DE RESULTADOS {starting_year ", "", "", "", ""],
                ["", "1", "2", "3", "4"],
                ["Ventas", "", "", "", f"${estado_financiero2021['ventas']}"],
                ["Costo de Ventas", "", "", "", f"${estado_financiero2021['costodeventas']}"],
                ["", "", "", "Utilidad Bruta", f"${estado_de_resultados2021['utilidad_bruta']}"],
                ["", "", "", "", ""],
                ["Gastos de venta", "", "", f"${estado_financiero2021['gastosdeventas']}", ""],
                ["Gastos de Administracion", "", "", f"${estado_financiero2021['gastosdeadministracion']}", ""],
                ["Gastos x Depreciación", "", "", f"${estado_financiero2021['gastospordepreciacion']}", ""],
                ["Gastos Financieros", "", f"${estado_financiero2021['gastosfinancieros']}", "", ""],
                ["Productos Financieros", "", f"${estado_financiero2021['productosfinancieros']}", "", ""],
                ["Resul. Intgrl d Finan.", "", f"${estado_de_resultados2021['resultado_integral_financiamento']}", "",
                 ""],
                ["", "", "", "Total de Gastos Operativos", f"${estado_de_resultados2021['total_gastos_operacion']}"],
                ["", "", "", "Utilidad Operativa", f"${estado_de_resultados2021['utilidad_operativa']}"],
                ["", "", "", "", ""],
                ["Otros Gastos", "", "", f"${estado_financiero2021['otrosgastos']}", ""],
                ["Otros Productos", "", "", f"${estado_financiero2021['otrosproductos']}", ""],
                ["", "", "", "Total de Otros Gastos y Productos", f"${estado_de_resultados2021['total_otros_gastos']}"],
                ["", "", "", "Utilidad Antes de Impuestos", f"${estado_de_resultados2021['utilidad_antes_impuestos']}"],
                ["", "", "", "", ""],
                ["ISR", "", "30%", f"${estado_de_resultados2021['isr']}", ""],
                ["PTU", "", "10%", f"${estado_de_resultados2021['ptu']}", ""],
                ["", "", "", "Total de Impuestos x Pagar", f"${estado_de_resultados2021['impuestos_por_pagar']}"],
                ["", "", "", "Utilidad Neta del Ejercicio", f"${estado_de_resultados2021['utilidad_del_ejercicio']}"]
                ]

tabla_bg2021 = [["BALANCE GENERAL {starting_year", "", "", "", ""],
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
estado_de_resultados2022["ptu"] = round(estado_de_resultados2022["utilidad_antes_impuestos"] * 0.10, 2)
estado_de_resultados2022["impuestos_por_pagar"] = round(
    estado_de_resultados2022["isr"] + estado_de_resultados2022["ptu"], 2)
estado_de_resultados2022["utilidad_del_ejercicio"] = round(estado_de_resultados2022["utilidad_antes_impuestos"] - \
                                                           estado_de_resultados2022["impuestos_por_pagar"], 2)

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

tabla_er2022 = [[" ESTADO DE RESULTADOS {ending_year} ", "", "", "", ""],
                ["", "1", "2", "3", "4"],
                ["Ventas", "", "", "", f"${estado_financiero2022['ventas']}"],
                ["Costo de Ventas", "", "", "", f"${estado_financiero2022['costodeventas']}"],
                ["", "", "", "Utilidad Bruta", f"${estado_de_resultados2022['utilidad_bruta']}"],
                ["", "", "", "", ""],
                ["Gastos de venta", "", "", f"${estado_financiero2022['gastosdeventas']}", ""],
                ["Gastos de Administracion", "", "", f"${estado_financiero2022['gastosdeadministracion']}", ""],
                ["Gastos x Depreciación", "", "", f"${estado_financiero2022['gastospordepreciacion']}", ""],
                ["Gastos Financieros", "", f"${estado_financiero2022['gastosfinancieros']}", "", ""],
                ["Productos Financieros", "", f"${estado_financiero2022['productosfinancieros']}", "", ""],
                ["Resul. Intgrl d Finan.", "", f"${estado_de_resultados2022['resultado_integral_financiamento']}", "",
                 ""],
                ["", "", "", "Total de Gastos Operativos", f"${estado_de_resultados2022['total_gastos_operacion']}"],
                ["", "", "", "Utilidad Operativa", f"${estado_de_resultados2022['utilidad_operativa']}"],
                ["", "", "", "", ""],
                ["Otros Gastos", "", "", f"${estado_financiero2022['otrosgastos']}", ""],
                ["Otros Productos", "", "", f"${estado_financiero2022['otrosproductos']}", ""],
                ["", "", "", "Total de Otros Gastos y Productos", f"${estado_de_resultados2022['total_otros_gastos']}"],
                ["", "", "", "Utilidad Antes de Impuestos", f"${estado_de_resultados2022['utilidad_antes_impuestos']}"],
                ["", "", "", "", ""],
                ["ISR", "", "30%", f"${estado_de_resultados2022['isr']}", ""],
                ["PTU", "", "10%", f"${estado_de_resultados2022['ptu']}", ""],
                ["", "", "", "Total de Impuestos x Pagar", f"${estado_de_resultados2022['impuestos_por_pagar']}"],
                ["", "", "", "Utilidad Neta del Ejercicio", f"${estado_de_resultados2022['utilidad_del_ejercicio']}"]
                ]

tabla_bg2022 = [["BALANCE GENERAL {ending_year}", "", "", "", ""],
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

bg = [["LA COSTEÑITA.COM SA DE CV ", "", "", "", ""],
      ["Balance General", "", "", "", ""],
      ["Activo Circulante", "", "$200", "", ""],
      ["Efectivo", "", f"${estado_financiero2021['efectivo']:.2f}", "", ""]]

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

# Ciclo de Conversion de Efectivo

capital_de_trabajo2021 = balance_general2021["activo_circulante"] - balance_general2021["pasivo_corto_plazo"]
capital_de_trabajo2022 = balance_general2022["activo_circulante"] - balance_general2022["pasivo_corto_plazo"]
epi_2021 = 360 / rotacion_inv2021
epi_2022 = 360 / rotacion_inv2022
ppc_2021 = 360 / rotacion_cxc2021
ppc_2022 = 360 / rotacion_cxc2022
ppp_2021 = 360 / rotacioncxp2021
ppp_2022 = 360 / rotacioncxp2022
ciclo_operativo2021 = epi_2021 + ppc_2021
ciclo_operativo2022 = epi_2022 + ppc_2022
ciclo_conversion_efectivo2021 = ciclo_operativo2021 - ppp_2021
ciclo_conversion_efectivo2022 = ciclo_operativo2022 - ppp_2022

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

razones_financieras = [["Razones Financieras", "", "", "", ""],
                       ["Razones de Liquidez", "", "{starting_year", "{ending_year}", "Interpretación"],
                       ["Liquidez", "", f"{liquidez2021:.2f}", f"{liquidez2022:.2f}",
                        f"La empresa tiene una razón circulante {'dentro del' if 1 <= liquidez2021 <= 2 else 'fuera del'} rango aceptable y"
                        f"\n del ejercicio del {starting_year} al {ending_year} {'mejoro' if liquidez2022 > liquidez2021 else 'empeoro'} su razón circulante en "
                        f"{abs(liquidez2022 - liquidez2021):.2f}."],
                       ["Prueba Acida", "", f"{prueba_acida2021:.2f}", f"{prueba_acida2022:.2f}",
                        f"La empresa tiene una prueba acida {'dentro del' if 1 <= prueba_acida2021 <= 1.5 else 'fuera del'} rango aceptable"
                        f"\ny del ejercicio del {starting_year} al {ending_year} {'mejoro' if prueba_acida2022 > prueba_acida2021 else 'empeoro'} su prueba "
                        f"acida en {abs(prueba_acida2022 - prueba_acida2021):.2f}."],
                       ["Efectivo", "", f"{efectivo2021:.2f}", f"{efectivo2022:.2f}",
                        f"La empresa por cada peso que debe en el banco tiene ${efectivo2021:.2f} centavos"
                        f"\n{'incrementando un' if efectivo2022 > efectivo2021 else 'disminuyendo un'} "
                        f"{abs(efectivo2022 - efectivo2021):.2f} centavos del ejercicio del {starting_year} al {ending_year}."],
                       ["", "", "", ""],
                       ["Razones de Actividad", "", "{starting_year", "{ending_year}", "Interpretación"],
                       ["Rotacion de Inventario", "", f"{rotacion_inv2021:.2f}", f"{rotacion_inv2022:.2f}",
                        f"La empresa {'aumentó' if rotacion_inv2021 < rotacion_inv2022 else 'disminuyó'} su Rotación de Inventario del "
                        f"{starting_year} al {ending_year}."],
                       ["Rotacion de Cuentas por Cobrar", "", f"{rotacion_cxc2021:.2f}",
                        f"{rotacion_cxc2022:.2f}",
                        f"La empresa {'aumentó' if rotacion_cxc2021 < rotacion_cxc2022 else 'disminuyó'} su Rotación de Cuentas por Cobrar "
                        f"del {starting_year} al {ending_year}."],
                       ["Rotacion de Cuentas por Pagar", "", f"{rotacioncxp2021:.2f}",
                        f"{rotacioncxp2022:.2f}",
                        f"La empresa {'aumentó' if rotacioncxp2021 < rotacioncxp2022 else 'disminuyó'} su Rotación de Cuentas por Pagar "
                        f"del {starting_year} al {ending_year}."],
                       ["Rotacion de Activos No Circulantes", "", f"{rotacion_anc2021:.2f}",
                        f"{rotacion_anc2022:.2f}",
                        f"La empresa {'aumentó' if rotacion_anc2021 < rotacion_anc2022 else 'disminuyó'} su Rotación de No Circulantes del "
                        f"{starting_year} al {ending_year}."],
                       ["Rotacion de Activos Totales", "", f"{rotacion_at2021:.2f}",
                        f"{rotacion_at2022:.2f}",
                        f"La empresa {'aumentó' if rotacion_at2021 < rotacion_at2022 else 'disminuyó'} su Rotación de Activos Totales del "
                        f"{starting_year} al {ending_year}."],
                       ["", "", "", ""],
                       ["Ciclo de Conversión de Efectivo", "", "{starting_year", "{ending_year}", "Interpretación"],
                       ["Capital de Trabajo", "", f"${capital_de_trabajo2021:.2f}", f"${capital_de_trabajo2022:.2f}",
                        f"La empresa {'incrementó' if capital_de_trabajo2021 < capital_de_trabajo2022 else 'disminuyó'} su Capital de "
                        f"Trabajo del {starting_year} al {ending_year}."],
                       ["Edad Promedio de Inventarios", "", f"{epi_2021:.2f}", f"{epi_2022:.2f}",
                        f"La empresa {'incrementó' if epi_2021 < epi_2022 else 'disminuyó'} su Edad Promedio de Inventarios del {starting_year} al "
                        f"{ending_year}."],
                       ["Periodo Promedio de Cobro", "", f"{ppc_2021:.2f}", f"{ppc_2022:.2f}",
                        f"La empresa {'incrementó' if ppc_2021 < ppc_2022 else 'disminuyó'} su Periodo Promedio de Cobro del {starting_year} al "
                        f"{ending_year}."],
                       ["Periodo Promedio de Pago", "", f"{ppp_2021:.2f}", f"{ppp_2022:.2f}",
                        f"La empresa {'incrementó' if ppp_2021 < ppp_2022 else 'disminuyó'} su Periodo Promedio de Pago del {starting_year} al "
                        f"{ending_year}."],
                       ["Ciclo Operativo", "", f"{ciclo_operativo2021:.2f}", f"{ciclo_operativo2022:.2f}",
                        f"La empresa {'incrementó' if ciclo_operativo2021 < ciclo_operativo2022 else 'disminuyó'} su Ciclo Operativo "
                        f"del {starting_year} al {ending_year}."],
                       ["Ciclo de Conversión de Efectivo", "", f"{ciclo_conversion_efectivo2021:.2f}",
                        f"{ciclo_conversion_efectivo2022:.2f}",
                        f"La empresa {'incrementó' if ciclo_conversion_efectivo2021 < ciclo_conversion_efectivo2022 else 'disminuyó'}"
                        f"su Ciclo de Conversión de Efectivo del {starting_year} al {ending_year}."],
                       ["", "", "", ""],
                       ["Razones de Endeudamiento", "", "{starting_year", "{ending_year}", "Interpretación"],
                       ["Razon de Endeudamiento", "", f"{razon_endeudamiento2021:.2f}",
                        f"{razon_endeudamiento2022:.2f}",
                        f"La empresa esta financiada en un {razon_endeudamiento2022 * 100:.2f}%"
                        f"de deuda externa."],
                       ["Razon de Capital", "", f"{razon_capital2021:.2f}", f"{razon_capital2022:.2f}",
                        f"La empresa esta financiada en un {razon_capital2022 * 100:.2f}% de capital propio."],
                       ["Razón de Endeudamiento sobre Capital", "", f"{razon_deuda_capital2021:.2f}",
                        f"{razon_deuda_capital2022:.2f}"],
                       ["Razon de Cargos de Intereses Fijos", "", f"{razon_cargo_interes2021:.2f}",
                        f"{razon_cargo_interes2022:.2f}"],
                       ["", "", "", ""],
                       ["Razones de Rentabilidad", "", "{starting_year", "{ending_year}", "Interpretación"],
                       ["Margen de Utilidad", "", f"{margen_utilidad2021:.2f}", f"{margen_utilidad2022:.2f}"],
                       ["Margen Bruto", "", f"{margen_bruto2021:.2f}", f"{margen_bruto2022:.2f}"],
                       ["Margen Operativo", "", f"{margen_operativo2021:.2f}", f"{margen_operativo2022:.2f}"],
                       ["Rendimiento sobre Activos", "", f"{rendimiento_activos2021:.2f}",
                        f"{rendimiento_activos2022:.2f}",
                        f"La empresa {'incrementó' if rendimiento_activos2021 < rendimiento_activos2022 else 'disminuyó'} su Rendimiento sobre Activos del {starting_year} al {ending_year}."],
                       ["Rendimiento sobre Patrimonio", "", f"{rendimiento_patrimonio2021:.2f}",
                        f"{rendimiento_patrimonio2022:.2f}",
                        f"La empresa {'incrementó' if rendimiento_patrimonio2021 < rendimiento_patrimonio2022 else 'disminuyó'} su Rendimiento sobre Patrimonio del {starting_year} al {ending_year}."],
                       ["Rendimiento sobre Capital", "", f"{rendimiento_capital2021:.2f}",
                        f"{rendimiento_capital2022:.2f}",
                        f"La empresa {'incrementó' if rendimiento_capital2021 < rendimiento_capital2022 else 'disminuyó'} su Rendimiento sobre Capital del {starting_year} al {ending_year}."]]

# print(tabulate(tabla_bg2021, headers="firstrow", tablefmt="fancy_grid"))
# print(tabulate(tabla_er2021, headers="firstrow", tablefmt="fancy_grid"))
# print(tabulate(tabla_bg2022, headers="firstrow", tablefmt="fancy_grid"))
# print(tabulate(tabla_er2022, headers="firstrow", tablefmt="fancy_grid"))
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

analisis_dupont = [["Analisis DuPont", "", "{starting_year", "{ending_year}", "Interpretación"],
                   ["Margen de Utilidad Neta", "", f"{ros2021:.2%}", f"{ros2022:.2%}",
                    f"La empresa {'incrementó' if ros2021 < ros2022 else 'disminuyó'} su Margen de Utilidad Neta del {starting_year} al {ending_year}."],
                   ["Rotacion de Activos", "", f"{rota2021:.2%}", f"{rota2022:.2%}",
                    f"La empresa {'incrementó' if rota2021 < rota2022 else 'disminuyó'} su Rotación de Activos del {starting_year} al {ending_year}."],
                   ["Multiplicador de Apalancamiento Financiero", "", f"{maf2021:.2%}", f"{maf2022:.2%}",
                    f"La empresa {'incrementó' if maf2021 < maf2022 else 'disminuyó'} su Multiplicador de Apalancamiento Financiero del {starting_year} al {ending_year}."],
                   ["Rendimiento sobre Activos", "", f"{roa2021:.2%}", f"{roa2022:.2%}",
                    f"La empresa {'incrementó' if roa2021 < roa2022 else 'disminuyó'} su Rendimiento sobre Activos del {starting_year} al {ending_year}."],
                   ["Rendimiento sobre Capital", "", f"{roe:.2%}", f"{roe2022:.2%}",
                    f"La empresa {'incrementó' if roe < roe2022 else 'disminuyó'} su Rendimiento sobre Capital del {starting_year} al {ending_year}."]]
print(tabulate(analisis_dupont, headers="firstrow", tablefmt="fancy_grid"))
