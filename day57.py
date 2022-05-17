def hypertensive(patients):
    hypertension = 0
    
    for patient in patients:
        systolic = 0
        diastolic = 0
        sys_dias = False
        
        for measurements in patient:
            stats = measurements.split("/")
            
            if int(stats[0]) >= 180 and int(stats[1]) >= 110:
                hypertension += 1
                sys_dias = True
                break
            
            systolic += int(stats[0])
            diastolic += int(stats[1])
            
        avg_sys = systolic / len(patient)
        avg_dias = diastolic / len(patient)
        
        if sys_dias == True:
            pass
        else:
            if len(patient) >= 2:
                if avg_sys >= 140 or avg_dias >=90:
                    hypertension += 1
            
            
    return hypertension