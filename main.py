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


estado_financiero2021 = {
    "cuentasxcobrar": validacionInt("Ingrese el monto de la cuenta Cuentas por Cobrar del 2021: "),
    "efectivo": validacionInt("Ingrese el monto de la cuenta Efectivo del 2021: "),
    "inventarios": validacionInt("Ingrese el monto de la cuenta Inventarios del 2021: "),
    "inversiones": validacionInt("Ingrese el monto de la cuenta Inversiones del 2021: "),
    "depreciacionacumuladaactivosfijos": validacionInt(
        "Ingrese el monto de la cuenta Depreciación Acumulada de Activos Fijos del 2021: "),
    "equipodecomputo": validacionInt("Ingrese el monto de la cuenta Equipo de Computo del 2021: "),
    "equipodetransporte": validacionInt(
        "Ingrese el monto de la cuenta Equipo de Transporte del 2021: "),
    "maquinariayequipo": validacionInt(
        "Ingrese el monto de la cuenta Maquinaria y Equipo del 2021: "),
    "mobiliarioyaccesorios": validacionInt(
        "Ingrese el monto de la cuenta Mobiliario y Accesorios del 2021: "),
    "terrenoyedificios": validacionInt(
        "Ingrese el monto de la cuenta Terreno y Edificios del 2021: "),
    "aportacionesparafuturosaumentosdecapital": validacionInt(
        "Ingrese el monto de la cuenta Aportaciones para Futuros "
        "Aumentos de Capital del 2021: "),
    "capitalsocial": validacionInt("Ingrese el monto de la cuenta Capital Social del 2021: "),
    "reservalegal": validacionInt("Ingrese el monto de la cuenta Reserva Legal del 2021: "),
    "utilidadesyejerciciosanteriores": validacionInt(
        "Ingrese el monto de la cuenta Utilidades Ejercicios Anteriores del 2021: "),
    "costodeventas": validacionInt("Ingrese el monto de la cuenta Costo de Ventas del 2021: "),
    "gastosdeadministracion": validacionInt(
        "Ingrese el monto de la cuenta Gastos de Administración del 2021: "),
    "gastosdeventas": validacionInt("Ingrese el monto de la cuenta Gastos de Ventas del 2021: "),
    "gastosfinancieros": validacionInt(
        "Ingrese el monto de la cuenta Gastos Financieros del 2021: "),
    "gastospordepreciacion": validacionInt(
        "Ingrese el monto de la cuenta Gastos por Depreciación del 2021: "),
    "otrosgastos": validacionInt("Ingrese el monto de la cuenta Otros Gastos del 2021: "),
    "otrosproductos": validacionInt("Ingrese el monto de la cuenta Otros Productos del 2021: "),
    "productosfinancieros": validacionInt(
        "Ingrese el monto de la cuenta Productos Financieros del 2021: "),
    "ventas": validacionInt("Ingrese el monto de la cuenta Ventas del 2021: "),
    "gastospreoperativos": validacionInt(
        "Ingrese el monto de la cuenta Gastos Preoperativos del 2021: "),
    "acreedoresdiversos": validacionInt(
        "Ingrese el monto de la cuenta Acreedores Diversos del 2021: "),
    "cuentasporpagar": validacionInt("Ingrese el monto de la cuenta Cuentas por Pagar del 2021: "),
    "documentosporpagar": validacionInt(
        "Ingrese el monto de la cuenta Documentos por Pagar del 2021: "),
    "impuestos": validacionInt("Ingrese el monto de la cuenta Impuestos del 2021: "),
    "hipotecasporpagarlargoplazo": validacionInt(
        "Ingrese el monto de la cuenta Hipotecas por Pagar Largo Plazo del 2021: ")
}

estado_financiero2022 = {
    "cuentasxcobrar": validacionInt("Ingrese el monto de la cuenta Cuentas por Cobrar del 2022: "),
    "efectivo": validacionInt("Ingrese el monto de la cuenta Efectivo del 2022: "),
    "inventarios": validacionInt("Ingrese el monto de la cuenta Inventarios del 2022: "),
    "inversiones": validacionInt("Ingrese el monto de la cuenta Inversiones del 2022: "),
    "depreciacionacumuladaactivosfijos": validacionInt("Ingrese el monto de la cuenta "
                                                       "Depreciación Acumulada de Activos Fijos del 2022: "),
    "equipodecomputo": validacionInt("Ingrese el monto de la cuenta Equipo de Computo del 2022: "),
    "equipodetransporte": validacionInt("Ingrese el monto de la cuenta Equipo de Transporte del 2022: "),
    "maquinariayequipo": validacionInt("Ingrese el monto de la cuenta Maquinaria y Equipo del 2022: "),
    "mobiliarioyaccesorios": validacionInt("Ingrese el monto de la cuenta Mobiliario y Accesorios del 2022: "),
    "terrenoyedificios": validacionInt("Ingrese el monto de la cuenta Terreno y Edificios del 2022: "),
    "aportacionesparafuturosaumentosdecapital": validacionInt("Ingrese el monto de la cuenta Aportaciones para Futuros"
                                                              " Aumentos de Capital del 2022: "),
    "capitalsocial": validacionInt("Ingrese el monto de la cuenta Capital Social del 2022: "),
    "reservalegal": validacionInt("Ingrese el monto de la cuenta Reserva Legal del 2022: "),
    "utilidadesyejerciciosanteriores": validacionInt(
        "Ingrese el monto de la cuenta Utilidades Ejercicios Anteriores del 2022: "),
    "costodeventas": validacionInt("Ingrese el monto de la cuenta Costo de Ventas del 2022: "),
    "gastosdeadministracion": validacionInt(
        "Ingrese el monto de la cuenta Gastos de Administración del 2022: "),
    "gastosdeventas": validacionInt("Ingrese el monto de la cuenta Gastos de Ventas del 2022: "),
    "gastosfinancieros": validacionInt("Ingrese el monto de la cuenta Gastos Financieros del 2022: "),
    "gastospordepreciacion": validacionInt("Ingrese el monto de la cuenta Gastos por Depreciación del 2022: "),
    "otrosgastos": validacionInt("Ingrese el monto de la cuenta Otros Gastos del 2022: "),
    "otrosproductos": validacionInt("Ingrese el monto de la cuenta Otros Productos del 2022: "),
    "productosfinancieros": validacionInt("Ingrese el monto de la cuenta Productos Financieros del 2022: "),
    "ventas": validacionInt("Ingrese el monto de la cuenta Ventas del 2022: "),
    "gastospreoperativos": validacionInt(
        "Ingrese el monto de la cuenta Gastos Preoperativos del 2022: "),
    "acreedoresdiversos": validacionInt(
        "Ingrese el monto de la cuenta Acreedores Diversos del 2022: "),
    "cuentasporpagar": validacionInt("Ingrese el monto de la cuenta Cuentas por Pagar del 2022: "),
    "documentosporpagar": validacionInt(
        "Ingrese el monto de la cuenta Documentos por Pagar del 2022: "),
    "impuestos": validacionInt("Ingrese el monto de la cuenta Impuestos del 2022: "),
    "hipotecasporpagarlargoplazo": validacionInt(
        "Ingrese el monto de la cuenta Hipotecas por Pagar Largo Plazo del 2022: ")
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


print("""
╭─────────────────────────────╮
│  Estado de Resultados 2021  │
╰─────────────────────────────╯
""")

print(f'Utilidad Bruta: ${estado_de_resultados2021["utilidad_bruta"]:.2f}')
print(f'Total Gastos de Operacion: ${estado_de_resultados2021["total_gastos_operacion"]:.2f}\n')
print(f'Utilidad Operativa: ${estado_de_resultados2021["utilidad_operativa"]:.2f}')
print(f'Total Otros Gastos: ${estado_de_resultados2021["total_otros_gastos"]:.2f}\n')
print(f'Utilidad antes de Impuestos: ${estado_de_resultados2021["utilidad_antes_impuestos"]:.2f}')
print(f'Total Impuestos: ${estado_de_resultados2021["impuestos_por_pagar"]:.2f}\n')
print(f'Utilidad del Ejercicio: ${estado_de_resultados2021["utilidad_del_ejercicio"]:.2f}')

print("""
╭────────────────────────╮
│  Balance General 2021  │
╰────────────────────────╯
""")
#Mostrar Activos
print(f'Activo Circulante: ${balance_general2021["activo_circulante"]:.2f}')
print(f'Activo No circulante: ${balance_general2021["activo_no_circulante"]:.2f}')
print(f'Total de Activos: ${balance_general2021["total_activos"]:.2f}\n')

#Mostrar Pasivos
print(f'Pasivos a Corto plazo: ${balance_general2021["pasivo_corto_plazo"]:.2f}')
print(f'Pasivos a Largo plazo: ${balance_general2021["pasivo_largo_plazo"]:.2f}')
print(f'Total de Pasivos: ${balance_general2021["total_pasivos"]:.2f}\n')

#Mostrar Capital Contable
print(f'Capital Contribuido: ${balance_general2021["capital_contribuido"]:.2f}')
print(f'Capital Ganado: ${balance_general2021["capital_ganado"]:.2f}')
print(f'Total de Capital Contable: ${balance_general2021["total_capital_contable"]:.2f}\n')

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

print("""
───────────────────────────────────────────────────────────────────────────────────────────────

╭─────────────────────────────╮
│  Estado de Resultados 2022  │
╰─────────────────────────────╯
""")

print(f'Utilidad Bruta: ${estado_de_resultados2022["utilidad_bruta"]:.2f}')
print(f'Total Gastos de Operacion: ${estado_de_resultados2022["total_gastos_operacion"]:.2f}\n')
print(f'Utilidad Operativa: ${estado_de_resultados2022["utilidad_operativa"]:.2f}')
print(f'Total Otros Gastos: ${estado_de_resultados2022["total_otros_gastos"]:.2f}\n')
print(f'Utilidad antes de Impuestos: ${estado_de_resultados2022["utilidad_antes_impuestos"]:.2f}')
print(f'Total Impuestos: ${estado_de_resultados2022["impuestos_por_pagar"]:.2f}\n')
print(f'Utilidad del Ejercicio: ${estado_de_resultados2022["utilidad_del_ejercicio"]:.2f}')

print("""
╭────────────────────────╮
│  Balance General 2022  │
╰────────────────────────╯
""")
#Mostrar Activos
print(f'Activo Circulante: ${balance_general2022["activo_circulante"]:.2f}')
print(f'Activo No circulante: ${balance_general2022["activo_no_circulante"]:.2f}')
print(f'Total de Activos: ${balance_general2022["total_activos"]:.2f}\n')

#Mostrar Pasivos
print(f'Pasivos a Corto plazo: ${balance_general2022["pasivo_corto_plazo"]:.2f}')
print(f'Pasivos a Largo plazo: ${balance_general2022["pasivo_largo_plazo"]:.2f}')
print(f'Total de Pasivos: ${balance_general2022["total_pasivos"]:.2f}\n')

#Mostrar Capital Contable
print(f'Capital Contribuido: ${balance_general2022["capital_contribuido"]:.2f}')
print(f'Capital Ganado: ${balance_general2022["capital_ganado"]:.2f}')
print(f'Total de Capital Contable: ${balance_general2022["total_capital_contable"]:.2f}\n')
