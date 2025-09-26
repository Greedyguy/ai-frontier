import React, { useState, useEffect } from 'react';

const NotificationSettings = () => {
  const [emailSubscribers, setEmailSubscribers] = useState({
    daily: [],
    weekly: []
  });
  const [keywordSubscribers, setKeywordSubscribers] = useState([]);
  const [newEmail, setNewEmail] = useState('');
  const [newKeywords, setNewKeywords] = useState('');
  const [digestType, setDigestType] = useState('daily');
  const [notificationStatus, setNotificationStatus] = useState(null);
  const [loading, setLoading] = useState(false);
  const [message, setMessage] = useState('');
  const [showKeywordForm, setShowKeywordForm] = useState(false);
  const [editingSubscription, setEditingSubscription] = useState(null);

  useEffect(() => {
    fetchEmailSubscribers();
    fetchKeywordSubscribers();
    fetchNotificationStatus();
  }, []);

  const fetchEmailSubscribers = async () => {
    try {
      // 일반 이메일 구독자 가져오기
      const response = await fetch('/api/notifications/email/subscribers');
      if (response.ok) {
        const data = await response.json();

        // 키워드 구독자도 함께 가져와서 통합
        const keywordResponse = await fetch('/api/notifications/keywords/subscribers');
        if (keywordResponse.ok) {
          const keywordData = await keywordResponse.json();
          const keywordSubscriptions = keywordData.subscriptions || [];

          // 일간/주간별로 키워드 구독자 분류
          const dailyKeywordEmails = keywordSubscriptions
            .filter(sub => sub.digest_type === 'daily' && sub.active)
            .map(sub => sub.email);
          const weeklyKeywordEmails = keywordSubscriptions
            .filter(sub => sub.digest_type === 'weekly' && sub.active)
            .map(sub => sub.email);

          setEmailSubscribers({
            daily: [...new Set([...(data.daily_subscribers || []), ...dailyKeywordEmails])],
            weekly: [...new Set([...(data.weekly_subscribers || []), ...weeklyKeywordEmails])]
          });
        } else {
          setEmailSubscribers({
            daily: data.daily_subscribers || [],
            weekly: data.weekly_subscribers || []
          });
        }
      }
    } catch (error) {
      console.error('Error fetching email subscribers:', error);
    }
  };

  const fetchKeywordSubscribers = async () => {
    try {
      const response = await fetch('/api/notifications/keywords/subscribers');
      if (response.ok) {
        const data = await response.json();
        setKeywordSubscribers(data.subscriptions || []);
      }
    } catch (error) {
      console.error('Error fetching keyword subscribers:', error);
    }
  };

  const fetchNotificationStatus = async () => {
    try {
      const response = await fetch('/api/notifications/status');
      if (response.ok) {
        const data = await response.json();
        setNotificationStatus(data);
      }
    } catch (error) {
      console.error('Error fetching notification status:', error);
    }
  };

  const handleSubscribeEmail = async (e) => {
    e.preventDefault();
    if (!newEmail) return;

    setLoading(true);
    try {
      if (digestType === 'both') {
        // 일간과 주간 모두 구독
        const dailyResponse = await fetch('/api/notifications/email/subscribe', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({
            email: newEmail,
            digest_type: 'daily'
          }),
        });

        const weeklyResponse = await fetch('/api/notifications/email/subscribe', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({
            email: newEmail,
            digest_type: 'weekly'
          }),
        });

        const dailyData = await dailyResponse.json();
        const weeklyData = await weeklyResponse.json();

        if (dailyData.success && weeklyData.success) {
          setMessage(`✅ ${newEmail}을 일간 + 주간 구독 목록에 추가했습니다.`);
        } else {
          setMessage(`⚠️ 일부 구독에 실패했습니다. 일간: ${dailyData.success ? '성공' : '실패'}, 주간: ${weeklyData.success ? '성공' : '실패'}`);
        }
      } else {
        // 기존 방식
        const response = await fetch('/api/notifications/email/subscribe', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({
            email: newEmail,
            digest_type: digestType
          }),
        });

        const data = await response.json();
        if (data.success) {
          setMessage(`✅ ${newEmail}을 ${digestType === 'daily' ? '일간' : '주간'} 구독 목록에 추가했습니다.`);
        } else {
          setMessage(`⚠️ ${data.message}`);
        }
      }

      setNewEmail('');
      fetchEmailSubscribers();
    } catch (error) {
      setMessage(`❌ 구독 추가 중 오류가 발생했습니다: ${error.message}`);
    }
    setLoading(false);
  };

  const handleSubscribeKeywords = async (e) => {
    e.preventDefault();
    if (!newEmail || !newKeywords.trim()) return;

    setLoading(true);
    try {
      const keywords = newKeywords.split(',').map(k => k.trim()).filter(k => k.length > 0);

      if (digestType === 'both') {
        // 일간과 주간 모두 구독
        const dailyResponse = await fetch('/api/notifications/keywords/subscribe', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({
            email: newEmail,
            keywords: keywords,
            digest_type: 'daily'
          }),
        });

        const weeklyResponse = await fetch('/api/notifications/keywords/subscribe', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({
            email: newEmail,
            keywords: keywords,
            digest_type: 'weekly'
          }),
        });

        const dailyData = await dailyResponse.json();
        const weeklyData = await weeklyResponse.json();

        if (dailyData.success && weeklyData.success) {
          setMessage(`✅ ${newEmail}을 키워드 기반 일간 + 주간 구독 목록에 추가했습니다.\n키워드: ${keywords.join(', ')}`);
        } else {
          setMessage(`⚠️ 구독 중 일부 오류가 발생했습니다.\n일간: ${dailyData.message || '성공'}\n주간: ${weeklyData.message || '성공'}`);
        }
      } else {
        // 단일 구독 (daily 또는 weekly)
        const response = await fetch('/api/notifications/keywords/subscribe', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({
            email: newEmail,
            keywords: keywords,
            digest_type: digestType
          }),
        });

        const data = await response.json();
        if (data.success) {
          setMessage(`✅ ${newEmail}을 키워드 기반 ${digestType === 'daily' ? '일간' : '주간'} 구독 목록에 추가했습니다.\n키워드: ${keywords.join(', ')}`);
        } else {
          setMessage(`⚠️ ${data.message}`);
        }
      }

      setNewEmail('');
      setNewKeywords('');
      setShowKeywordForm(false);
      fetchKeywordSubscribers();
      fetchEmailSubscribers(); // 통합 목록 새로고침
    } catch (error) {
      setMessage(`❌ 키워드 구독 추가 중 오류가 발생했습니다: ${error.message}`);
    }
    setLoading(false);
  };

  const handleUnsubscribeEmail = async (email, type) => {
    if (!confirm(`${email}을 ${type} 구독 목록에서 제거하시겠습니까?`)) {
      return;
    }

    try {
      const response = await fetch('/api/notifications/email/unsubscribe', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          email: email,
          digest_type: type
        }),
      });

      const data = await response.json();
      if (data.success) {
        setMessage(`✅ ${email}을 ${type} 구독 목록에서 제거했습니다.`);
        fetchEmailSubscribers();
      } else {
        setMessage(`⚠️ ${data.message}`);
      }
    } catch (error) {
      setMessage(`❌ 구독 해제 중 오류가 발생했습니다: ${error.message}`);
    }
  };

  const handleUnsubscribeKeywords = async (email) => {
    if (!confirm(`${email}을 키워드 기반 구독 목록에서 제거하시겠습니까?`)) {
      return;
    }

    try {
      const response = await fetch(`/api/notifications/keywords/unsubscribe?email=${encodeURIComponent(email)}`, {
        method: 'DELETE',
        headers: {
          'Content-Type': 'application/json',
        },
      });

      const data = await response.json();
      if (data.success) {
        setMessage(`✅ ${email}을 키워드 기반 구독 목록에서 제거했습니다.`);
        fetchKeywordSubscribers();
        fetchEmailSubscribers(); // 통합 목록 새로고침
      } else {
        setMessage(`⚠️ ${data.message}`);
      }
    } catch (error) {
      setMessage(`❌ 키워드 구독 해제 중 오류가 발생했습니다: ${error.message}`);
    }
  };

  const handleEditSubscription = (subscriber) => {
    setEditingSubscription(subscriber);
    setNewEmail(subscriber.email);
    setNewKeywords(subscriber.keywords.join(', '));
    setDigestType(subscriber.digest_type);
    setShowKeywordForm(true);
  };

  const handleUpdateSubscription = async (e) => {
    e.preventDefault();
    if (!newEmail || !newKeywords.trim() || !editingSubscription) return;

    setLoading(true);
    try {
      const keywords = newKeywords.split(',').map(k => k.trim()).filter(k => k.length > 0);

      if (digestType === 'both') {
        // 일간과 주간 모두 구독
        const dailyResponse = await fetch('/api/notifications/keywords/subscribe', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({
            email: newEmail,
            keywords: keywords,
            digest_type: 'daily'
          }),
        });

        const weeklyResponse = await fetch('/api/notifications/keywords/subscribe', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({
            email: newEmail,
            keywords: keywords,
            digest_type: 'weekly'
          }),
        });

        const dailyData = await dailyResponse.json();
        const weeklyData = await weeklyResponse.json();

        if (dailyData.success && weeklyData.success) {
          setMessage(`✅ ${newEmail}의 키워드 구독이 일간 + 주간으로 업데이트되었습니다.\n키워드: ${keywords.join(', ')}`);
        } else {
          setMessage(`⚠️ 구독 업데이트 중 일부 오류가 발생했습니다.\n일간: ${dailyData.message || '성공'}\n주간: ${weeklyData.message || '성공'}`);
        }
      } else {
        // 단일 구독 (daily 또는 weekly)
        const response = await fetch('/api/notifications/keywords/subscribe', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({
            email: newEmail,
            keywords: keywords,
            digest_type: digestType
          }),
        });

        const data = await response.json();
        if (data.success) {
          setMessage(`✅ ${newEmail}의 키워드 구독이 ${digestType === 'daily' ? '일간' : '주간'}으로 업데이트되었습니다.\n키워드: ${keywords.join(', ')}`);
        } else {
          setMessage(`⚠️ ${data.message}`);
        }
      }

      setNewEmail('');
      setNewKeywords('');
      setShowKeywordForm(false);
      setEditingSubscription(null);
      fetchKeywordSubscribers();
      fetchEmailSubscribers(); // 통합 목록 새로고침
    } catch (error) {
      setMessage(`❌ 키워드 구독 업데이트 중 오류가 발생했습니다: ${error.message}`);
    }
    setLoading(false);
  };

  const handleTestNotifications = async () => {
    setLoading(true);
    try {
      const response = await fetch('/api/notifications/test', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          test_email: true,
          test_slack: true,
          test_webhooks: true
        }),
      });

      const data = await response.json();
      if (data.success) {
        const results = data.results;
        let testMessage = '🧪 연결 테스트 결과:\\n';
        testMessage += `📧 이메일: ${results.email ? '✅ 성공' : '❌ 실패'}\\n`;
        testMessage += `💬 슬랙: ${results.slack ? '✅ 성공' : '❌ 실패'}\\n`;

        if (results.webhooks && typeof results.webhooks === 'object') {
          const webhookResults = Object.entries(results.webhooks);
          testMessage += `🔗 웹훅: ${webhookResults.length}개 테스트\\n`;
          webhookResults.forEach(([url, success]) => {
            testMessage += `  - ${url}: ${success ? '✅' : '❌'}\\n`;
          });
        }

        setMessage(testMessage);
      } else {
        setMessage('❌ 연결 테스트 중 오류가 발생했습니다.');
      }
    } catch (error) {
      setMessage(`❌ 연결 테스트 중 오류가 발생했습니다: ${error.message}`);
    }
    setLoading(false);
  };

  return (
    <div className="bg-white rounded-lg shadow p-6">
      <h2 className="text-xl font-semibold mb-6">📨 알림 설정</h2>

      {/* 알림 서비스 상태 */}
      {notificationStatus && (
        <div className="mb-6 p-4 bg-gray-50 rounded-lg">
          <h3 className="font-medium mb-3">🔧 서비스 상태</h3>
          <div className="grid grid-cols-2 gap-4 text-sm">
            <div>
              <span className="font-medium">이메일 설정:</span>
              <span className={`ml-2 ${notificationStatus.email_configured ? 'text-green-600' : 'text-red-600'}`}>
                {notificationStatus.email_configured ? '✅ 설정됨' : '❌ 미설정'}
              </span>
            </div>
            <div>
              <span className="font-medium">슬랙 설정:</span>
              <span className={`ml-2 ${notificationStatus.slack_configured ? 'text-green-600' : 'text-red-600'}`}>
                {notificationStatus.slack_configured ? '✅ 설정됨' : '❌ 미설정'}
              </span>
            </div>
            <div>
              <span className="font-medium">웹훅 설정:</span>
              <span className={`ml-2 ${notificationStatus.webhooks_configured ? 'text-green-600' : 'text-red-600'}`}>
                {notificationStatus.webhooks_configured ? `✅ ${notificationStatus.webhook_urls_count}개` : '❌ 미설정'}
              </span>
            </div>
            <div>
              <span className="font-medium">자동 전송:</span>
              <span className="ml-2">
                📧{notificationStatus.auto_send_email ? '✅' : '❌'}
                💬{notificationStatus.auto_send_slack ? '✅' : '❌'}
              </span>
            </div>
          </div>
        </div>
      )}

      {/* 연결 테스트 */}
      <div className="mb-6">
        <button
          onClick={handleTestNotifications}
          disabled={loading}
          className="bg-blue-500 hover:bg-blue-600 text-white px-4 py-2 rounded-lg disabled:opacity-50"
        >
          {loading ? '테스트 중...' : '🧪 연결 테스트'}
        </button>
      </div>

      {/* 이메일 구독 추가 */}
      <div className="mb-6">
        <h3 className="font-medium mb-3">📧 이메일 구독 추가</h3>
        <form onSubmit={handleSubscribeEmail} className="flex gap-2 mb-4">
          <input
            type="email"
            value={newEmail}
            onChange={(e) => setNewEmail(e.target.value)}
            placeholder="이메일 주소 입력"
            className="flex-1 px-3 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
            required
          />
          <select
            value={digestType}
            onChange={(e) => setDigestType(e.target.value)}
            className="px-3 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
          >
            <option value="daily">일간</option>
            <option value="weekly">주간</option>
            <option value="both">일간 + 주간</option>
          </select>
          <button
            type="submit"
            disabled={loading}
            className="bg-green-500 hover:bg-green-600 text-white px-4 py-2 rounded-lg disabled:opacity-50"
          >
            {loading ? '추가 중...' : '추가'}
          </button>
        </form>

        {/* 키워드 기반 구독 토글 */}
        <div className="flex items-center gap-2 mb-3">
          <button
            type="button"
            onClick={() => setShowKeywordForm(!showKeywordForm)}
            className="text-blue-500 hover:text-blue-700 text-sm underline"
          >
            🔍 키워드 기반 맞춤 구독 {showKeywordForm ? '숨기기' : '설정하기'}
          </button>
        </div>

        {/* 키워드 기반 구독 폼 */}
        {showKeywordForm && (
          <div className="p-4 bg-blue-50 border border-blue-200 rounded-lg">
            <div className="flex items-center justify-between mb-3">
              <h4 className="font-medium text-blue-800">
                {editingSubscription ? '✏️ 키워드 구독 수정' : '🎯 키워드 맞춤 구독'}
              </h4>
              {editingSubscription && (
                <button
                  type="button"
                  onClick={() => {
                    setEditingSubscription(null);
                    setNewEmail('');
                    setNewKeywords('');
                    setShowKeywordForm(false);
                  }}
                  className="text-gray-500 hover:text-gray-700"
                >
                  ✖️ 취소
                </button>
              )}
            </div>
            <form onSubmit={editingSubscription ? handleUpdateSubscription : handleSubscribeKeywords} className="space-y-3">
              <input
                type="email"
                value={newEmail}
                onChange={(e) => setNewEmail(e.target.value)}
                placeholder="이메일 주소 입력"
                className={`w-full px-3 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 ${editingSubscription ? 'bg-gray-100' : ''}`}
                readOnly={editingSubscription}
                required
              />
              <textarea
                value={newKeywords}
                onChange={(e) => setNewKeywords(e.target.value)}
                placeholder="관심 키워드를 쉼표로 구분하여 입력하세요 (예: transformer, attention, neural network, computer vision)"
                rows="3"
                className="w-full px-3 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
                required
              />
              <div className="flex gap-2">
                <select
                  value={digestType}
                  onChange={(e) => setDigestType(e.target.value)}
                  className="px-3 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
                >
                  <option value="daily">일간</option>
                  <option value="weekly">주간</option>
                  <option value="both">일간 + 주간</option>
                </select>
                <button
                  type="submit"
                  disabled={loading}
                  className="bg-blue-500 hover:bg-blue-600 text-white px-4 py-2 rounded-lg disabled:opacity-50"
                >
                  {loading ? (editingSubscription ? '업데이트 중...' : '구독 중...') : (editingSubscription ? '키워드 업데이트' : '키워드 구독')}
                </button>
              </div>
            </form>
            <p className="text-xs text-blue-600 mt-2">
              💡 키워드 기반 구독: 입력한 키워드와 관련된 논문만 필터링하여 맞춤형 다이제스트를 받을 수 있습니다.
            </p>
          </div>
        )}
      </div>

      {/* 메시지 표시 */}
      {message && (
        <div className="mb-4 p-3 bg-blue-50 border border-blue-200 rounded-lg text-sm whitespace-pre-line">
          {message}
        </div>
      )}

      {/* 이메일 구독자 목록 */}
      <div className="space-y-6">
        {/* 일간 구독자 */}
        <div>
          <h3 className="font-medium mb-3">📅 일간 다이제스트 구독자 ({emailSubscribers.daily.length}명)</h3>
          {emailSubscribers.daily.length === 0 ? (
            <p className="text-gray-500 text-sm">구독자가 없습니다.</p>
          ) : (
            <div className="space-y-2">
              {emailSubscribers.daily.map((email, index) => {
                const isKeywordSubscriber = keywordSubscribers.find(sub => sub.email === email && sub.digest_type === 'daily');
                return (
                  <div key={index} className="flex items-center justify-between p-2 bg-gray-50 rounded">
                    <div className="flex items-center gap-2">
                      <span className="text-sm">{email}</span>
                      {isKeywordSubscriber && (
                        <span className="text-xs bg-blue-100 text-blue-700 px-2 py-1 rounded">
                          🎯 키워드: {isKeywordSubscriber.keywords.join(', ')}
                        </span>
                      )}
                    </div>
                    <div className="flex gap-2">
                      {isKeywordSubscriber && (
                        <button
                          onClick={() => handleEditSubscription(isKeywordSubscriber)}
                          className="text-blue-500 hover:text-blue-700 text-sm"
                        >
                          수정
                        </button>
                      )}
                      <button
                        onClick={() => isKeywordSubscriber ? handleUnsubscribeKeywords(email) : handleUnsubscribeEmail(email, 'daily')}
                        className="text-red-500 hover:text-red-700 text-sm"
                      >
                        제거
                      </button>
                    </div>
                  </div>
                );
              })}
            </div>
          )}
        </div>

        {/* 주간 구독자 */}
        <div>
          <h3 className="font-medium mb-3">📊 주간 다이제스트 구독자 ({emailSubscribers.weekly.length}명)</h3>
          {emailSubscribers.weekly.length === 0 ? (
            <p className="text-gray-500 text-sm">구독자가 없습니다.</p>
          ) : (
            <div className="space-y-2">
              {emailSubscribers.weekly.map((email, index) => {
                const isKeywordSubscriber = keywordSubscribers.find(sub => sub.email === email && sub.digest_type === 'weekly');
                return (
                  <div key={index} className="flex items-center justify-between p-2 bg-gray-50 rounded">
                    <div className="flex items-center gap-2">
                      <span className="text-sm">{email}</span>
                      {isKeywordSubscriber && (
                        <span className="text-xs bg-blue-100 text-blue-700 px-2 py-1 rounded">
                          🎯 키워드: {isKeywordSubscriber.keywords.join(', ')}
                        </span>
                      )}
                    </div>
                    <div className="flex gap-2">
                      {isKeywordSubscriber && (
                        <button
                          onClick={() => handleEditSubscription(isKeywordSubscriber)}
                          className="text-blue-500 hover:text-blue-700 text-sm"
                        >
                          수정
                        </button>
                      )}
                      <button
                        onClick={() => isKeywordSubscriber ? handleUnsubscribeKeywords(email) : handleUnsubscribeEmail(email, 'weekly')}
                        className="text-red-500 hover:text-red-700 text-sm"
                      >
                        제거
                      </button>
                    </div>
                  </div>
                );
              })}
            </div>
          )}
        </div>

        {/* 키워드 구독 관리 (상세 정보용) */}
        <div>
          <details className="border border-gray-200 rounded-lg p-4">
            <summary className="font-medium cursor-pointer text-gray-700">
              🎯 키워드 구독 상세 관리 ({keywordSubscribers.length}명) - 클릭하여 펼치기
            </summary>
            <div className="mt-4">
              {keywordSubscribers.length === 0 ? (
                <p className="text-gray-500 text-sm">키워드 기반 구독자가 없습니다.</p>
              ) : (
                <div className="space-y-3">
                  {keywordSubscribers.map((subscriber, index) => (
                    <div key={index} className="p-3 bg-blue-50 border border-blue-200 rounded-lg">
                      <div className="flex items-center justify-between mb-2">
                        <span className="text-sm font-medium">{subscriber.email}</span>
                        <div className="flex items-center gap-2">
                          <span className="text-xs text-blue-600 bg-blue-100 px-2 py-1 rounded">
                            {subscriber.digest_type}
                          </span>
                          <div className="flex gap-2">
                            <button
                              onClick={() => handleEditSubscription(subscriber)}
                              className="text-blue-500 hover:text-blue-700 text-sm"
                            >
                              수정
                            </button>
                            <button
                              onClick={() => handleUnsubscribeKeywords(subscriber.email)}
                              className="text-red-500 hover:text-red-700 text-sm"
                            >
                              제거
                            </button>
                          </div>
                        </div>
                      </div>
                      <div className="flex flex-wrap gap-1">
                        {subscriber.keywords.length > 0 ? (
                          subscriber.keywords.map((keyword, kIndex) => (
                            <span key={kIndex} className="text-xs bg-blue-200 text-blue-800 px-2 py-1 rounded">
                              {keyword}
                            </span>
                          ))
                        ) : (
                          <span className="text-xs text-gray-500">모든 논문 수신 (키워드 없음)</span>
                        )}
                      </div>
                      <div className="text-xs text-gray-500 mt-1">
                        가입: {new Date(subscriber.created_at).toLocaleDateString('ko-KR')}
                        {subscriber.updated_at !== subscriber.created_at && (
                          <span> | 수정: {new Date(subscriber.updated_at).toLocaleDateString('ko-KR')}</span>
                        )}
                      </div>
                    </div>
                  ))}
                </div>
              )}
            </div>
          </details>
        </div>
      </div>

      {/* 설정 안내 */}
      <div className="mt-6 p-4 bg-yellow-50 border border-yellow-200 rounded-lg">
        <h4 className="font-medium text-yellow-800 mb-2">⚙️ 알림 설정 방법</h4>
        <div className="text-sm text-yellow-700 space-y-1">
          <p><strong>이메일:</strong> .env 파일에 EMAIL_* 설정 추가</p>
          <p><strong>슬랙:</strong> .env 파일에 SLACK_WEBHOOK_URL 설정 추가</p>
          <p><strong>웹훅:</strong> .env 파일에 NOTIFICATION_WEBHOOKS 설정 추가 (n8n, Zapier 등)</p>
          <p><strong>자동 전송:</strong> AUTO_SEND_EMAIL, AUTO_SEND_SLACK 설정으로 다이제스트 생성 시 자동 전송</p>
          <p><strong>키워드 구독:</strong> 관심 있는 키워드를 등록하여 맞춤형 논문 다이제스트 수신</p>
        </div>
      </div>
    </div>
  );
};

export default NotificationSettings;