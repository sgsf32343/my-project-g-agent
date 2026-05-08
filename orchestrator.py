from agents import AnalystAgent, CoderAgent, ReviewerAgent, TesterAgent

class CodeOrchestrator:
    def __init__(self):
        self.analyst = AnalystAgent()
        self.coder = CoderAgent()
        self.reviewer = ReviewerAgent()
        self.tester = TesterAgent()
        self.max_rounds = 3  # 最多修复轮次

    def run(self, requirement: str) -> dict:
        print(f"\n📋 需求: {requirement}")
        # 1. 需求分析
        spec = self.analyst.act(requirement)
        print(f"🔍 分析结果: {spec}")

        # 2. 编码
        code = self.coder.act(spec)
        print(f"💻 初始代码:\n{code}")

        # 3. 审查与测试循环（长链推理）
        for round_num in range(1, self.max_rounds + 1):
            print(f"\n--- 第 {round_num} 轮审查测试 ---")
            review = self.reviewer.act(code)
            print(f"👀 审查: {review}")
            test = self.tester.act(code)
            print(f"🧪 测试: {test}")

            if "通过" in review and "通过" in test:
                print("✅ 审查和测试均通过，交付！")
                return {"status": "success", "code": code}
            else:
                if round_num < self.max_rounds:
                    print("🔄 启动修复闭环...")
                    # 将审查和测试反馈作为修复输入
                    fix_prompt = f"原始需求:{requirement}\n当前代码:\n{code}\n审查意见:{review}\n测试结果:{test}\n请修复代码。"
                    code = self.coder.act(fix_prompt)
                    print(f"🔧 修复后代码:\n{code}")
                else:
                    print("❌ 达到最大修复轮次，需人工介入。")
        return {"status": "failed", "code": code}
