module.exports = function(grunt) {
  grunt.initConfig({
    pkg: grunt.file.readJSON('package.json'),

    // requirejs: {
    //   compile: {
    //     options: {
    //       baseUrl: "./",
    //       mainConfigFile: "static/js/config.js",
    //       name: "static_build/js/vendors/almond.js",
    //       out: "static_build/js/app.js"
    //     }
    //   }
    // },

    // shell: {
    //     options: {
    //         stderr: false
    //     },
    //     buildJs: {
    //         command: './node_modules/.bin/r.js -o build.js'
    //     }
    // },

    // requirejs: {
    //   compile: {
    //     options: {
    //       findNestedDependencies: true,
    //       baseUrl : './',
    //       mainConfigFile: "static/js/config.js",
    //       name : 'static/js/main.js',
    //       out : "static_build/js/app.js",
    //       optimize : 'none'
    //     }
    //   }
    // },

    sass: {
      options: {
        loadPath: [
          'static/bower_components/foundation/scss',
        ]
      },
      dist: {
        options: {
          style: 'expanded'
        },
        files: {
          'static/css/app.css': 'static/scss/app.scss'
        }
      }
    },

    watch: {
      scripts: {
        files: [
          'static/scss/**/*.scss',
        ],
        tasks: ['sass'],
        options: {
          spawn: false,
        },
      },
    },

    copy: {
      main: {
        files: [
          {
            expand: true,
            cwd: './static/images',
            src: ['**/*'],
            dest: 'static_build/images/',
            filter: 'isFile'
          },
          {
            expand: true,
            cwd: './static/css',
            src: ['**/*'],
            dest: 'static_build/css/',
            filter: 'isFile'
          },
          {
            flatten: true,
            expand: true,
            cwd: './',
            src: [
              'static/bower_components/modernizr/modernizr.js',
              'static/bower_components/almond/almond.js',
              'static/bower_components/requirejs/require.js'
            ],
            dest: 'static_build/js/vendors/'
          }
        ]
      },
      vendors: {
        files: [
          {
            flatten: true,
            expand: true,
            cwd: './',
            src: [
              'static/bower_components/modernizr/modernizr.js',
              'static/bower_components/almond/almond.js',
              'static/bower_components/requirejs/require.js'
            ],
            dest: 'static/js/vendors/'
          }
        ]
      }
    },

    clean: ["static_build"]
  });

  grunt.loadNpmTasks('grunt-contrib-sass');
  grunt.loadNpmTasks('grunt-contrib-watch');
  grunt.loadNpmTasks('grunt-contrib-copy');
  grunt.loadNpmTasks('grunt-contrib-clean');

  // grunt.registerTask('build', ['clean', 'sass', 'copy', 'requirejs']);
  // grunt.registerTask('build', ['clean', 'copy', 'shell:buildJs']);
  grunt.registerTask('default', ['watch']);
};