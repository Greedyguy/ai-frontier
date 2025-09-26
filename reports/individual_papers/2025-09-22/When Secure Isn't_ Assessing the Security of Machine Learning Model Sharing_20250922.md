---
keywords:
  - Machine Learning
  - Model Sharing
  - Security Risks
  - Zero-Day Vulnerabilities
category: cs.LG
publish_date: 2025-09-22
arxiv_id: 2509.06703
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T11:23:12.794522",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Machine Learning",
    "Model Sharing",
    "Security Risks",
    "Zero-Day Vulnerabilities"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Machine Learning": 0.85,
    "Model Sharing": 0.88,
    "Security Risks": 0.82,
    "Zero-Day Vulnerabilities": 0.9
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Machine Learning",
        "canonical": "Machine Learning",
        "aliases": [],
        "category": "broad_technical",
        "rationale": "A foundational concept that connects to various technical discussions in the paper.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.5,
        "link_intent_score": 0.85
      },
      {
        "surface": "model sharing",
        "canonical": "Model Sharing",
        "aliases": [
          "model exchange",
          "model distribution"
        ],
        "category": "unique_technical",
        "rationale": "Central to the paper's discussion on security risks and practices.",
        "novelty_score": 0.75,
        "connectivity_score": 0.7,
        "specificity_score": 0.8,
        "link_intent_score": 0.88
      },
      {
        "surface": "security risks",
        "canonical": "Security Risks",
        "aliases": [
          "security threats",
          "vulnerabilities"
        ],
        "category": "specific_connectable",
        "rationale": "Key to understanding the challenges in model sharing frameworks.",
        "novelty_score": 0.55,
        "connectivity_score": 0.78,
        "specificity_score": 0.72,
        "link_intent_score": 0.82
      },
      {
        "surface": "0-day vulnerabilities",
        "canonical": "Zero-Day Vulnerabilities",
        "aliases": [
          "0-day exploits",
          "zero-day threats"
        ],
        "category": "unique_technical",
        "rationale": "Highlights specific security issues uncovered in the study.",
        "novelty_score": 0.8,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.9
      }
    ],
    "ban_list_suggestions": [
      "frameworks",
      "hubs",
      "file format"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Machine Learning",
      "resolved_canonical": "Machine Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.9,
        "specificity": 0.5,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "model sharing",
      "resolved_canonical": "Model Sharing",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.7,
        "specificity": 0.8,
        "link_intent": 0.88
      }
    },
    {
      "candidate_surface": "security risks",
      "resolved_canonical": "Security Risks",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.78,
        "specificity": 0.72,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "0-day vulnerabilities",
      "resolved_canonical": "Zero-Day Vulnerabilities",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.9
      }
    }
  ]
}
-->

# When Secure Isn't: Assessing the Security of Machine Learning Model Sharing

**Korean Title:** 보안이 보장되지 않을 때: 머신러닝 모델 공유의 보안성 평가

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.06703.pdf)
**Category**: cs.LG
**Published**: 2025-09-22
**ArXiv ID**: [2509.06703](https://arxiv.org/abs/2509.06703)

## 🔗 유사한 논문
- [[2025-09-22/PickleBall_ Secure Deserialization of Pickle-based Machine Learning Models (Extended Report)_20250922|PickleBall: Secure Deserialization of Pickle-based Machine Learning Models (Extended Report)]] (82.7% similar)
- [[2025-09-19/The Sum Leaks More Than Its Parts_ Compositional Privacy Risks and Mitigations in Multi-Agent Collaboration_20250919|The Sum Leaks More Than Its Parts: Compositional Privacy Risks and Mitigations in Multi-Agent Collaboration]] (81.7% similar)
- [[2025-09-19/Enterprise AI Must Enforce Participant-Aware Access Control_20250919|Enterprise AI Must Enforce Participant-Aware Access Control]] (80.8% similar)
- [[2025-09-18/Is GPT-4o mini Blinded by its Own Safety Filters? Exposing the Multimodal-to-Unimodal Bottleneck in Hate Speech Detection_20250918|Is GPT-4o mini Blinded by its Own Safety Filters? Exposing the Multimodal-to-Unimodal Bottleneck in Hate Speech Detection]] (80.6% similar)
- [[2025-09-18/The Cybersecurity of a Humanoid Robot_20250918|The Cybersecurity of a Humanoid Robot]] (80.5% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Machine Learning|Machine Learning]]
**🔗 Specific Connectable**: [[keywords/Security Risks|Security Risks]]
**⚡ Unique Technical**: [[keywords/Model Sharing|Model Sharing]], [[keywords/Zero-Day Vulnerabilities|Zero-Day Vulnerabilities]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.06703v2 Announce Type: replace-cross 
Abstract: The rise of model-sharing through frameworks and dedicated hubs makes Machine Learning significantly more accessible. Despite their benefits, these tools expose users to underexplored security risks, while security awareness remains limited among both practitioners and developers. To enable a more security-conscious culture in Machine Learning model sharing, in this paper we evaluate the security posture of frameworks and hubs, assess whether security-oriented mechanisms offer real protection, and survey how users perceive the security narratives surrounding model sharing. Our evaluation shows that most frameworks and hubs address security risks partially at best, often by shifting responsibility to the user. More concerningly, our analysis of frameworks advertising security-oriented settings and complete model sharing uncovered six 0-day vulnerabilities enabling arbitrary code execution. Through this analysis, we debunk the misconceptions that the model-sharing problem is largely solved and that its security can be guaranteed by the file format used for sharing. As expected, our survey shows that the surrounding security narrative leads users to consider security-oriented settings as trustworthy, despite the weaknesses shown in this work. From this, we derive takeaways and suggestions to strengthen the security of model-sharing ecosystems.

## 🔍 Abstract (한글 번역)

arXiv:2509.06703v2 발표 유형: 교체-크로스  
초록: 프레임워크와 전용 허브를 통한 모델 공유의 증가는 기계 학습을 상당히 더 접근 가능하게 만듭니다. 이러한 도구들은 이점이 있지만, 사용자들에게 충분히 탐구되지 않은 보안 위험을 노출시키며, 실무자와 개발자 모두의 보안 인식은 제한적입니다. 기계 학습 모델 공유에서 보다 보안 의식이 높은 문화를 조성하기 위해, 본 논문에서는 프레임워크와 허브의 보안 태세를 평가하고, 보안 지향 메커니즘이 실제로 보호 기능을 제공하는지 평가하며, 모델 공유를 둘러싼 보안 서사를 사용자가 어떻게 인식하는지 조사합니다. 우리의 평가는 대부분의 프레임워크와 허브가 보안 위험을 최대한 부분적으로만 해결하며, 종종 책임을 사용자에게 전가한다는 것을 보여줍니다. 더 우려되는 점은, 보안 지향 설정과 완전한 모델 공유를 광고하는 프레임워크의 분석에서 임의 코드 실행을 가능하게 하는 6개의 제로데이 취약점을 발견했다는 것입니다. 이 분석을 통해, 모델 공유 문제가 대부분 해결되었고, 공유에 사용되는 파일 형식으로 보안이 보장될 수 있다는 오해를 불식시킵니다. 예상대로, 우리의 설문조사는 주변의 보안 서사가 사용자로 하여금 보안 지향 설정을 신뢰할 수 있는 것으로 간주하게 만든다는 것을 보여줍니다, 이 연구에서 드러난 약점에도 불구하고. 이를 바탕으로, 우리는 모델 공유 생태계의 보안을 강화하기 위한 교훈과 제안을 도출합니다.

## 📝 요약

이 논문은 머신러닝 모델 공유의 보안 문제를 평가하고, 보안 인식 제고를 위한 방안을 제시합니다. 연구 결과, 대부분의 프레임워크와 허브는 보안 위험을 부분적으로만 다루며, 사용자에게 책임을 전가하는 경향이 있습니다. 특히, 보안을 강조하는 설정에서도 임의 코드 실행을 가능하게 하는 6개의 제로데이 취약점이 발견되었습니다. 이러한 분석을 통해 모델 공유의 보안 문제가 해결되지 않았음을 밝히고, 파일 형식만으로 보안을 보장할 수 없다는 오해를 바로잡습니다. 설문조사 결과, 사용자들은 보안 설정을 신뢰하지만, 실제로는 취약점이 존재함을 보여줍니다. 이를 바탕으로 모델 공유 생태계의 보안을 강화하기 위한 제언을 제공합니다.

## 🎯 주요 포인트

- 1. 모델 공유를 통해 머신러닝 접근성이 크게 향상되었지만, 보안 위험에 대한 인식은 여전히 부족하다.
- 2. 대부분의 프레임워크와 허브는 보안 위험을 부분적으로만 해결하며, 종종 사용자에게 책임을 전가한다.
- 3. 보안 지향 설정을 광고하는 프레임워크 분석에서 임의 코드 실행을 가능하게 하는 6개의 제로데이 취약점이 발견되었다.
- 4. 모델 공유 문제는 아직 해결되지 않았으며, 파일 형식만으로 보안을 보장할 수 없다는 오해를 불식시켰다.
- 5. 사용자들은 보안 지향 설정을 신뢰할 수 있다고 여기지만, 실제로는 취약점이 존재한다는 점이 드러났다.


---

*Generated on 2025-09-23 11:23:12*