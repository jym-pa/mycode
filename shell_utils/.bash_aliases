function python_chmod_and_execute() {
	chmod u+x "$1" && "$1"
}
alias pyrun='python_chmod_and_execute'

