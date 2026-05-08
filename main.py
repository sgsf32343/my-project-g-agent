import argparse
from orchestrator import CodeOrchestrator
from config import DEMO_MODE

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--demo", action="store_true", help="使用模拟 Agent 运行演示")
    args = parser.parse_args()

    if args.demo:
        import config
        config.DEMO_MODE = True
        print("🎭 运行演示模式（无 API 消耗）")

    orchestrator = CodeOrchestrator()
    result = orchestrator.run("写一个函数，计算两个整数的和")
    print("\n📦 最终结果:")
    print(result)

if __name__ == "__main__":
    main()
