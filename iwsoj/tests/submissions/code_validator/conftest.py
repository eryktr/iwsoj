import pytest

@pytest.fixture()
def valid_cpp_code():
    return """
        #include <iostream>
        
        int main(void) {
            int n;
            std::cin >> n;
            std::cout << 2 * n << " output" << std::endl;
        }
    """


@pytest.fixture()
def wrong_cpp_code():
    return """
        #include <iostream>

        int main(void) {
            int n;
            std::cin >> n;
            std::cout << 3 * n << " output" << std::endl;
        }
    """


@pytest.fixture()
def not_compiling_cpp_code():
    return """
        #include __FILE__
        
        Some_huge_compile_error;
    """