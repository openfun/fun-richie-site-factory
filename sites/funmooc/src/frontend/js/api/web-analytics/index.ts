import { Maybe } from 'richie-education/js/types/utils';
import { CourseProductEvent, WebAnalyticsAPI } from 'richie-education/js/types/web-analytics';
import context from 'richie-education/js/utils/context';
import { handle } from 'richie-education/js/utils/errors/handle';
// @ts-ignore
import PianoAnalyticsApi from '../../../../../js/api/web-analytics/pianoanalytics';

enum FunMoocWebAnalyticsBackend {
  PIANOANALYTICS = 'pianoanalytics',
}

const WEB_ANALYTICS_PROVIDERS = context?.web_analytics_providers;

/**
 * Delegate event calls to all configured web analytics providers.
 */
class WebAnalyticsAPIDelegator2Providers implements WebAnalyticsAPI {
  providers: WebAnalyticsAPI[];
  constructor(providers: WebAnalyticsAPI[]) {
    this.providers = providers;
  }

  sendEnrolledEvent(resourceLink: string): void {
    this.providers.forEach((provider) => provider.sendEnrolledEvent(resourceLink));
  }

  sendCourseProductEvent(category: CourseProductEvent, productKey: string): void {
    this.providers.forEach((provider) => provider.sendCourseProductEvent(category, productKey));
  }
}

const WebAnalyticsAPIHandler = (): Maybe<WebAnalyticsAPIDelegator2Providers> => {
  const providers: WebAnalyticsAPI[] = [];
  try {
    if (WEB_ANALYTICS_PROVIDERS?.includes(FunMoocWebAnalyticsBackend.PIANOANALYTICS)) {
      providers.push(new PianoAnalyticsApi());
    }
  } catch (error) {
    handle(error);
  }
  return providers.length === 0 ? undefined : new WebAnalyticsAPIDelegator2Providers(providers);
};

export default WebAnalyticsAPIHandler;
