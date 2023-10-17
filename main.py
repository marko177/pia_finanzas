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


estado_financiero2021 = {"cuentasxcobrar": validacionInt("Ingrese el monto de la cuenta Cuentas por Cobrar del 2021: "),
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
                             "Ingrese el monto de la cuenta Hipotecas por Pagar Largo Plazo del 2021: ")}

print(estado_financiero2021)

estado_financiero2022 = {"cuentasxcobrar": validacionInt("Ingrese el monto de la cuenta Cuentas por Cobrar del 2022: "),
                         "efectivo": validacionInt("Ingrese el monto de la cuenta Efectivo del 2022: "),
                         "inventarios": validacionInt("Ingrese el monto de la cuenta Inventarios del 2022: "),
                         "inversiones": validacionInt("Ingrese el monto de la cuenta Inversiones del 2022: "),
                         "depreciacionacumuladaactivosfijos": validacionInt("Ingrese el monto de la cuenta "
                                                                            "Depreciación Acumulada de Activos Fijos "
                                                                            "del 2022: "),
                         "equipodecomputo": validacionInt("Ingrese el monto de la cuenta Equipo de Computo del 2022: "),
                         "equipodetransporte": validacionInt("Ingrese el monto de la cuenta Equipo de Transporte del "
                                                             "2022: "),
                         "maquinariayequipo": validacionInt("Ingrese el monto de la cuenta Maquinaria y Equipo del "
                                                            "2022: "),
                         "mobiliarioyaccesorios": validacionInt("Ingrese el monto de la cuenta Mobiliario y Accesorios "
                                                                "del 2022: "),
                         "terrenoyedificios": validacionInt("Ingrese el monto de la cuenta Terreno y Edificios del "
                                                            "2022: "),
                         "aportacionesparafuturosaumentosdecapital": validacionInt("Ingrese el monto de la cuenta "
                                                                                   "Aportaciones para Futuros"
                                                                                   "Aumentos de Capital del 2022: "),
                         "capitalsocial": validacionInt("Ingrese el monto de la cuenta Capital Social del 2022: "),
                         "reservalegal": validacionInt("Ingrese el monto de la cuenta Reserva Legal del 2022: "),
                         "utilidadesyejerciciosanteriores": validacionInt(
                             "Ingrese el monto de la cuenta Utilidades Ejercicios Anteriores del 2022: "),
                         "costodeventas": validacionInt("Ingrese el monto de la cuenta Costo de Ventas del 2022: "),
                         "gastosdeadministracion": validacionInt(
                             "Ingrese el monto de la cuenta Gastos de Administración del 2022: "),
                         "gastosdeventas": validacionInt("Ingrese el monto de la cuenta Gastos de Ventas del 2022: "),
                         "gastosfinancieros": validacionInt(
                             "Ingrese el monto de la cuenta Gastos Financieros del 2022: "),
                         "gastospordepreciacion": validacionInt(
                             "Ingrese el monto de la cuenta Gastos por Depreciación del 2022: "),
                         "otrosgastos": validacionInt("Ingrese el monto de la cuenta Otros Gastos del 2022: "),
                         "otrosproductos": validacionInt("Ingrese el monto de la cuenta Otros Productos del 2022: "),
                         "productosfinancieros": validacionInt(
                             "Ingrese el monto de la cuenta Productos Financieros del 2022: "),
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
                             "Ingrese el monto de la cuenta Hipotecas por Pagar Largo Plazo del 2022: ")}

print(estado_financiero2022)

balance_general2021 = {
    "activo_circulante": estado_financiero2021["cuentasxcobrar"] + estado_financiero2021["efectivo"] +
                         estado_financiero2021["inventarios"] + estado_financiero2021["inversiones"],
    "activo_no_circulante": estado_financiero2021["depreciacionacumuladaactivosfijos"] +
                            estado_financiero2021["equipodecomputo"] + estado_financiero2021["equipodetransporte"] +
                            estado_financiero2021["maquinariayequipo"] + estado_financiero2021[
                                "mobiliarioyaccesorios"] + estado_financiero2021["terrenoyedificios"],
    "pasivo_corto_plazo": estado_financiero2021["aportacionesparafuturosaumentosdecapital"] +
                          estado_financiero2021["capitalsocial"] + estado_financiero2021["reservalegal"] +
                          estado_financiero2021["utilidadesyejerciciosanteriores"],
    "pasivo_largo_plazo": estado_financiero2021["hipotecasporpagarlargoplazo"],
    "capital_contribuido": estado_financiero2021["aportacionesparafuturosaumentosdecapital"] +
                           estado_financiero2021["capitalsocial"],
    "capital_ganado": estado_financiero2021["reservalegal"] + estado_financiero2021[
        "utilidadesyejerciciosanteriores"],
}
