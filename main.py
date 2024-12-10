import engine_module
import display_module
import fileIO_module

WORD_FILE = "word_list_ranked.txt"
PERFORMANCE_FILE = "performance_data.txt"

def main():
    # Load initial data
    engine_module.load_words(WORD_FILE)
    engine_module.update_performance_data(PERFORMANCE_FILE)
    fileIO_module.load_performance(PERFORMANCE_FILE)
    display_module.init_instruction_screen()
main()
