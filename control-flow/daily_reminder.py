#todo list
task = input('Enter your task: ')
priority = input('Priority (high/medium/low): ')
time_bound = input('Is it time-bound? (yes/no): ')

match priority:
    case 'high':
        if time_bound == 'yes':
            print('Reminder: ' +task + ' is important and urgent, complete it now.')
        else:
            print('Reminder: '+task +' require immediate attention today.')
    case 'medium':
        if time_bound == 'yes':
            print('Alert:'+task + ' is important complete within 24 hours.')
        else:
            print('Check '+ task+ ' need to be complete within 48 hours.')
    case 'low':
        if time_bound =='yes':
            print('Note:'+task +'  not urgent do it before weekend.')
        else:
            print('Note: '+task+' can be completed on weekend.')
    case _:
        print('No such task.')

    