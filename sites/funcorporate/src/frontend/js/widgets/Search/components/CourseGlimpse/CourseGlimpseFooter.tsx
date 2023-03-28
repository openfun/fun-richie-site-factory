import React from 'react';
import { defineMessages, useIntl } from 'react-intl';

import { CommonDataProps } from 'richie-education/js/types/commonDataProps';
import { Course } from 'richie-education/js/types/Course';
import { Icon } from 'richie-education/js/components/Icon';

const messages = defineMessages({
  dateIconAlt: {
    defaultMessage: 'Course duration',
    description: 'Course duration logo alternative text for screen reader users',
    id: 'components.CourseGlimpseFooter.dateIconAlt',
  },
});

/**
 * <CourseGlimpseFooter />.
 * This is spun off from <CourseGlimpse /> to allow easier override through webpack.
 */
export const CourseGlimpseFooter: React.FC<{ course: Course } & CommonDataProps> = ({ course }) => {
  const intl = useIntl();

  return (
    <div className="course-glimpse-footer">
      <div className="course-glimpse-footer__date">
        <Icon name="icon-clock" title={intl.formatMessage(messages.dateIconAlt)} />
        {course.duration}
      </div>
    </div>
  );
};
