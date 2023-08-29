/* eslint-disable class-methods-use-this */
import { BaseWebAnalyticsApi } from 'richie-education/js/api/web-analytics/base';

/**
 *
 * Xiti Richie Web Analytics API Implementation
 *
 * This implementation is used when web analytics is configured as `xiti`.
 * It will send events to the xiti.
 *
 */
export default class XitiApi extends BaseWebAnalyticsApi {
  PA: any;

  constructor() {
    super();

    const PA = (window as any)?.PA;

    // User has denied being tracked or an adblocker has blocked the tag initialization.
    if (PA === undefined) {
      return;
    }

    this.PA = PA;
  }

  sendEvent(actionName: string, category: string, action: string, label: string): void {
    this.PA?.tag.sendEvent('click.action', {
      ...this.PA?.data,
      click: category,
      's:resource_link': label,
    });
  }
}
