import csv


def open_csv(file_path : str):
    with open(file_path, 'r', encoding='utf-8-sig') as file:
        data = file.readlines()
    return data

def check_node(node_struct : str):
    node = ["",""]
    match node_struct:
        case "Узел 1":
            node = ["node1","Node1"]
        case "Узел 2":
            node = ["node2","Node2"]
        case "Узел 3":
            node = ["node3","Node3"]
        case "Узел 4":
            node = ["node4","Node4"]
        case "Узел 5":
            node = ["node5","Node5"]
        case "Узел 6":
            node = ["node6","Node6"]
        case "Узел 7":
            node = ["node7","Node7"]
        case "Узел 8":
            node = ["node8","Node8"]
        case "Узел 9":
            node = ["node9","Node9"]
        case "Узел 10":
            node = ["node10","Node10"]
    return node

def binding_mechanism(data : list):
    modified_data = []
    first_line = data[0].strip()
    for line in data:
        line = line.strip()
        if not line:
            continue
        
        columns = line.split(";")
        if len(columns) > 5:
            node = ""
            try:
                device = columns[2].split(".")[4]
            except:
                continue
            try:
                node_struct = columns[2].split(".")[2]
            except:
                continue

            node = check_node(node_struct)

            """
            Подвязка задвижек
            """
            if "Gate" in device:
                match columns[1]:
                    case "Слово состояния":
                        columns[4] = f"Система.АРМ 1.Протоколы.OPC UA.IEC_DATA.Application.STATES.{node[0]}.{device}.Background.Вход"
                    case "Слово положения":
                        columns[4] = f"Система.АРМ 1.Протоколы.OPC UA.IEC_DATA.Application.STATES.{node[0]}.{device}.Center.Вход"
                    case "Текущий режим":
                        columns[4] = f"Система.АРМ 1.Протоколы.OPC UA.IEC_DATA.Application.STATES.{node[0]}.{device}.AlarmCode.Вход"
                    case "В процессе открывания":
                        columns[4] = f"Система.АРМ 1.Протоколы.OPC UA.IEC_DATA.Application.STATES.{node[0]}.{device}.OriginalState.InProcessOpen.Вход"
                    case "В процессе закрывания":
                        columns[4] = f"Система.АРМ 1.Протоколы.OPC UA.IEC_DATA.Application.STATES.{node[0]}.{device}.OriginalState.InProcessClose.Вход"
                    case "Статус режим":
                        columns[4] = f"Система.АРМ 1.Протоколы.OPC UA.IEC_DATA.Application.STATES.{node[0]}.{device}.OriginalState.Auto"
                    case "Ключ управления":
                        columns[4] = f"Система.АРМ 1.Протоколы.OPC UA.IEC_DATA.Application.STATES.{node[0]}.{device}.key"
                    case "Текущее положение":
                        columns[4] = f""
                    case "Готовность":
                        columns[4] = f""
                    case "Уставка":
                        columns[4] = f""
                    case "Автоматический режим":
                        columns[5] = f"Система.АРМ 1.Протоколы.OPC UA.IEC_DATA.Application.CTRL.scadaControl.{node[1]}.{device}.SetAuto"
                    case "Ручной режим":
                        columns[5] = f"Система.АРМ 1.Протоколы.OPC UA.IEC_DATA.Application.CTRL.scadaControl.{node[1]}.{device}.SetManual"
                    case "Сброс":
                        columns[5] = f"Система.АРМ 1.Протоколы.OPC UA.IEC_DATA.Application.CTRL.scadaControl.{node[1]}.{device}.ResetErrors"
                    case "Открыть":
                        columns[5] = f"Система.АРМ 1.Протоколы.OPC UA.IEC_DATA.Application.CTRL.scadaControl.{node[1]}.{device}.OpenManual"
                    case "Закрыть":
                        columns[5] = f"Система.АРМ 1.Протоколы.OPC UA.IEC_DATA.Application.CTRL.scadaControl.{node[1]}.{device}.CloseManual"

            """
            Подвязка миксеров
            """
            if "Mixer" in device:
                match columns[1]:
                    case "Слово состояния":
                        columns[4] = f"Система.АРМ 1.Протоколы.OPC UA.IEC_DATA.Application.STATES.{node[0]}.{device}.Background"
                    case "Слово положения":
                        columns[4] = f"Система.АРМ 1.Протоколы.OPC UA.IEC_DATA.Application.STATES.{node[0]}.{device}.Center"
                    case "Запускается":
                        columns[4] = f"Система.АРМ 1.Протоколы.OPC UA.IEC_DATA.Application.STATES.{node[0]}.{device}.OriginalState.InProcessStart"
                    case "Останавливается":
                        columns[4] = f"Система.АРМ 1.Протоколы.OPC UA.IEC_DATA.Application.STATES.{node[0]}.{device}.OriginalState.InProcessStop"
                    case "Текстовый статус":
                        columns[4] = f"Система.АРМ 1.Протоколы.OPC UA.IEC_DATA.Application.STATES.{node[0]}.{device}.AlarmCode"
                    case "Ключ управления":
                        columns[4] = f"Система.АРМ 1.Протоколы.OPC UA.IEC_DATA.Application.STATES.{node[0]}.{device}.key"
                    case "Режим":
                        columns[4] = f"Система.АРМ 1.Протоколы.OPC UA.IEC_DATA.Application.STATES.{node[0]}.{device}.OriginalState.Auto"
                    case "ПУСК":
                        columns[5] = f"Система.АРМ 1.Протоколы.OPC UA.IEC_DATA.Application.CTRL.scadaControl.{node[1]}.{device}.StartManual"
                    case "СТОП":
                        columns[5] = f"Система.АРМ 1.Протоколы.OPC UA.IEC_DATA.Application.CTRL.scadaControl.{node[1]}.{device}.StopManual"
                    case "СБРОС":
                        columns[5] = f"Система.АРМ 1.Протоколы.OPC UA.IEC_DATA.Application.CTRL.scadaControl.{node[1]}.{device}.ResetEngineFailure"
                    case "Автоматический режим":
                        columns[5] = f"Система.АРМ 1.Протоколы.OPC UA.IEC_DATA.Application.CTRL.scadaControl.{node[1]}.{device}.SetAuto"
                    case "Ручной режим":
                        columns[5] = f"Система.АРМ 1.Протоколы.OPC UA.IEC_DATA.Application.CTRL.scadaControl.{node[1]}.{device}.SetManual"

                        
        modified_line = ";".join(columns)
        modified_data.append(modified_line)
    modified_data.insert(0, first_line)
    return modified_data

def binding_ai(data : list):
    """
    Подвязка любого AI сигнала, пока что без AO (возможно будет сепарация)
    """
    modified_data = []
    first_line = data[0].strip()
    for line in data:
        line = line.strip()
        if not line:
            continue
        
        columns = line.split(";")
        if len(columns) > 5:
            try:
                ai_signal = columns[2].split(".")[1]
            except:
                continue
            in_or_out = 0
            try:
                in_or_out = 1 if columns[2].split(".")[6] == "Вход" else 2
            except:
                in_or_out = 0

            target = columns[2].split(".")[4]
            if "Сигналы и экземпляры" in ai_signal:
                match columns[2].split(".")[5]:
                    case "value":
                        columns[4] = f"Система.АРМ 1.Протоколы.OPC UA.IEC_DATA.Application.SIGNALS.{target}.Processed.Value.Вход"
                    case "Ток на канале":
                        columns[4] = f"Система.АРМ 1.Протоколы.OPC UA.IEC_DATA.Application.SIGNALS.{target}.source_value.Вход"

                    case "Контроль HH":
                        if in_or_out == 1:
                            columns[4] = f"Система.АРМ 1.Протоколы.OPC UA.IEC_DATA.Application.SIGNALS.{target}.Processed.State.Enable_HH.Вход"
                        elif in_or_out == 2:
                            columns[5] = f"Система.АРМ 1.Протоколы.OPC UA.IEC_DATA.Application.CFG.scadaConf.signals.{target}.Enable_HH.Выход"
                    case "Контроль H":
                        if in_or_out == 1:
                            columns[4] = f"Система.АРМ 1.Протоколы.OPC UA.IEC_DATA.Application.SIGNALS.{target}.Processed.State.Enable_H.Вход"
                        elif in_or_out == 2:
                            columns[5] = f"Система.АРМ 1.Протоколы.OPC UA.IEC_DATA.Application.CFG.scadaConf.signals.{target}.Enable_H.Выход"
                    case "Контроль L":
                        if in_or_out == 1:
                            columns[4] = f"Система.АРМ 1.Протоколы.OPC UA.IEC_DATA.Application.SIGNALS.{target}.Processed.State.Enable_L.Вход"
                        elif in_or_out == 2:
                            columns[5] = f"Система.АРМ 1.Протоколы.OPC UA.IEC_DATA.Application.CFG.scadaConf.signals.{target}.Enable_L.Выход"
                    case "Контроль LL":
                        if in_or_out == 1:
                            columns[4] = f"Система.АРМ 1.Протоколы.OPC UA.IEC_DATA.Application.SIGNALS.{target}.Processed.State.Enable_LL.Вход"
                        elif in_or_out == 2:
                            columns[5] = f"Система.АРМ 1.Протоколы.OPC UA.IEC_DATA.Application.CFG.scadaConf.signals.{target}.Enable_LL.Выход"

                    case "Нижнее инженерное значение":
                        if in_or_out == 1:
                            columns[4] = f"Система.АРМ 1.Протоколы.OPC UA.IEC_DATA.Application.CFG.scadaConf.signals.{target}.ValueMin.Вход"
                        elif in_or_out == 2:
                            columns[5] = f"Система.АРМ 1.Протоколы.OPC UA.IEC_DATA.Application.CFG.scadaConf.signals.{target}.ValueMin.Выход"
                    case "Верхнее инженерное значение":
                        if in_or_out == 1:
                            columns[4] = f"Система.АРМ 1.Протоколы.OPC UA.IEC_DATA.Application.CFG.scadaConf.signals.{target}.ValueMax.Вход"
                        elif in_or_out == 2:
                            columns[5] = f"Система.АРМ 1.Протоколы.OPC UA.IEC_DATA.Application.CFG.scadaConf.signals.{target}.ValueMin.Выход"

                    case "Верхнее аварийное значение":
                        if in_or_out == 1:
                            columns[4] = f"Система.АРМ 1.Протоколы.OPC UA.IEC_DATA.Application.CFG.scadaConf.signals.{target}.AlarmValueHH.Вход"
                        elif in_or_out == 2:
                            columns[5] = f"Система.АРМ 1.Протоколы.OPC UA.IEC_DATA.Application.CFG.scadaConf.signals.{target}.AlarmValueHH.Выход"
                    case "Верхнее предупредительное значение":
                        if in_or_out == 1:
                            columns[4] = f"Система.АРМ 1.Протоколы.OPC UA.IEC_DATA.Application.CFG.scadaConf.signals.{target}.AlarmValueH.Вход"
                        elif in_or_out == 2:
                            columns[5] = f"Система.АРМ 1.Протоколы.OPC UA.IEC_DATA.Application.CFG.scadaConf.signals.{target}.AlarmValueH.Выход"
                    case "Нижнее предупредительное значение":
                        if in_or_out == 1:
                            columns[4] = f"Система.АРМ 1.Протоколы.OPC UA.IEC_DATA.Application.CFG.scadaConf.signals.{target}.AlarmValueL.Вход"
                        elif in_or_out == 2:
                            columns[5] = f"Система.АРМ 1.Протоколы.OPC UA.IEC_DATA.Application.CFG.scadaConf.signals.{target}.AlarmValueL.Выход"
                    case "Нижнее аварийное значение":
                        if in_or_out == 1:
                            columns[4] = f"Система.АРМ 1.Протоколы.OPC UA.IEC_DATA.Application.CFG.scadaConf.signals.{target}.AlarmValueLL.Вход"
                        elif in_or_out == 2:
                            columns[5] = f"Система.АРМ 1.Протоколы.OPC UA.IEC_DATA.Application.CFG.scadaConf.signals.{target}.AlarmValueLL.Выход"

                    case "Имитация":
                        if in_or_out == 1:
                            columns[4] = f"Система.АРМ 1.Протоколы.OPC UA.IEC_DATA.Application.SIGNALS.{target}.Processed.State.Imitation.Вход"
                        elif in_or_out == 2:
                            columns[5] = f"Система.АРМ 1.Протоколы.OPC UA.IEC_DATA.Application.CFG.scadaConf.signals.{target}.Imitation.Выход"
                    case "Имитация значение":
                        if in_or_out == 1:
                            columns[4] = f"Система.АРМ 1.Протоколы.OPC UA.IEC_DATA.Application.CFG.scadaConf.signals.{target}.ImitValue.Вход"
                        elif in_or_out == 2:
                            columns[5] = f"Система.АРМ 1.Протоколы.OPC UA.IEC_DATA.Application.CFG.scadaConf.signals.{target}.ImitValue.Выход"

                    case "Выход сигнала за верхнюю аварийную границу":
                        columns[4] = f"Система.АРМ 1.Протоколы.OPC UA.IEC_DATA.Application.SIGNALS.{target}.Processed.State.Alarm_HH.Вход"
                    case "Выход сигнала за верхнюю предупредительную границу":
                        columns[4] = f"Система.АРМ 1.Протоколы.OPC UA.IEC_DATA.Application.SIGNALS.{target}.Processed.State.Alarm_H.Вход"
                    case "Выход сигнала за нижнюю предупредительную границу":
                        columns[4] = f"Система.АРМ 1.Протоколы.OPC UA.IEC_DATA.Application.SIGNALS.{target}.Processed.State.Alarm_L.Вход"
                    case "Выход сигнала за нижнюю аварийную границу":
                        columns[4] = f"Система.АРМ 1.Протоколы.OPC UA.IEC_DATA.Application.SIGNALS.{target}.Processed.State.Alarm_LL.Вход"

                    case "Неисправность канала":
                        columns[4] = f""
                    case "Бракование канала":
                        columns[4] = f""
        
        modified_line = ";".join(columns)
        modified_data.append(modified_line)
    modified_data.insert(0, first_line)
    return modified_data


# modified_data = binding_mechanism(open_csv('podvyaz_in.csv'))
modified_data = binding_ai(open_csv('ai_podvyaz.csv'))
with open('priem_peredacha_out.csv', 'w', encoding='utf-8-sig', newline='') as file:
    file.write("\n".join(modified_data))
    print("Файл 'priem_peredacha_out.csv' создан")