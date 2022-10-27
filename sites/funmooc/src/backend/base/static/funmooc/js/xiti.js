(function () {
  /**
   * Deserialize a context analytic dimension
   *
   * @param dimension - string with items joined by ' | '
   * @param toArray - flag to enforce to return result as Array
   * @return data
   *    - [] || undefined if the dimension string was empty
   *    - [value] or value if the dimension cannot be split
   *    - An array of values if dimension has been split
   */
  function deserialize(dimension, toArray = false) {
    const data = dimension.split(' | ');
    if (data.length === 1) {
      if (!data[0].trim()) return toArray ? [] : undefined;
      return toArray ? data : data[0];
    }
    return data;
  }

  /**
   *
   * An object to initialize then use Piano Analytics Tag.
   *
   * @param metadata - analytics context
   *
   *  - id: AT Internet site id to identify the site on Analytics Suite
   *  - provider: 'xiti',
   *  - dimensions: some serialized data related to the current page
   *    + course_code
   *    + course_runs_resource_links
   *    + course_runs_titles
   *    + organizations_codes
   *    + page_title
   *    + root_page_id: level2
   *
   */
  function PATag(metadata) {
    this.data = null;
    this.level2 = metadata.dimensions.root_page_id;
    this.organizations = deserialize(metadata.dimensions.organizations_codes, true);
    this.siteId = metadata.id;
    this.tag = null;

    /**
     * Populate the data object sent to Xiti on dispatch.
     * It includes level2, name and chapters
     *
     * To get name and chapters we split the url pathname "/"
     * name is the first element of this destructuring
     * chapters are the remaining elements
     */
    this.populateData = function () {
      var self = this;
      var chapters = location.pathname
        .split('/')
        .filter(function (slug) {
          return slug.length > 0;
        })
        .slice(1); // Remove lang

      var name = chapters.shift();

      this.data = {
        page: name || '/',
        site_level2: this.level2,
      };

      chapters.forEach(function (chapter, index) {
        self.data['page_chapter' + (index + 1)] = chapter;
      });

      // Detail language
      var lang = (document.documentElement.lang || '-').split('-')[0].toLowerCase();
      if (lang) {
        self.data.langue = lang;
      }

      // Detail organizations related to the page
      if (this.organizations && this.organizations.length > 0) {
        self.data['a:s:organizations'] =
          '[' +
          this.organizations
            .map(function (organization) {
              return '"' + organization + '"';
            })
            .toString() +
          ']';
      }
    };

    /**
     * Dispatch data on page display
     * Set internalSearch if it is relevant then dispatch a record.
     */
    this.dispatch = function () {
      // Detail search query if there is
      var searchParams = new URL(location.href).searchParams;

      if (searchParams.has('query')) {
        var searchQuery = searchParams.get('query');
        var searchLimit = searchParams.get('limit') || 0;
        var searchOffset = searchParams.get('offset') || 0;
        this.tag.sendEvent('internal_search_result.display', Object.assign({
          ise_keyword: searchQuery,
          ise_page: 1 + (searchOffset / searchLimit),
        }, this.data));
      }

      // Dispatch data
      this.tag.sendEvent('page.display', this.data);
    };

    /**
     * Configure the PA tag
     * Check if `pa` exists then configure the tag with our site information.
     */
    this.createTag = function () {
      if (pa) {
        this.tag = pa;
        this.tag.setConfigurations({
          collectDomain: 'https://logs1409.xiti.com',
          secure: true,
          site: this.siteId,
        });
      }
    };

    /**
     * Add click event listeners on all buttons on the page.
     * Send a record each time a visitor click on an action button on the page.
     */
    this.spyClickOnButtons = function () {
      var self = this;

      function spyClick(event) {
        var $target = event.currentTarget;
        var name = $target.innerText || $target.classList.value.replace(' ', '.');

        var parameters = self.data;
        parameters.page = name;

        self.tag.sendEvent('click.action', parameters, { elem: $target, event: event });
      }

      // Some browsers do not implement `HTMLCollection.forEach` method
      // so we transform HTMLCollection into an Array
      var $buttons = [].slice.call(document.getElementsByTagName('button'));
      $buttons.forEach(($button) => {
        $button.addEventListener('click', spyClick, false);
      });
    };

    /**
     * Initialize PATag
     *
     * Create PATag, populate data then dispatch a record
     * and add click listeners on buttons
     */
    this.init = function () {
      this.createTag();
      this.populateData();
      this.dispatch();
      this.spyClickOnButtons();
    };
  }

  var context = window.__funmooc_context__.analytics;

  tarteaucitron.services.paFun = {
    key: 'xiti',
    type: 'analytic',
    name: 'Piano Analytics',
    uri: 'https://www.atinternet.com/societe/rgpd-et-vie-privee/',
    needConsent: false,
    cookies: ['pa_vid', 'pa_privacy'],
    js: function () {
      var pa_url = 'https://tag.aticdn.net/piano-analytics.js';
      function onLoad() {
        const PA = new PATag(context);
        PA.init()
        // expose PATag globally
        window.PA = PA;
      }
      tarteaucitron.addScript(pa_url, '', onLoad);
    },
  };
  tarteaucitron.job.push('paFun');
})();
