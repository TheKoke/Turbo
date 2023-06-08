from matplotlib.axes import Axes
from matplotlib.figure import Figure


class Note:
    def __init__(self, path: str, quiz_frequency: float, file_frequency: float) -> None:
        self.path = path
        self.normal_ranges: dict[str, tuple[float, float]] = dict()

        self.line_counter = 0
        self.quiz_frequency = quiz_frequency
        self.new_file_frequency = file_frequency

    @property
    def main_file(self) -> str:
        if '.csv' in self.path:
            return ''

        return f'{self.path}\\out.csv'


class CSVParser:
    def __init__(self, note: Note) -> None:
        self.note = note

    def get_parameters(self) -> list[str]:
        first_file = self.get_files()[0]
        return open(f'{self.note.path}\\{first_file}').readline().split(';')

    def get_files(self) -> list[str]:
        main_file = open(f'{self.note.path}\\{self.note.main_file}.csv').readlines()
        return [main_file[i].split(';')[1] for i in range(len(main_file))]
    
    def take_last_note(self, parameter: str) -> float:
        return self.take_last_file(parameter)[-1]
    
    def take_last_file(self, parameter: str) -> list[float]:
        last = self.get_files()[-1]
        return self.get_parameter_values(parameter, last)

    def get_parameter_values(self, parameter: str, file_name: str) -> list[float]:
        self.everything_is_ok(file_name, parameter)

        params = self.get_parameters()
        index = params.index(parameter) if parameter in params else -1

        log = open(f'{self.note.path}\\{file_name}').readlines()[1:]
        return [float(log[i].split(';')[index]) for i in range(len(log))]
    
    def everything_is_ok(self, file_name: str, parameter: str) -> None:
        params = self.get_parameters()
        index = params.index(parameter) if parameter in params else -1

        if file_name not in self.get_files():
            raise RuntimeError(f"File {file_name}.csv doesn't exist.")
        
        if index == -1:
            raise RuntimeError(f"Pump doesn't have {parameter} parameter to output show.")


class Observer:
    def __init__(self, note: Note) -> None:
        self.note = note
        self.parser = CSVParser(note)

        self.parameters = self.parser.get_parameters()

    def set_norm_ranges(self, ranges: dict[str, tuple[float, float]]) -> None:
        for param in ranges:
            if param in self.note.normal_ranges:
                self.note.normal_ranges[param] = ranges[param]

    def check(self) -> bool:
        for param in self.parameters:
            if self.parser.take_last_note(param) <= self.note.normal_ranges[param][0] or \
                    self.parser.take_last_note(param) >= self.note.normal_ranges[param][1]:
                return False

        return True

    def error_message(self, parameter: str) -> str:
        if parameter not in self.parameters:
            return 'okay'

        return f'{parameter} is out of normal range'


class Painter:
    def __init__(self) -> None:
        pass


if __name__ == '__main__':
    pass
