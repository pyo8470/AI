## Non-deterministic Search
> ## EX) Grid World
> > # ![image](https://user-images.githubusercontent.com/84065357/192706376-37ef4529-e5a0-49b7-be9a-d0ffef2ba7a4.png)

## Markov Decision Processes(MDP)
> ### 구성요소
> > - Set of states $s$ in $S$
> > - Set of actions $a$ in $A$
> > - Transition function $T(s,a,s')$
> > > - $s$로부터 $a$를 선택해서 $s'$로 가는 확률 $P(s'| s,a)$
> > > - model이나 dynamics라고도 불림
> > - Reward Function $R(s,a,s')$
> > > - $R(s)$ 나 $R(s')$ 로도 표현됨(때때로)
> > - Start state
> > - terminal state
> ## Markov
> > - 주어진 현재 상태, 미래,현재는 독립적이다라는 뜻
> > # ![image](https://user-images.githubusercontent.com/84065357/192707732-0ba4486f-d29e-443a-8989-94c34f06933c.png)
> # ![image](https://user-images.githubusercontent.com/84065357/192707938-3b129fe3-43bb-4be9-ae0b-88f5f5ac71c7.png)
> - 현재 상황에서만 Optimal을 추구함.
> ## Utilities of Sequence
> > # ![image](https://user-images.githubusercontent.com/84065357/192709350-dad8cb91-be68-4116-ae4a-c6c787c3aaac.png)

## Discounting
> # ![image](https://user-images.githubusercontent.com/84065357/192709443-3e106334-487d-4117-ac53-4b5a5bf9afbc.png)
> > - reward의 가치가 시간이 지날수록 지수적으로 감소한다.
> # ![image](https://user-images.githubusercontent.com/84065357/192709779-c381a53e-986f-4960-bcb8-bcab44f978cd.png)

## Infinite Uitilites
> - 게임이 영원히 지속된다면 어찌할까
> ## Solution
> ### Finite Horizon(depth - limit 탐색과 유사함)
> > - 고정된 T Step후 강제 종료시킴
> > - 고정되지않은 policy 제공(파이는 남은 시간에 의존한다)
> ### Discounting
> > - 
> > # ![image](https://user-images.githubusercontent.com/84065357/192710379-6387a540-bc04-4b0e-91a1-efa26b6c9c90.png)
