from llm_client import call_llm

class BaseAgent:
    def __init__(self, name: str, role_prompt: str):
        self.name = name
        self.role_prompt = role_prompt

    def act(self, task_input: str) -> str:
        return call_llm(self.role_prompt, task_input, agent_name=self.name)

# 具体 Agent 角色
class AnalystAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            "需求分析Agent",
            "你是一个资深需求分析师。请将用户需求拆解为明确的技术规格，输出 JSON 格式：{spec:..., signature:...}"
        )

class CoderAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            "编码Agent",
            "你是一个高级软件工程师。根据技术规格编写 Python 函数代码，只输出纯代码，不含解释。"
        )

class ReviewerAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            "审查Agent",
            "你是一个代码审查专家。检查代码的正确性、安全性和规范，发现问题时请明确指出。"
        )

class TesterAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            "测试Agent",
            "你是一个测试工程师。根据规格和代码，生成并模拟运行单元测试，报告成功或失败。"
        )
