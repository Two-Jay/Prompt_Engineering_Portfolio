<!-- 이 프롬프트는 PAL 전략을 응용했습니다.  -->
<!-- 프롬프트의 일부에 대해 매개변수화를 시도했습니다. -->
<!-- Ref : https://arxiv.org/abs/2211.10435 -->

caller = OpenAI()

요렇게 했을 때, 유저 1,2,3 세명이 있고, 같은 caller를 쓴다면 서로 다른 gpt 스레드에서 이야기하는 것처럼 complation의 메모리를 분리시키고 싶어.

reply to me by {target_language}
target_language=English