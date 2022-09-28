import calc
import ui
import logger

def button_menu(command, x, y):

        if command == "1": 
            logger.write_log(ui.view_result(str(f'{x} + {y} = {calc.sum(x, y)}')))
        elif command == "2": 
            logger.write_log(ui.view_result(str(f'{x} - {y} = {calc.sub(x, y)}')))
        elif command == "3": 
            logger.write_log(ui.view_result(str(f'{x} * {y} = {calc.mult(x, y)}')))
        elif command == "4": 
            logger.write_log(ui.view_result(str(f'{x} / {y} = {calc.div(x, y)}')))