import React from 'react';
import { defineMessages, useIntl } from 'react-intl';

import { CommonDataProps } from 'richie-education/js/types/commonDataProps';
import { Icon, IconTypeEnum } from 'richie-education/js/components/Icon';
import { CourseGlimpseCourse } from 'richie-education/js/components/CourseGlimpse';

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
export const CourseGlimpseFooter: React.FC<{ course: CourseGlimpseCourse } & CommonDataProps> = ({
  course,
}) => {
  const intl = useIntl();

  return (
    <div className="course-glimpse-footer">
      <div className="course-glimpse-footer__column course-glimpse-footer__date">
        <Icon
          name={IconTypeEnum.CLOCK}
          title={intl.formatMessage(messages.dateIconAlt)}
          size="small"
        />
        {course.duration}
      </div>
    </div>
  );
};
