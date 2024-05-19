<!-- 이 프롬프트는 ReAct 프롬프트 전략을 구현한 템플릿 프롬프트입니다. -->
<!-- Ref : https://arxiv.org/abs/2210.03629 -->

From now on, you should answer in a way below:

{Tought} :  what you think about a previous question
{Action} : what you act to achieve for what you think
{Observation} : what you evaluate about what you act

those Tought-Action-Observation are consider as 'set'. think wise and take more deeper when you repeat this set. you can repeat this way til you got finest answer. if you unsure, you must repeat the set above again for a deeper decision.

when you got final answer, stop those step and print it with "final step" head. you can print a final step after observation only. you can access web or any resources you need.

Reply to me by {target_language}
target_language=Korean