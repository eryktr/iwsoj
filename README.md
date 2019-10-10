# iwsoj
Intelligent Web-Based Scalable Online Judge

# Workflow
1. **master** is a protected branch - pushing directly to it blocked.
2. In order to apply changes to master, you need to create a side-branch and then open a **pull request** against master.
3. You need to get at least one **approval** to be able to **merge** the pull request.
4. If there are **unresolved comments** about your pull request, do not merge it until all comments have been resolved.
5. For the ease of documentation generation, please use **docstrings** in the language of your choice.
6. If you know how to improve a certain area of a pull request, please, come up with a helpful **snippet**.
7. Code should be tested. **Unit tests**, maybe mocked, are enough to start with, but we will want to introduce integration testing later on.
