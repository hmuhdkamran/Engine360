<template>
  <page-view>
    <!--begin::Row-->
    <div class="row">
      <div class="col-xl-4">
        <!--begin::Tiles Widget 1-->
        <div class="card card-custom gutter-b card-stretch">
          <!--begin::Header-->
          <div class="card-header border-0 pt-5">
            <div class="card-title">
              <div class="card-label">
                <div class="font-weight-bolder">Weekly Sales Stats</div>
                <div class="font-size-sm text-muted mt-2">890,344 Sales</div>
              </div>
            </div>
            <div class="card-toolbar">
              <div class="dropdown dropdown-inline">
                <a
                  href="#"
                  class="btn btn-clean btn-sm btn-icon"
                  data-toggle="dropdown"
                  aria-haspopup="true"
                  aria-expanded="false"
                >
                  <i class="ki ki-bold-more-hor"></i>
                </a>
                <div class="dropdown-menu dropdown-menu-md dropdown-menu-right">
                  <!--begin::Navigation-->
                  <ul class="navi navi-hover py-5">
                    <li class="navi-item">
                      <a href="#" class="navi-link">
                        <span class="navi-icon">
                          <i class="flaticon2-drop"></i>
                        </span>
                        <span class="navi-text">New Group</span>
                      </a>
                    </li>
                    <li class="navi-item">
                      <a href="#" class="navi-link">
                        <span class="navi-icon">
                          <i class="flaticon2-list-3"></i>
                        </span>
                        <span class="navi-text">Contacts</span>
                      </a>
                    </li>
                    <li class="navi-item">
                      <a href="#" class="navi-link">
                        <span class="navi-icon">
                          <i class="flaticon2-rocket-1"></i>
                        </span>
                        <span class="navi-text">Groups</span>
                        <span class="navi-link-badge">
                          <span class="label label-light-primary label-inline font-weight-bold">new</span>
                        </span>
                      </a>
                    </li>
                    <li class="navi-item">
                      <a href="#" class="navi-link">
                        <span class="navi-icon">
                          <i class="flaticon2-bell-2"></i>
                        </span>
                        <span class="navi-text">Calls</span>
                      </a>
                    </li>
                    <li class="navi-item">
                      <a href="#" class="navi-link">
                        <span class="navi-icon">
                          <i class="flaticon2-gear"></i>
                        </span>
                        <span class="navi-text">Settings</span>
                      </a>
                    </li>
                    <li class="navi-separator my-3"></li>
                    <li class="navi-item">
                      <a href="#" class="navi-link">
                        <span class="navi-icon">
                          <i class="flaticon2-magnifier-tool"></i>
                        </span>
                        <span class="navi-text">Help</span>
                      </a>
                    </li>
                    <li class="navi-item">
                      <a href="#" class="navi-link">
                        <span class="navi-icon">
                          <i class="flaticon2-bell-2"></i>
                        </span>
                        <span class="navi-text">Privacy</span>
                        <span class="navi-link-badge">
                          <span class="label label-light-danger label-rounded font-weight-bold">5</span>
                        </span>
                      </a>
                    </li>
                  </ul>
                  <!--end::Navigation-->
                </div>
              </div>
            </div>
          </div>
          <!--end::Header-->
          <!--begin::Body-->
          <div class="card-body d-flex flex-column px-0">
            <!--begin::Chart-->
            <div id="kt_tiles_widget_1_chart" data-color="danger" style="height: 150px"></div>
            <!--end::Chart-->
            <!--begin::Items-->
            <div class="flex-grow-1 card-spacer-x">
              <!--begin::Item-->
              <div class="d-flex align-items-center justify-content-between mb-10">
                <div class="d-flex align-items-center mr-2">
                  <div class="symbol symbol-50 symbol-light mr-3 flex-shrink-0">
                    <div class="symbol-label">
                      <img src="assets/media/svg/misc/006-plurk.svg" alt class="h-50" />
                    </div>
                  </div>
                  <div>
                    <a
                      href="#"
                      class="font-size-h6 text-dark-75 text-hover-primary font-weight-bolder"
                    >Top Authors</a>
                    <div
                      class="font-size-sm text-muted font-weight-bold mt-1"
                    >Ricky Hunt, Sandra Trepp</div>
                  </div>
                </div>
                <div
                  class="label label-light label-inline font-weight-bold text-dark-50 py-4 px-3 font-size-base"
                >+105$</div>
              </div>
              <!--end::Item-->
              <!--begin::Item-->
              <div class="d-flex align-items-center justify-content-between mb-10">
                <div class="d-flex align-items-center mr-2">
                  <div class="symbol symbol-50 symbol-light mr-3 flex-shrink-0">
                    <div class="symbol-label">
                      <img src="assets/media/svg/misc/015-telegram.svg" alt class="h-50" />
                    </div>
                  </div>
                  <div>
                    <a
                      href="#"
                      class="font-size-h6 text-dark-75 text-hover-primary font-weight-bolder"
                    >Bestsellers</a>
                    <div
                      class="font-size-sm text-muted font-weight-bold mt-1"
                    >Pitstop Email Marketing</div>
                  </div>
                </div>
                <div
                  class="label label-light label-inline font-weight-bold text-dark-50 py-4 px-3 font-size-base"
                >+60$</div>
              </div>
              <!--end::Item-->
              <!--begin::Item-->
              <div class="d-flex align-items-center justify-content-between">
                <div class="d-flex align-items-center mr-2">
                  <div class="symbol symbol-50 symbol-light mr-3 flex-shrink-0">
                    <div class="symbol-label">
                      <img src="assets/media/svg/misc/003-puzzle.svg" alt class="h-50" />
                    </div>
                  </div>
                  <div>
                    <a
                      href="#"
                      class="font-size-h6 text-dark-75 text-hover-primary font-weight-bolder"
                    >Top Engagement</a>
                    <div
                      class="font-size-sm text-muted font-weight-bold mt-1"
                    >KT.com solution provider</div>
                  </div>
                </div>
                <div
                  class="label label-light label-inline font-weight-bold text-dark-50 py-4 px-3 font-size-base"
                >+75$</div>
              </div>
              <!--end::Item-->
            </div>
            <!--end::Items-->
          </div>
          <!--end::Body-->
        </div>
        <!--end::Tiles Widget 1-->
      </div>
      <div class="col-xl-8">
        <div class="row">
          <div class="col-xl-3">
            <!--begin::Tiles Widget 3-->
            <div
              class="card card-custom bgi-no-repeat bgi-no-repeat bgi-size-cover gutter-b"
              style="height: 150px; background-image: url(assets/media/bg/bg-9.jpg)"
            >
              <!--begin::Body-->
              <div class="card-body d-flex flex-column">
                <!--begin::Title-->
                <a
                  href="#"
                  class="text-dark-75 text-hover-primary font-weight-bolder font-size-h3"
                >Properties</a>
                <!--end::Title-->
              </div>
              <!--end::Body-->
            </div>
            <!--end::Tiles Widget 3-->
          </div>
          <div class="col-xl-9">
            <!--begin::Mixed Widget 10-->
            <div class="card card-custom gutter-b" style="height: 150px">
              <!--begin::Body-->
              <div class="card-body d-flex align-items-center justify-content-between flex-wrap">
                <div class="mr-2">
                  <h3 class="font-weight-bolder">Create CRM Reports</h3>
                  <div class="text-dark-50 font-size-lg mt-2">Generate the latest CRM Report</div>
                </div>
                <a href="#" class="btn btn-primary font-weight-bold py-3 px-6">Start Now</a>
              </div>
              <!--end::Body-->
            </div>
            <!--end::Mixed Widget 10-->
          </div>
        </div>
        <div class="row">
          <div class="col-xl-6">
            <!--begin::Tiles Widget 13-->
            <div
              class="card card-custom bgi-no-repeat gutter-b"
              style="height: 175px; background-color: #663259; background-position: calc(100% + 0.5rem) 100%; background-size: 100% auto; background-image: url(assets/media/svg/patterns/taieri.svg)"
            >
              <!--begin::Body-->
              <div class="card-body d-flex align-items-center">
                <div>
                  <h3 class="text-white font-weight-bolder line-height-lg mb-5">
                    Create SaaS
                    <br />Based Reports
                  </h3>
                  <a href="#" class="btn btn-success font-weight-bold px-6 py-3">Create Report</a>
                </div>
              </div>
              <!--end::Body-->
            </div>
            <!--end::Tiles Widget 13-->
            <div class="row">
              <div class="col-xl-6">
                <!--begin::Tiles Widget 11-->
                <div class="card card-custom bg-primary gutter-b" style="height: 150px">
                  <div class="card-body">
                    <span class="svg-icon svg-icon-3x svg-icon-white ml-n2">
                      <!--begin::Svg Icon | path:assets/media/svg/icons/Layout/Layout-4-blocks.svg-->
                      <svg
                        xmlns="http://www.w3.org/2000/svg"
                        xmlns:xlink="http://www.w3.org/1999/xlink"
                        width="24px"
                        height="24px"
                        viewBox="0 0 24 24"
                        version="1.1"
                      >
                        <g stroke="none" stroke-width="1" fill="none" fill-rule="evenodd">
                          <rect x="0" y="0" width="24" height="24" />
                          <rect fill="#000000" x="4" y="4" width="7" height="7" rx="1.5" />
                          <path
                            d="M5.5,13 L9.5,13 C10.3284271,13 11,13.6715729 11,14.5 L11,18.5 C11,19.3284271 10.3284271,20 9.5,20 L5.5,20 C4.67157288,20 4,19.3284271 4,18.5 L4,14.5 C4,13.6715729 4.67157288,13 5.5,13 Z M14.5,4 L18.5,4 C19.3284271,4 20,4.67157288 20,5.5 L20,9.5 C20,10.3284271 19.3284271,11 18.5,11 L14.5,11 C13.6715729,11 13,10.3284271 13,9.5 L13,5.5 C13,4.67157288 13.6715729,4 14.5,4 Z M14.5,13 L18.5,13 C19.3284271,13 20,13.6715729 20,14.5 L20,18.5 C20,19.3284271 19.3284271,20 18.5,20 L14.5,20 C13.6715729,20 13,19.3284271 13,18.5 L13,14.5 C13,13.6715729 13.6715729,13 14.5,13 Z"
                            fill="#000000"
                            opacity="0.3"
                          />
                        </g>
                      </svg>
                      <!--end::Svg Icon-->
                    </span>
                    <div class="text-inverse-primary font-weight-bolder font-size-h2 mt-3">790</div>
                    <a
                      href="#"
                      class="text-inverse-primary font-weight-bold font-size-lg mt-1"
                    >New Products</a>
                  </div>
                </div>
                <!--end::Tiles Widget 11-->
              </div>
              <div class="col-xl-6">
                <!--begin::Tiles Widget 12-->
                <div class="card card-custom gutter-b" style="height: 150px">
                  <div class="card-body">
                    <span class="svg-icon svg-icon-3x svg-icon-success">
                      <!--begin::Svg Icon | path:assets/media/svg/icons/Communication/Group.svg-->
                      <svg
                        xmlns="http://www.w3.org/2000/svg"
                        xmlns:xlink="http://www.w3.org/1999/xlink"
                        width="24px"
                        height="24px"
                        viewBox="0 0 24 24"
                        version="1.1"
                      >
                        <g stroke="none" stroke-width="1" fill="none" fill-rule="evenodd">
                          <polygon points="0 0 24 0 24 24 0 24" />
                          <path
                            d="M18,14 C16.3431458,14 15,12.6568542 15,11 C15,9.34314575 16.3431458,8 18,8 C19.6568542,8 21,9.34314575 21,11 C21,12.6568542 19.6568542,14 18,14 Z M9,11 C6.790861,11 5,9.209139 5,7 C5,4.790861 6.790861,3 9,3 C11.209139,3 13,4.790861 13,7 C13,9.209139 11.209139,11 9,11 Z"
                            fill="#000000"
                            fill-rule="nonzero"
                            opacity="0.3"
                          />
                          <path
                            d="M17.6011961,15.0006174 C21.0077043,15.0378534 23.7891749,16.7601418 23.9984937,20.4 C24.0069246,20.5466056 23.9984937,21 23.4559499,21 L19.6,21 C19.6,18.7490654 18.8562935,16.6718327 17.6011961,15.0006174 Z M0.00065168429,20.1992055 C0.388258525,15.4265159 4.26191235,13 8.98334134,13 C13.7712164,13 17.7048837,15.2931929 17.9979143,20.2 C18.0095879,20.3954741 17.9979143,21 17.2466999,21 C13.541124,21 8.03472472,21 0.727502227,21 C0.476712155,21 -0.0204617505,20.45918 0.00065168429,20.1992055 Z"
                            fill="#000000"
                            fill-rule="nonzero"
                          />
                        </g>
                      </svg>
                      <!--end::Svg Icon-->
                    </span>
                    <div class="text-dark font-weight-bolder font-size-h2 mt-3">8,600</div>
                    <a
                      href="#"
                      class="text-muted text-hover-primary font-weight-bold font-size-lg mt-1"
                    >New Customers</a>
                  </div>
                </div>
                <!--end::Tiles Widget 12-->
              </div>
            </div>
          </div>
          <div class="col-xl-6">
            <!--begin::Mixed Widget 14-->
            <div
              class="card card-custom bgi-no-repeat bgi-size-cover gutter-b card-stretch"
              style="background-image: url(assets/media/stock-600x600/img-16.jpg)"
            >
              <!--begin::Body-->
              <div class="card-body d-flex flex-column align-items-start justify-content-start">
                <div class="p-1 flex-grow-1">
                  <h3 class="text-white font-weight-bolder line-height-lg mb-5">
                    Create Reports
                    <br />With App
                  </h3>
                </div>
                <a href="#" class="btn btn-link btn-link-warning font-weight-bold">
                  Create Report
                  <span class="svg-icon svg-icon-lg svg-icon-warning">
                    <!--begin::Svg Icon | path:assets/media/svg/icons/Navigation/Arrow-right.svg-->
                    <svg
                      xmlns="http://www.w3.org/2000/svg"
                      xmlns:xlink="http://www.w3.org/1999/xlink"
                      width="24px"
                      height="24px"
                      viewBox="0 0 24 24"
                      version="1.1"
                    >
                      <g stroke="none" stroke-width="1" fill="none" fill-rule="evenodd">
                        <polygon points="0 0 24 0 24 24 0 24" />
                        <rect
                          fill="#000000"
                          opacity="0.3"
                          transform="translate(12.000000, 12.000000) rotate(-90.000000) translate(-12.000000, -12.000000)"
                          x="11"
                          y="5"
                          width="2"
                          height="14"
                          rx="1"
                        />
                        <path
                          d="M9.70710318,15.7071045 C9.31657888,16.0976288 8.68341391,16.0976288 8.29288961,15.7071045 C7.90236532,15.3165802 7.90236532,14.6834152 8.29288961,14.2928909 L14.2928896,8.29289093 C14.6714686,7.914312 15.281055,7.90106637 15.675721,8.26284357 L21.675721,13.7628436 C22.08284,14.136036 22.1103429,14.7686034 21.7371505,15.1757223 C21.3639581,15.5828413 20.7313908,15.6103443 20.3242718,15.2371519 L15.0300721,10.3841355 L9.70710318,15.7071045 Z"
                          fill="#000000"
                          fill-rule="nonzero"
                          transform="translate(14.999999, 11.999997) scale(1, -1) rotate(90.000000) translate(-14.999999, -11.999997)"
                        />
                      </g>
                    </svg>
                    <!--end::Svg Icon-->
                  </span>
                </a>
              </div>
              <!--end::Body-->
            </div>
            <!--end::Mixed Widget 14-->
          </div>
        </div>
      </div>
    </div>
    <!--end::Row-->
    <!--begin::Row-->
    <div class="row">
      <div class="col-lg-6 col-xxl-4">
        <!--begin::Mixed Widget 4-->
        <div class="card card-custom bg-radial-gradient-danger gutter-b card-stretch">
          <!--begin::Header-->
          <div class="card-header border-0 py-5">
            <h3 class="card-title font-weight-bolder text-white">Sales Progress</h3>
            <div class="card-toolbar">
              <div class="dropdown dropdown-inline">
                <a
                  href="#"
                  class="btn btn-text-white btn-hover-white btn-sm btn-icon border-0"
                  data-toggle="dropdown"
                  aria-haspopup="true"
                  aria-expanded="false"
                >
                  <i class="ki ki-bold-more-hor"></i>
                </a>
                <div class="dropdown-menu dropdown-menu-sm dropdown-menu-right">
                  <!--begin::Navigation-->
                  <ul class="navi navi-hover">
                    <li class="navi-header pb-1">
                      <span
                        class="text-primary text-uppercase font-weight-bold font-size-sm"
                      >Add new:</span>
                    </li>
                    <li class="navi-item">
                      <a href="#" class="navi-link">
                        <span class="navi-icon">
                          <i class="flaticon2-shopping-cart-1"></i>
                        </span>
                        <span class="navi-text">Order</span>
                      </a>
                    </li>
                    <li class="navi-item">
                      <a href="#" class="navi-link">
                        <span class="navi-icon">
                          <i class="flaticon2-calendar-8"></i>
                        </span>
                        <span class="navi-text">Event</span>
                      </a>
                    </li>
                    <li class="navi-item">
                      <a href="#" class="navi-link">
                        <span class="navi-icon">
                          <i class="flaticon2-graph-1"></i>
                        </span>
                        <span class="navi-text">Report</span>
                      </a>
                    </li>
                    <li class="navi-item">
                      <a href="#" class="navi-link">
                        <span class="navi-icon">
                          <i class="flaticon2-rocket-1"></i>
                        </span>
                        <span class="navi-text">Post</span>
                      </a>
                    </li>
                    <li class="navi-item">
                      <a href="#" class="navi-link">
                        <span class="navi-icon">
                          <i class="flaticon2-writing"></i>
                        </span>
                        <span class="navi-text">File</span>
                      </a>
                    </li>
                  </ul>
                  <!--end::Navigation-->
                </div>
              </div>
            </div>
          </div>
          <!--end::Header-->
          <!--begin::Body-->
          <div class="card-body d-flex flex-column p-0">
            <!--begin::Chart-->
            <div id="kt_mixed_widget_6_chart" style="height: 200px"></div>
            <!--end::Chart-->
            <!--begin::Stats-->
            <div class="card-spacer bg-white card-rounded flex-grow-1">
              <!--begin::Row-->
              <div class="row m-0">
                <div class="col px-8 py-6 mr-8">
                  <div class="font-size-sm text-muted font-weight-bold">Average Sale</div>
                  <div class="font-size-h4 font-weight-bolder">$650</div>
                </div>
                <div class="col px-8 py-6">
                  <div class="font-size-sm text-muted font-weight-bold">Commission</div>
                  <div class="font-size-h4 font-weight-bolder">$233,600</div>
                </div>
              </div>
              <!--end::Row-->
              <!--begin::Row-->
              <div class="row m-0">
                <div class="col px-8 py-6 mr-8">
                  <div class="font-size-sm text-muted font-weight-bold">Annual Taxes</div>
                  <div class="font-size-h4 font-weight-bolder">$29,004</div>
                </div>
                <div class="col px-8 py-6">
                  <div class="font-size-sm text-muted font-weight-bold">Annual Income</div>
                  <div class="font-size-h4 font-weight-bolder">$1,480,00</div>
                </div>
              </div>
              <!--end::Row-->
            </div>
            <!--end::Stats-->
          </div>
          <!--end::Body-->
        </div>
        <!--end::Mixed Widget 4-->
      </div>
      <div class="col-lg-6 col-xxl-8">
        <!--begin::Advance Table Widget 1-->
        <div class="card card-custom card-stretch gutter-b">
          <!--begin::Header-->
          <div class="card-header border-0 py-5">
            <h3 class="card-title align-items-start flex-column">
              <span class="card-label font-weight-bolder text-dark">Agents Stats</span>
              <span class="text-muted mt-3 font-weight-bold font-size-sm">More than 400+ new members</span>
            </h3>
            <div class="card-toolbar">
              <a href="#" class="btn btn-success font-weight-bolder font-size-sm">
                <span class="svg-icon svg-icon-md svg-icon-white">
                  <!--begin::Svg Icon | path:assets/media/svg/icons/Communication/Add-user.svg-->
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    xmlns:xlink="http://www.w3.org/1999/xlink"
                    width="24px"
                    height="24px"
                    viewBox="0 0 24 24"
                    version="1.1"
                  >
                    <g stroke="none" stroke-width="1" fill="none" fill-rule="evenodd">
                      <polygon points="0 0 24 0 24 24 0 24" />
                      <path
                        d="M18,8 L16,8 C15.4477153,8 15,7.55228475 15,7 C15,6.44771525 15.4477153,6 16,6 L18,6 L18,4 C18,3.44771525 18.4477153,3 19,3 C19.5522847,3 20,3.44771525 20,4 L20,6 L22,6 C22.5522847,6 23,6.44771525 23,7 C23,7.55228475 22.5522847,8 22,8 L20,8 L20,10 C20,10.5522847 19.5522847,11 19,11 C18.4477153,11 18,10.5522847 18,10 L18,8 Z M9,11 C6.790861,11 5,9.209139 5,7 C5,4.790861 6.790861,3 9,3 C11.209139,3 13,4.790861 13,7 C13,9.209139 11.209139,11 9,11 Z"
                        fill="#000000"
                        fill-rule="nonzero"
                        opacity="0.3"
                      />
                      <path
                        d="M0.00065168429,20.1992055 C0.388258525,15.4265159 4.26191235,13 8.98334134,13 C13.7712164,13 17.7048837,15.2931929 17.9979143,20.2 C18.0095879,20.3954741 17.9979143,21 17.2466999,21 C13.541124,21 8.03472472,21 0.727502227,21 C0.476712155,21 -0.0204617505,20.45918 0.00065168429,20.1992055 Z"
                        fill="#000000"
                        fill-rule="nonzero"
                      />
                    </g>
                  </svg>
                  <!--end::Svg Icon-->
                </span>Add New Member
              </a>
            </div>
          </div>
          <!--end::Header-->
          <!--begin::Body-->
          <div class="card-body py-0">
            <!--begin::Table-->
            <div class="table-responsive">
              <table
                class="table table-head-custom table-vertical-center"
                id="kt_advance_table_widget_1"
              >
                <thead>
                  <tr class="text-left">
                    <th class="pl-0" style="width: 20px">
                      <label class="checkbox checkbox-lg checkbox-single">
                        <input type="checkbox" value="1" />
                        <span></span>
                      </label>
                    </th>
                    <th class="pr-0" style="width: 50px">authors</th>
                    <th style="min-width: 200px"></th>
                    <th style="min-width: 150px">company</th>
                    <th style="min-width: 150px">progress</th>
                    <th class="pr-0 text-right" style="min-width: 150px">action</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td class="pl-0">
                      <label class="checkbox checkbox-lg checkbox-single">
                        <input type="checkbox" value="1" />
                        <span></span>
                      </label>
                    </td>
                    <td class="pr-0">
                      <div class="symbol symbol-50 symbol-light mt-1">
                        <span class="symbol-label">
                          <img
                            src="assets/media/svg/avatars/001-boy.svg"
                            class="h-75 align-self-end"
                            alt
                          />
                        </span>
                      </div>
                    </td>
                    <td class="pl-0">
                      <a
                        href="#"
                        class="text-dark-75 font-weight-bolder text-hover-primary mb-1 font-size-lg"
                      >Brad Simmons</a>
                      <span class="text-muted font-weight-bold text-muted d-block">HTML, JS, ReactJS</span>
                    </td>
                    <td>
                      <span class="text-dark-75 font-weight-bolder d-block font-size-lg">Intertico</span>
                      <span class="text-muted font-weight-bold">Web, UI/UX Design</span>
                    </td>
                    <td>
                      <div class="d-flex flex-column w-100 mr-2">
                        <div class="d-flex align-items-center justify-content-between mb-2">
                          <span class="text-muted mr-2 font-size-sm font-weight-bold">65%</span>
                          <span class="text-muted font-size-sm font-weight-bold">Progress</span>
                        </div>
                        <div class="progress progress-xs w-100">
                          <div
                            class="progress-bar bg-danger"
                            role="progressbar"
                            style="width: 65%;"
                            aria-valuenow="50"
                            aria-valuemin="0"
                            aria-valuemax="100"
                          ></div>
                        </div>
                      </div>
                    </td>
                    <td class="pr-0 text-right">
                      <a href="#" class="btn btn-icon btn-light btn-hover-primary btn-sm">
                        <span class="svg-icon svg-icon-md svg-icon-primary">
                          <!--begin::Svg Icon | path:assets/media/svg/icons/General/Settings-1.svg-->
                          <svg
                            xmlns="http://www.w3.org/2000/svg"
                            xmlns:xlink="http://www.w3.org/1999/xlink"
                            width="24px"
                            height="24px"
                            viewBox="0 0 24 24"
                            version="1.1"
                          >
                            <g stroke="none" stroke-width="1" fill="none" fill-rule="evenodd">
                              <rect x="0" y="0" width="24" height="24" />
                              <path
                                d="M7,3 L17,3 C19.209139,3 21,4.790861 21,7 C21,9.209139 19.209139,11 17,11 L7,11 C4.790861,11 3,9.209139 3,7 C3,4.790861 4.790861,3 7,3 Z M7,9 C8.1045695,9 9,8.1045695 9,7 C9,5.8954305 8.1045695,5 7,5 C5.8954305,5 5,5.8954305 5,7 C5,8.1045695 5.8954305,9 7,9 Z"
                                fill="#000000"
                              />
                              <path
                                d="M7,13 L17,13 C19.209139,13 21,14.790861 21,17 C21,19.209139 19.209139,21 17,21 L7,21 C4.790861,21 3,19.209139 3,17 C3,14.790861 4.790861,13 7,13 Z M17,19 C18.1045695,19 19,18.1045695 19,17 C19,15.8954305 18.1045695,15 17,15 C15.8954305,15 15,15.8954305 15,17 C15,18.1045695 15.8954305,19 17,19 Z"
                                fill="#000000"
                                opacity="0.3"
                              />
                            </g>
                          </svg>
                          <!--end::Svg Icon-->
                        </span>
                      </a>
                      <a href="#" class="btn btn-icon btn-light btn-hover-primary btn-sm mx-3">
                        <span class="svg-icon svg-icon-md svg-icon-primary">
                          <!--begin::Svg Icon | path:assets/media/svg/icons/Communication/Write.svg-->
                          <svg
                            xmlns="http://www.w3.org/2000/svg"
                            xmlns:xlink="http://www.w3.org/1999/xlink"
                            width="24px"
                            height="24px"
                            viewBox="0 0 24 24"
                            version="1.1"
                          >
                            <g stroke="none" stroke-width="1" fill="none" fill-rule="evenodd">
                              <rect x="0" y="0" width="24" height="24" />
                              <path
                                d="M12.2674799,18.2323597 L12.0084872,5.45852451 C12.0004303,5.06114792 12.1504154,4.6768183 12.4255037,4.38993949 L15.0030167,1.70195304 L17.5910752,4.40093695 C17.8599071,4.6812911 18.0095067,5.05499603 18.0083938,5.44341307 L17.9718262,18.2062508 C17.9694575,19.0329966 17.2985816,19.701953 16.4718324,19.701953 L13.7671717,19.701953 C12.9505952,19.701953 12.2840328,19.0487684 12.2674799,18.2323597 Z"
                                fill="#000000"
                                fill-rule="nonzero"
                                transform="translate(14.701953, 10.701953) rotate(-135.000000) translate(-14.701953, -10.701953)"
                              />
                              <path
                                d="M12.9,2 C13.4522847,2 13.9,2.44771525 13.9,3 C13.9,3.55228475 13.4522847,4 12.9,4 L6,4 C4.8954305,4 4,4.8954305 4,6 L4,18 C4,19.1045695 4.8954305,20 6,20 L18,20 C19.1045695,20 20,19.1045695 20,18 L20,13 C20,12.4477153 20.4477153,12 21,12 C21.5522847,12 22,12.4477153 22,13 L22,18 C22,20.209139 20.209139,22 18,22 L6,22 C3.790861,22 2,20.209139 2,18 L2,6 C2,3.790861 3.790861,2 6,2 L12.9,2 Z"
                                fill="#000000"
                                fill-rule="nonzero"
                                opacity="0.3"
                              />
                            </g>
                          </svg>
                          <!--end::Svg Icon-->
                        </span>
                      </a>
                      <a href="#" class="btn btn-icon btn-light btn-hover-primary btn-sm">
                        <span class="svg-icon svg-icon-md svg-icon-primary">
                          <!--begin::Svg Icon | path:assets/media/svg/icons/General/Trash.svg-->
                          <svg
                            xmlns="http://www.w3.org/2000/svg"
                            xmlns:xlink="http://www.w3.org/1999/xlink"
                            width="24px"
                            height="24px"
                            viewBox="0 0 24 24"
                            version="1.1"
                          >
                            <g stroke="none" stroke-width="1" fill="none" fill-rule="evenodd">
                              <rect x="0" y="0" width="24" height="24" />
                              <path
                                d="M6,8 L6,20.5 C6,21.3284271 6.67157288,22 7.5,22 L16.5,22 C17.3284271,22 18,21.3284271 18,20.5 L18,8 L6,8 Z"
                                fill="#000000"
                                fill-rule="nonzero"
                              />
                              <path
                                d="M14,4.5 L14,4 C14,3.44771525 13.5522847,3 13,3 L11,3 C10.4477153,3 10,3.44771525 10,4 L10,4.5 L5.5,4.5 C5.22385763,4.5 5,4.72385763 5,5 L5,5.5 C5,5.77614237 5.22385763,6 5.5,6 L18.5,6 C18.7761424,6 19,5.77614237 19,5.5 L19,5 C19,4.72385763 18.7761424,4.5 18.5,4.5 L14,4.5 Z"
                                fill="#000000"
                                opacity="0.3"
                              />
                            </g>
                          </svg>
                          <!--end::Svg Icon-->
                        </span>
                      </a>
                    </td>
                  </tr>
                  <tr>
                    <td class="pl-0">
                      <label class="checkbox checkbox-lg checkbox-single">
                        <input type="checkbox" value="1" />
                        <span></span>
                      </label>
                    </td>
                    <td class="pr-0">
                      <div class="symbol symbol-50 symbol-light mt-1">
                        <span class="symbol-label">
                          <img
                            src="assets/media/svg/avatars/018-girl-9.svg"
                            class="h-75 align-self-end"
                            alt
                          />
                        </span>
                      </div>
                    </td>
                    <td class="pl-0">
                      <a
                        href="#"
                        class="text-dark-75 font-weight-bolder text-hover-primary mb-1 font-size-lg"
                      >Jessie Clarcson</a>
                      <span
                        class="text-muted font-weight-bold text-muted d-block"
                      >C#, ASP.NET, MS SQL</span>
                    </td>
                    <td>
                      <span class="text-dark-75 font-weight-bolder d-block font-size-lg">Agoda</span>
                      <span class="text-muted font-weight-bold">Houses &amp; Hotels</span>
                    </td>
                    <td>
                      <div class="d-flex flex-column w-100 mr-2">
                        <div class="d-flex align-items-center justify-content-between mb-2">
                          <span class="text-muted mr-2 font-size-sm font-weight-bold">83%</span>
                          <span class="text-muted font-size-sm font-weight-bold">Progress</span>
                        </div>
                        <div class="progress progress-xs w-100">
                          <div
                            class="progress-bar bg-success"
                            role="progressbar"
                            style="width: 83%;"
                            aria-valuenow="50"
                            aria-valuemin="0"
                            aria-valuemax="100"
                          ></div>
                        </div>
                      </div>
                    </td>
                    <td class="pr-0 text-right">
                      <a href="#" class="btn btn-icon btn-light btn-hover-primary btn-sm">
                        <span class="svg-icon svg-icon-md svg-icon-primary">
                          <!--begin::Svg Icon | path:assets/media/svg/icons/General/Settings-1.svg-->
                          <svg
                            xmlns="http://www.w3.org/2000/svg"
                            xmlns:xlink="http://www.w3.org/1999/xlink"
                            width="24px"
                            height="24px"
                            viewBox="0 0 24 24"
                            version="1.1"
                          >
                            <g stroke="none" stroke-width="1" fill="none" fill-rule="evenodd">
                              <rect x="0" y="0" width="24" height="24" />
                              <path
                                d="M7,3 L17,3 C19.209139,3 21,4.790861 21,7 C21,9.209139 19.209139,11 17,11 L7,11 C4.790861,11 3,9.209139 3,7 C3,4.790861 4.790861,3 7,3 Z M7,9 C8.1045695,9 9,8.1045695 9,7 C9,5.8954305 8.1045695,5 7,5 C5.8954305,5 5,5.8954305 5,7 C5,8.1045695 5.8954305,9 7,9 Z"
                                fill="#000000"
                              />
                              <path
                                d="M7,13 L17,13 C19.209139,13 21,14.790861 21,17 C21,19.209139 19.209139,21 17,21 L7,21 C4.790861,21 3,19.209139 3,17 C3,14.790861 4.790861,13 7,13 Z M17,19 C18.1045695,19 19,18.1045695 19,17 C19,15.8954305 18.1045695,15 17,15 C15.8954305,15 15,15.8954305 15,17 C15,18.1045695 15.8954305,19 17,19 Z"
                                fill="#000000"
                                opacity="0.3"
                              />
                            </g>
                          </svg>
                          <!--end::Svg Icon-->
                        </span>
                      </a>
                      <a href="#" class="btn btn-icon btn-light btn-hover-primary btn-sm mx-3">
                        <span class="svg-icon svg-icon-md svg-icon-primary">
                          <!--begin::Svg Icon | path:assets/media/svg/icons/Communication/Write.svg-->
                          <svg
                            xmlns="http://www.w3.org/2000/svg"
                            xmlns:xlink="http://www.w3.org/1999/xlink"
                            width="24px"
                            height="24px"
                            viewBox="0 0 24 24"
                            version="1.1"
                          >
                            <g stroke="none" stroke-width="1" fill="none" fill-rule="evenodd">
                              <rect x="0" y="0" width="24" height="24" />
                              <path
                                d="M12.2674799,18.2323597 L12.0084872,5.45852451 C12.0004303,5.06114792 12.1504154,4.6768183 12.4255037,4.38993949 L15.0030167,1.70195304 L17.5910752,4.40093695 C17.8599071,4.6812911 18.0095067,5.05499603 18.0083938,5.44341307 L17.9718262,18.2062508 C17.9694575,19.0329966 17.2985816,19.701953 16.4718324,19.701953 L13.7671717,19.701953 C12.9505952,19.701953 12.2840328,19.0487684 12.2674799,18.2323597 Z"
                                fill="#000000"
                                fill-rule="nonzero"
                                transform="translate(14.701953, 10.701953) rotate(-135.000000) translate(-14.701953, -10.701953)"
                              />
                              <path
                                d="M12.9,2 C13.4522847,2 13.9,2.44771525 13.9,3 C13.9,3.55228475 13.4522847,4 12.9,4 L6,4 C4.8954305,4 4,4.8954305 4,6 L4,18 C4,19.1045695 4.8954305,20 6,20 L18,20 C19.1045695,20 20,19.1045695 20,18 L20,13 C20,12.4477153 20.4477153,12 21,12 C21.5522847,12 22,12.4477153 22,13 L22,18 C22,20.209139 20.209139,22 18,22 L6,22 C3.790861,22 2,20.209139 2,18 L2,6 C2,3.790861 3.790861,2 6,2 L12.9,2 Z"
                                fill="#000000"
                                fill-rule="nonzero"
                                opacity="0.3"
                              />
                            </g>
                          </svg>
                          <!--end::Svg Icon-->
                        </span>
                      </a>
                      <a href="#" class="btn btn-icon btn-light btn-hover-primary btn-sm">
                        <span class="svg-icon svg-icon-md svg-icon-primary">
                          <!--begin::Svg Icon | path:assets/media/svg/icons/General/Trash.svg-->
                          <svg
                            xmlns="http://www.w3.org/2000/svg"
                            xmlns:xlink="http://www.w3.org/1999/xlink"
                            width="24px"
                            height="24px"
                            viewBox="0 0 24 24"
                            version="1.1"
                          >
                            <g stroke="none" stroke-width="1" fill="none" fill-rule="evenodd">
                              <rect x="0" y="0" width="24" height="24" />
                              <path
                                d="M6,8 L6,20.5 C6,21.3284271 6.67157288,22 7.5,22 L16.5,22 C17.3284271,22 18,21.3284271 18,20.5 L18,8 L6,8 Z"
                                fill="#000000"
                                fill-rule="nonzero"
                              />
                              <path
                                d="M14,4.5 L14,4 C14,3.44771525 13.5522847,3 13,3 L11,3 C10.4477153,3 10,3.44771525 10,4 L10,4.5 L5.5,4.5 C5.22385763,4.5 5,4.72385763 5,5 L5,5.5 C5,5.77614237 5.22385763,6 5.5,6 L18.5,6 C18.7761424,6 19,5.77614237 19,5.5 L19,5 C19,4.72385763 18.7761424,4.5 18.5,4.5 L14,4.5 Z"
                                fill="#000000"
                                opacity="0.3"
                              />
                            </g>
                          </svg>
                          <!--end::Svg Icon-->
                        </span>
                      </a>
                    </td>
                  </tr>
                  <tr>
                    <td class="pl-0">
                      <label class="checkbox checkbox-lg checkbox-single">
                        <input type="checkbox" value="1" />
                        <span></span>
                      </label>
                    </td>
                    <td class="pr-0">
                      <div class="symbol symbol-50 symbol-lightv mt-1">
                        <span class="symbol-label">
                          <img
                            src="assets/media/svg/avatars/047-girl-25.svg"
                            class="h-75 align-self-end"
                            alt
                          />
                        </span>
                      </div>
                    </td>
                    <td class="pl-0">
                      <a
                        href="#"
                        class="text-dark-75 font-weight-bolder text-hover-primary mb-1 font-size-lg"
                      >Lebron Wayde</a>
                      <span
                        class="text-muted font-weight-bold text-muted d-block"
                      >PHP, Laravel, VueJS</span>
                    </td>
                    <td>
                      <span class="text-dark-75 font-weight-bolder d-block font-size-lg">RoadGee</span>
                      <span class="text-muted font-weight-bold">Transportation</span>
                    </td>
                    <td>
                      <div class="d-flex flex-column w-100 mr-2">
                        <div class="d-flex align-items-center justify-content-between mb-2">
                          <span class="text-muted mr-2 font-size-sm font-weight-bold">47%</span>
                          <span class="text-muted font-size-sm font-weight-bold">Progress</span>
                        </div>
                        <div class="progress progress-xs w-100">
                          <div
                            class="progress-bar bg-primary"
                            role="progressbar"
                            style="width: 83%;"
                            aria-valuenow="50"
                            aria-valuemin="0"
                            aria-valuemax="100"
                          ></div>
                        </div>
                      </div>
                    </td>
                    <td class="pr-0 text-right">
                      <a href="#" class="btn btn-icon btn-light btn-hover-primary btn-sm">
                        <span class="svg-icon svg-icon-md svg-icon-primary">
                          <!--begin::Svg Icon | path:assets/media/svg/icons/General/Settings-1.svg-->
                          <svg
                            xmlns="http://www.w3.org/2000/svg"
                            xmlns:xlink="http://www.w3.org/1999/xlink"
                            width="24px"
                            height="24px"
                            viewBox="0 0 24 24"
                            version="1.1"
                          >
                            <g stroke="none" stroke-width="1" fill="none" fill-rule="evenodd">
                              <rect x="0" y="0" width="24" height="24" />
                              <path
                                d="M7,3 L17,3 C19.209139,3 21,4.790861 21,7 C21,9.209139 19.209139,11 17,11 L7,11 C4.790861,11 3,9.209139 3,7 C3,4.790861 4.790861,3 7,3 Z M7,9 C8.1045695,9 9,8.1045695 9,7 C9,5.8954305 8.1045695,5 7,5 C5.8954305,5 5,5.8954305 5,7 C5,8.1045695 5.8954305,9 7,9 Z"
                                fill="#000000"
                              />
                              <path
                                d="M7,13 L17,13 C19.209139,13 21,14.790861 21,17 C21,19.209139 19.209139,21 17,21 L7,21 C4.790861,21 3,19.209139 3,17 C3,14.790861 4.790861,13 7,13 Z M17,19 C18.1045695,19 19,18.1045695 19,17 C19,15.8954305 18.1045695,15 17,15 C15.8954305,15 15,15.8954305 15,17 C15,18.1045695 15.8954305,19 17,19 Z"
                                fill="#000000"
                                opacity="0.3"
                              />
                            </g>
                          </svg>
                          <!--end::Svg Icon-->
                        </span>
                      </a>
                      <a href="#" class="btn btn-icon btn-light btn-hover-primary btn-sm mx-3">
                        <span class="svg-icon svg-icon-md svg-icon-primary">
                          <!--begin::Svg Icon | path:assets/media/svg/icons/Communication/Write.svg-->
                          <svg
                            xmlns="http://www.w3.org/2000/svg"
                            xmlns:xlink="http://www.w3.org/1999/xlink"
                            width="24px"
                            height="24px"
                            viewBox="0 0 24 24"
                            version="1.1"
                          >
                            <g stroke="none" stroke-width="1" fill="none" fill-rule="evenodd">
                              <rect x="0" y="0" width="24" height="24" />
                              <path
                                d="M12.2674799,18.2323597 L12.0084872,5.45852451 C12.0004303,5.06114792 12.1504154,4.6768183 12.4255037,4.38993949 L15.0030167,1.70195304 L17.5910752,4.40093695 C17.8599071,4.6812911 18.0095067,5.05499603 18.0083938,5.44341307 L17.9718262,18.2062508 C17.9694575,19.0329966 17.2985816,19.701953 16.4718324,19.701953 L13.7671717,19.701953 C12.9505952,19.701953 12.2840328,19.0487684 12.2674799,18.2323597 Z"
                                fill="#000000"
                                fill-rule="nonzero"
                                transform="translate(14.701953, 10.701953) rotate(-135.000000) translate(-14.701953, -10.701953)"
                              />
                              <path
                                d="M12.9,2 C13.4522847,2 13.9,2.44771525 13.9,3 C13.9,3.55228475 13.4522847,4 12.9,4 L6,4 C4.8954305,4 4,4.8954305 4,6 L4,18 C4,19.1045695 4.8954305,20 6,20 L18,20 C19.1045695,20 20,19.1045695 20,18 L20,13 C20,12.4477153 20.4477153,12 21,12 C21.5522847,12 22,12.4477153 22,13 L22,18 C22,20.209139 20.209139,22 18,22 L6,22 C3.790861,22 2,20.209139 2,18 L2,6 C2,3.790861 3.790861,2 6,2 L12.9,2 Z"
                                fill="#000000"
                                fill-rule="nonzero"
                                opacity="0.3"
                              />
                            </g>
                          </svg>
                          <!--end::Svg Icon-->
                        </span>
                      </a>
                      <a href="#" class="btn btn-icon btn-light btn-hover-primary btn-sm">
                        <span class="svg-icon svg-icon-md svg-icon-primary">
                          <!--begin::Svg Icon | path:assets/media/svg/icons/General/Trash.svg-->
                          <svg
                            xmlns="http://www.w3.org/2000/svg"
                            xmlns:xlink="http://www.w3.org/1999/xlink"
                            width="24px"
                            height="24px"
                            viewBox="0 0 24 24"
                            version="1.1"
                          >
                            <g stroke="none" stroke-width="1" fill="none" fill-rule="evenodd">
                              <rect x="0" y="0" width="24" height="24" />
                              <path
                                d="M6,8 L6,20.5 C6,21.3284271 6.67157288,22 7.5,22 L16.5,22 C17.3284271,22 18,21.3284271 18,20.5 L18,8 L6,8 Z"
                                fill="#000000"
                                fill-rule="nonzero"
                              />
                              <path
                                d="M14,4.5 L14,4 C14,3.44771525 13.5522847,3 13,3 L11,3 C10.4477153,3 10,3.44771525 10,4 L10,4.5 L5.5,4.5 C5.22385763,4.5 5,4.72385763 5,5 L5,5.5 C5,5.77614237 5.22385763,6 5.5,6 L18.5,6 C18.7761424,6 19,5.77614237 19,5.5 L19,5 C19,4.72385763 18.7761424,4.5 18.5,4.5 L14,4.5 Z"
                                fill="#000000"
                                opacity="0.3"
                              />
                            </g>
                          </svg>
                          <!--end::Svg Icon-->
                        </span>
                      </a>
                    </td>
                  </tr>
                  <tr>
                    <td class="pl-0">
                      <label class="checkbox checkbox-lg checkbox-single">
                        <input type="checkbox" value="1" />
                        <span></span>
                      </label>
                    </td>
                    <td class="pr-0">
                      <div class="symbol symbol-50 symbol-light mt-1">
                        <span class="symbol-label">
                          <img
                            src="assets/media/svg/avatars/014-girl-7.svg"
                            class="h-75 align-self-end"
                            alt
                          />
                        </span>
                      </div>
                    </td>
                    <td class="pl-0">
                      <a
                        href="#"
                        class="text-dark-75 font-weight-bolder text-hover-primary mb-1 font-size-lg"
                      >Natali Trump</a>
                      <span
                        class="text-muted font-weight-bold text-muted d-block"
                      >Python, PostgreSQL, ReactJS</span>
                    </td>
                    <td>
                      <span class="text-dark-75 font-weight-bolder d-block font-size-lg">The Hill</span>
                      <span class="text-muted font-weight-bold">Insurance</span>
                    </td>
                    <td>
                      <div class="d-flex flex-column w-100 mr-2">
                        <div class="d-flex align-items-center justify-content-between mb-2">
                          <span class="text-muted mr-2 font-size-sm font-weight-bold">71%</span>
                          <span class="text-muted font-size-sm font-weight-bold">Progress</span>
                        </div>
                        <div class="progress progress-xs w-100">
                          <div
                            class="progress-bar bg-danger"
                            role="progressbar"
                            style="width: 71%;"
                            aria-valuenow="50"
                            aria-valuemin="0"
                            aria-valuemax="100"
                          ></div>
                        </div>
                      </div>
                    </td>
                    <td class="pr-0 text-right">
                      <a href="#" class="btn btn-icon btn-light btn-hover-primary btn-sm">
                        <span class="svg-icon svg-icon-md svg-icon-primary">
                          <!--begin::Svg Icon | path:assets/media/svg/icons/General/Settings-1.svg-->
                          <svg
                            xmlns="http://www.w3.org/2000/svg"
                            xmlns:xlink="http://www.w3.org/1999/xlink"
                            width="24px"
                            height="24px"
                            viewBox="0 0 24 24"
                            version="1.1"
                          >
                            <g stroke="none" stroke-width="1" fill="none" fill-rule="evenodd">
                              <rect x="0" y="0" width="24" height="24" />
                              <path
                                d="M7,3 L17,3 C19.209139,3 21,4.790861 21,7 C21,9.209139 19.209139,11 17,11 L7,11 C4.790861,11 3,9.209139 3,7 C3,4.790861 4.790861,3 7,3 Z M7,9 C8.1045695,9 9,8.1045695 9,7 C9,5.8954305 8.1045695,5 7,5 C5.8954305,5 5,5.8954305 5,7 C5,8.1045695 5.8954305,9 7,9 Z"
                                fill="#000000"
                              />
                              <path
                                d="M7,13 L17,13 C19.209139,13 21,14.790861 21,17 C21,19.209139 19.209139,21 17,21 L7,21 C4.790861,21 3,19.209139 3,17 C3,14.790861 4.790861,13 7,13 Z M17,19 C18.1045695,19 19,18.1045695 19,17 C19,15.8954305 18.1045695,15 17,15 C15.8954305,15 15,15.8954305 15,17 C15,18.1045695 15.8954305,19 17,19 Z"
                                fill="#000000"
                                opacity="0.3"
                              />
                            </g>
                          </svg>
                          <!--end::Svg Icon-->
                        </span>
                      </a>
                      <a href="#" class="btn btn-icon btn-light btn-hover-primary btn-sm mx-3">
                        <span class="svg-icon svg-icon-md svg-icon-primary">
                          <!--begin::Svg Icon | path:assets/media/svg/icons/Communication/Write.svg-->
                          <svg
                            xmlns="http://www.w3.org/2000/svg"
                            xmlns:xlink="http://www.w3.org/1999/xlink"
                            width="24px"
                            height="24px"
                            viewBox="0 0 24 24"
                            version="1.1"
                          >
                            <g stroke="none" stroke-width="1" fill="none" fill-rule="evenodd">
                              <rect x="0" y="0" width="24" height="24" />
                              <path
                                d="M12.2674799,18.2323597 L12.0084872,5.45852451 C12.0004303,5.06114792 12.1504154,4.6768183 12.4255037,4.38993949 L15.0030167,1.70195304 L17.5910752,4.40093695 C17.8599071,4.6812911 18.0095067,5.05499603 18.0083938,5.44341307 L17.9718262,18.2062508 C17.9694575,19.0329966 17.2985816,19.701953 16.4718324,19.701953 L13.7671717,19.701953 C12.9505952,19.701953 12.2840328,19.0487684 12.2674799,18.2323597 Z"
                                fill="#000000"
                                fill-rule="nonzero"
                                transform="translate(14.701953, 10.701953) rotate(-135.000000) translate(-14.701953, -10.701953)"
                              />
                              <path
                                d="M12.9,2 C13.4522847,2 13.9,2.44771525 13.9,3 C13.9,3.55228475 13.4522847,4 12.9,4 L6,4 C4.8954305,4 4,4.8954305 4,6 L4,18 C4,19.1045695 4.8954305,20 6,20 L18,20 C19.1045695,20 20,19.1045695 20,18 L20,13 C20,12.4477153 20.4477153,12 21,12 C21.5522847,12 22,12.4477153 22,13 L22,18 C22,20.209139 20.209139,22 18,22 L6,22 C3.790861,22 2,20.209139 2,18 L2,6 C2,3.790861 3.790861,2 6,2 L12.9,2 Z"
                                fill="#000000"
                                fill-rule="nonzero"
                                opacity="0.3"
                              />
                            </g>
                          </svg>
                          <!--end::Svg Icon-->
                        </span>
                      </a>
                      <a href="#" class="btn btn-icon btn-light btn-hover-primary btn-sm">
                        <span class="svg-icon svg-icon-md svg-icon-primary">
                          <!--begin::Svg Icon | path:assets/media/svg/icons/General/Trash.svg-->
                          <svg
                            xmlns="http://www.w3.org/2000/svg"
                            xmlns:xlink="http://www.w3.org/1999/xlink"
                            width="24px"
                            height="24px"
                            viewBox="0 0 24 24"
                            version="1.1"
                          >
                            <g stroke="none" stroke-width="1" fill="none" fill-rule="evenodd">
                              <rect x="0" y="0" width="24" height="24" />
                              <path
                                d="M6,8 L6,20.5 C6,21.3284271 6.67157288,22 7.5,22 L16.5,22 C17.3284271,22 18,21.3284271 18,20.5 L18,8 L6,8 Z"
                                fill="#000000"
                                fill-rule="nonzero"
                              />
                              <path
                                d="M14,4.5 L14,4 C14,3.44771525 13.5522847,3 13,3 L11,3 C10.4477153,3 10,3.44771525 10,4 L10,4.5 L5.5,4.5 C5.22385763,4.5 5,4.72385763 5,5 L5,5.5 C5,5.77614237 5.22385763,6 5.5,6 L18.5,6 C18.7761424,6 19,5.77614237 19,5.5 L19,5 C19,4.72385763 18.7761424,4.5 18.5,4.5 L14,4.5 Z"
                                fill="#000000"
                                opacity="0.3"
                              />
                            </g>
                          </svg>
                          <!--end::Svg Icon-->
                        </span>
                      </a>
                    </td>
                  </tr>
                </tbody>
              </table>
            </div>
            <!--end::Table-->
          </div>
          <!--end::Body-->
        </div>
        <!--end::Advance Table Widget 1-->
      </div>
    </div>
    <!--end::Row-->
    <!--begin::Row-->
    <div class="row">
      <div class="col-xl-4">
        <!--begin::Mixed Widget 10-->
        <div class="card card-custom card-stretch gutter-b">
          <!--begin::Body-->
          <div class="card-body">
            <!--begin::Info-->
            <div class="d-flex align-items-center pr-2 mb-6">
              <span class="text-muted font-weight-bold font-size-lg flex-grow-1">7 Hours Ago</span>
              <div class="symbol symbol-50">
                <span class="symbol-label bg-light-light">
                  <img src="assets/media/svg/misc/006-plurk.svg" class="h-50 align-self-center" alt />
                </span>
              </div>
            </div>
            <!--end::Info-->
            <a href="#" class="text-dark font-weight-bolder text-hover-primary font-size-h4">
              PitStop - Multiple Email
              <br />Generator
            </a>
            <!--begin::Desc-->
            <p class="text-dark-50 font-weight-normal font-size-lg mt-6">
              Pitstop creates quick and easy email campaigns.
              <br />We help to leverage and strengthen your brand
              <br />for your every purpose.
            </p>
            <!--end::Desc-->
            <!--begin::Team-->
            <div class="d-flex align-items-center mt-25">
              <!--begin::Pic-->
              <a href="#" class="symbol symbol-45 symbol-light mr-3">
                <div class="symbol-label">
                  <img src="assets/media/svg/avatars/001-boy.svg" class="h-75 align-self-end" alt />
                </div>
              </a>
              <!--end::Pic-->
              <!--begin::Pic-->
              <a href="#" class="symbol symbol-45 symbol-light mr-3">
                <div class="symbol-label">
                  <img
                    src="assets/media/svg/avatars/028-girl-16.svg"
                    class="h-75 align-self-end"
                    alt
                  />
                </div>
              </a>
              <!--end::Pic-->
              <!--begin::Pic-->
              <a href="#" class="symbol symbol-45 symbol-light">
                <div class="symbol-label">
                  <img src="assets/media/svg/avatars/024-boy-9.svg" class="h-75 align-self-end" alt />
                </div>
              </a>
              <!--end::Pic-->
            </div>
            <!--end::Team-->
          </div>
          <!--end::Body-->
        </div>
        <!--end::Mixed Widget 10-->
      </div>
      <div class="col-xl-4">
        <!--begin::Mixed Widget 11-->
        <div class="card card-custom card-stretch gutter-b">
          <!--begin::Body-->
          <div class="card-body">
            <!--begin::Info-->
            <div class="d-flex align-items-center pr-2 mb-6">
              <span class="text-muted font-weight-bold font-size-lg flex-grow-1">2 Days Ago</span>
              <div class="symbol symbol-50">
                <span class="symbol-label bg-light-light">
                  <img
                    src="assets/media/svg/misc/015-telegram.svg"
                    class="h-50 align-self-center"
                    alt
                  />
                </span>
              </div>
            </div>
            <!--end::Info-->
            <a href="#" class="text-dark font-weight-bolder text-hover-primary font-size-h4">
              Craft - ReactJS Admin
              <br />Theme
            </a>
            <!--begin::Desc-->
            <p class="text-dark-50 font-weight-normal font-size-lg mt-6">
              Craft uses the latest and greatest frameworks
              <br />with ReactJS for complete modernization and
              <br />future proofing your business operations
              <br />and sales opportunities
            </p>
            <!--end::Desc-->
            <!--begin::Team-->
            <div class="d-flex align-items-center mt-18">
              <!--begin::Pic-->
              <a href="#" class="symbol symbol-45 symbol-light mr-3">
                <div class="symbol-label">
                  <img src="assets/media/svg/avatars/001-boy.svg" class="h-75 align-self-end" alt />
                </div>
              </a>
              <!--end::Pic-->
              <!--begin::Pic-->
              <a href="#" class="symbol symbol-45 symbol-light mr-3">
                <div class="symbol-label">
                  <img
                    src="assets/media/svg/avatars/028-girl-16.svg"
                    class="h-75 align-self-end"
                    alt
                  />
                </div>
              </a>
              <!--end::Pic-->
              <!--begin: Pic-->
              <a href="#" class="symbol symbol-45 symbol-light mr-3">
                <div class="symbol-label">
                  <img src="assets/media/svg/avatars/024-boy-9.svg" class="h-75 align-self-end" alt />
                </div>
              </a>
              <!--end::Pic-->
              <!--begin::Pic-->
              <a href="#" class="symbol symbol-45 symbol-light">
                <div class="symbol-label">
                  <img
                    src="assets/media/svg/avatars/005-girl-2.svg"
                    class="h-75 align-self-end"
                    alt
                  />
                </div>
              </a>
              <!--end::Pic-->
            </div>
            <!--end::Team-->
          </div>
          <!--end::Body-->
        </div>
        <!--end::Mixed Widget 11-->
      </div>
      <div class="col-xl-4">
        <!--begin::Mixed Widget 12-->
        <div class="card card-custom card-stretch gutter-b">
          <!--begin::Body-->
          <div class="card-body">
            <!--begin::Info-->
            <div class="d-flex align-items-center pr-2 mb-6">
              <span class="text-muted font-weight-bold font-size-lg flex-grow-1">5 Weeks Ago</span>
              <div class="symbol symbol-50">
                <span class="symbol-label bg-light-light">
                  <img
                    src="assets/media/svg/misc/003-puzzle.svg"
                    class="h-50 align-self-center"
                    alt
                  />
                </span>
              </div>
            </div>
            <!--end::Info-->
            <a href="#" class="text-dark font-weight-bolder text-hover-primary font-size-h4">
              KT.com - High Quality
              <br />Templates
            </a>
            <!--begin::Desc-->
            <p class="text-dark-50 font-weight-normal font-size-lg mt-6">
              Easy to use, incredibly flexible and secure
              <br />with in-depth documentation that outlines
              <br />everything for you
            </p>
            <!--end::Desc-->
            <!--begin::Team-->
            <div class="d-flex align-items-center mt-25">
              <!--begin::Pic-->
              <a href="#" class="symbol symbol-45 symbol-light mr-3">
                <div class="symbol-label">
                  <img src="assets/media/svg/avatars/001-boy.svg" class="h-75 align-self-end" alt />
                </div>
              </a>
              <!--end::Pic-->
              <!--begin::Pic-->
              <a href="#" class="symbol symbol-45 symbol-light mr-3">
                <div class="symbol-label">
                  <img
                    src="assets/media/svg/avatars/028-girl-16.svg"
                    class="h-75 align-self-end"
                    alt
                  />
                </div>
              </a>
              <!--end::Pic-->
              <!--begin::Pic-->
              <a href="#" class="symbol symbol-45 symbol-light">
                <div class="symbol-label">
                  <img src="assets/media/svg/avatars/024-boy-9.svg" class="h-75 align-self-end" alt />
                </div>
              </a>
              <!--end::Pic-->
            </div>
            <!--end::Team-->
          </div>
          <!--end::Body-->
        </div>
        <!--end::Mixed Widget 12-->
      </div>
    </div>
    <!--end::Row-->
    <!--begin::Row-->
    <div class="row">
      <div class="col-lg-6">
        <!--begin::List Widget 10-->
        <div class="card card-custom card-stretch gutter-b">
          <!--begin::Header-->
          <div class="card-header border-0">
            <h3 class="card-title font-weight-bolder text-dark">Notifications</h3>
            <div class="card-toolbar">
              <div class="dropdown dropdown-inline">
                <a
                  href="#"
                  class="btn btn-clean btn-hover-light-primary btn-sm btn-icon"
                  data-toggle="dropdown"
                  aria-haspopup="true"
                  aria-expanded="false"
                >
                  <i class="ki ki-bold-more-ver"></i>
                </a>
                <div class="dropdown-menu dropdown-menu-md dropdown-menu-right">
                  <!--begin::Naviigation-->
                  <ul class="navi">
                    <li class="navi-header font-weight-bold py-5">
                      <span class="font-size-lg">Add New:</span>
                      <i
                        class="flaticon2-information icon-md text-muted"
                        data-toggle="tooltip"
                        data-placement="right"
                        title="Click to learn more..."
                      ></i>
                    </li>
                    <li class="navi-separator mb-3 opacity-70"></li>
                    <li class="navi-item">
                      <a href="#" class="navi-link">
                        <span class="navi-icon">
                          <i class="flaticon2-shopping-cart-1"></i>
                        </span>
                        <span class="navi-text">Order</span>
                      </a>
                    </li>
                    <li class="navi-item">
                      <a href="#" class="navi-link">
                        <span class="navi-icon">
                          <i class="navi-icon flaticon2-calendar-8"></i>
                        </span>
                        <span class="navi-text">Members</span>
                        <span class="navi-label">
                          <span class="label label-light-danger label-rounded font-weight-bold">3</span>
                        </span>
                      </a>
                    </li>
                    <li class="navi-item">
                      <a href="#" class="navi-link">
                        <span class="navi-icon">
                          <i class="navi-icon flaticon2-telegram-logo"></i>
                        </span>
                        <span class="navi-text">Project</span>
                      </a>
                    </li>
                    <li class="navi-item">
                      <a href="#" class="navi-link">
                        <span class="navi-icon">
                          <i class="navi-icon flaticon2-new-email"></i>
                        </span>
                        <span class="navi-text">Record</span>
                        <span class="navi-label">
                          <span class="label label-light-success label-rounded font-weight-bold">5</span>
                        </span>
                      </a>
                    </li>
                    <li class="navi-separator mt-3 opacity-70"></li>
                    <li class="navi-footer pt-5 pb-4">
                      <a
                        class="btn btn-light-primary font-weight-bolder btn-sm"
                        href="#"
                      >More options</a>
                      <a
                        class="btn btn-clean font-weight-bold btn-sm d-none"
                        href="#"
                        data-toggle="tooltip"
                        data-placement="right"
                        title="Click to learn more..."
                      >Learn more</a>
                    </li>
                  </ul>
                  <!--end::Naviigation-->
                </div>
              </div>
            </div>
          </div>
          <!--end::Header-->
          <!--begin::Body-->
          <div class="card-body pt-0">
            <!--begin::Item-->
            <div class="mb-6">
              <!--begin::Content-->
              <div class="d-flex align-items-center flex-grow-1">
                <!--begin::Checkbox-->
                <label class="checkbox checkbox-lg checkbox-lg checkbox-single flex-shrink-0 mr-4">
                  <input type="checkbox" value="1" />
                  <span></span>
                </label>
                <!--end::Checkbox-->
                <!--begin::Section-->
                <div class="d-flex flex-wrap align-items-center justify-content-between w-100">
                  <!--begin::Info-->
                  <div class="d-flex flex-column align-items-cente py-2 w-75">
                    <!--begin::Title-->
                    <a
                      href="#"
                      class="text-dark-75 font-weight-bold text-hover-primary font-size-lg mb-1"
                    >Daily Standup Meeting</a>
                    <!--end::Title-->
                    <!--begin::Data-->
                    <span class="text-muted font-weight-bold">Due in 2 Days</span>
                    <!--end::Data-->
                  </div>
                  <!--end::Info-->
                  <!--begin::Label-->
                  <span
                    class="label label-lg label-light-primary label-inline font-weight-bold py-4"
                  >Approved</span>
                  <!--end::Label-->
                </div>
                <!--end::Section-->
              </div>
              <!--end::Content-->
            </div>
            <!--end::Item-->
            <!--begin::Item-->
            <div class="mb-6">
              <!--begin::Content-->
              <div class="d-flex align-items-center flex-grow-1">
                <!--begin::Checkbox-->
                <label class="checkbox checkbox-lg checkbox-lg checkbox-single flex-shrink-0 mr-4">
                  <input type="checkbox" value="1" />
                  <span></span>
                </label>
                <!--end::Checkbox-->
                <!--begin::Section-->
                <div class="d-flex flex-wrap align-items-center justify-content-between w-100">
                  <!--begin::Info-->
                  <div class="d-flex flex-column align-items-cente py-2 w-75">
                    <!--begin::Title-->
                    <a
                      href="#"
                      class="text-dark-75 font-weight-bold text-hover-primary font-size-lg mb-1"
                    >Group Town Hall Meet-up with showcase</a>
                    <!--end::Title-->
                    <!--begin::Data-->
                    <span class="text-muted font-weight-bold">Due in 2 Days</span>
                    <!--end::Data-->
                  </div>
                  <!--end::Info-->
                  <!--begin::Label-->
                  <span
                    class="label label-lg label-light-warning label-inline font-weight-bold py-4"
                  >In Progress</span>
                  <!--end::Label-->
                </div>
                <!--end::Section-->
              </div>
              <!--end::Content-->
            </div>
            <!--end::Item-->
            <!--begin::Item-->
            <div class="mb-6">
              <!--begin::Content-->
              <div class="d-flex align-items-center flex-grow-1">
                <!--begin::Checkbox-->
                <label class="checkbox checkbox-lg checkbox-lg checkbox-single flex-shrink-0 mr-4">
                  <input type="checkbox" value="1" />
                  <span></span>
                </label>
                <!--end::Checkbox-->
                <!--begin::Section-->
                <div class="d-flex flex-wrap align-items-center justify-content-between w-100">
                  <!--begin::Info-->
                  <div class="d-flex flex-column align-items-cente py-2 w-75">
                    <!--begin::Title-->
                    <a
                      href="#"
                      class="text-dark-75 font-weight-bold text-hover-primary font-size-lg mb-1"
                    >Next sprint planning and estimations</a>
                    <!--end::Title-->
                    <!--begin::Data-->
                    <span class="text-muted font-weight-bold">Due in 2 Days</span>
                    <!--end::Data-->
                  </div>
                  <!--end::Info-->
                  <!--begin::Label-->
                  <span
                    class="label label-lg label-light-success label-inline font-weight-bold py-4"
                  >Success</span>
                  <!--end::Label-->
                </div>
                <!--end::Section-->
              </div>
              <!--end::Content-->
            </div>
            <!--end::Item-->
            <!--begin::Item-->
            <div class="mb-6">
              <!--begin::Content-->
              <div class="d-flex align-items-center flex-grow-1">
                <!--begin::Checkbox-->
                <label class="checkbox checkbox-lg checkbox-lg checkbox-single flex-shrink-0 mr-4">
                  <input type="checkbox" value="1" />
                  <span></span>
                </label>
                <!--end::Checkbox-->
                <!--begin::Section-->
                <div class="d-flex flex-wrap align-items-center justify-content-between w-100">
                  <!--begin::Info-->
                  <div class="d-flex flex-column align-items-cente py-2 w-75">
                    <!--begin::Title-->
                    <a
                      href="#"
                      class="text-dark-75 font-weight-bold text-hover-primary font-size-lg mb-1"
                    >Sprint delivery and project deployment</a>
                    <!--end::Title-->
                    <!--begin::Data-->
                    <span class="text-muted font-weight-bold">Due in 2 Days</span>
                    <!--end::Data-->
                  </div>
                  <!--end::Info-->
                  <!--begin::Label-->
                  <span
                    class="label label-lg label-light-danger label-inline font-weight-bold py-4"
                  >Rejected</span>
                  <!--end::Label-->
                </div>
                <!--end::Section-->
              </div>
              <!--end::Content-->
            </div>
            <!--end: Item-->
            <!--begin: Item-->
            <div class>
              <!--begin::Content-->
              <div class="d-flex align-items-center flex-grow-1">
                <!--begin::Checkbox-->
                <label class="checkbox checkbox-lg checkbox-lg checkbox-single flex-shrink-0 mr-4">
                  <input type="checkbox" value="1" />
                  <span></span>
                </label>
                <!--end::Checkbox-->
                <!--begin::Section-->
                <div class="d-flex flex-wrap align-items-center justify-content-between w-100">
                  <!--begin::Info-->
                  <div class="d-flex flex-column align-items-cente py-2 w-75">
                    <!--begin::Title-->
                    <a
                      href="#"
                      class="text-dark-75 font-weight-bold text-hover-primary font-size-lg mb-1"
                    >Data analytics research showcase</a>
                    <!--end::Title-->
                    <!--begin::Data-->
                    <span class="text-muted font-weight-bold">Due in 2 Days</span>
                    <!--end::Data-->
                  </div>
                  <!--end::Info-->
                  <!--begin::Label-->
                  <span
                    class="label label-lg label-light-warning label-inline font-weight-bold py-4"
                  >In Progress</span>
                  <!--end::Label-->
                </div>
                <!--end::Section-->
              </div>
              <!--end::Content-->
            </div>
            <!--end: Item-->
          </div>
          <!--end: Card Body-->
        </div>
        <!--end: Card-->
        <!--end: List Widget 10-->
      </div>
      <div class="col-lg-6">
        <!--begin::List Widget 11-->
        <div class="card card-custom card-stretch gutter-b">
          <!--begin::Header-->
          <div class="card-header border-0">
            <h3 class="card-title font-weight-bolder text-dark">Trends</h3>
            <div class="card-toolbar">
              <div
                class="dropdown dropdown-inline"
                data-toggle="tooltip"
                title="Quick actions"
                data-placement="left"
              >
                <a
                  href="#"
                  class="btn btn-clean btn-hover-light-primary btn-sm btn-icon"
                  data-toggle="dropdown"
                  aria-haspopup="true"
                  aria-expanded="false"
                >
                  <i class="ki ki-bold-more-ver"></i>
                </a>
                <div class="dropdown-menu dropdown-menu-md dropdown-menu-right">
                  <!--begin::Navigation-->
                  <ul class="navi navi-hover py-5">
                    <li class="navi-item">
                      <a href="#" class="navi-link">
                        <span class="navi-icon">
                          <i class="flaticon2-drop"></i>
                        </span>
                        <span class="navi-text">New Group</span>
                      </a>
                    </li>
                    <li class="navi-item">
                      <a href="#" class="navi-link">
                        <span class="navi-icon">
                          <i class="flaticon2-list-3"></i>
                        </span>
                        <span class="navi-text">Contacts</span>
                      </a>
                    </li>
                    <li class="navi-item">
                      <a href="#" class="navi-link">
                        <span class="navi-icon">
                          <i class="flaticon2-rocket-1"></i>
                        </span>
                        <span class="navi-text">Groups</span>
                        <span class="navi-link-badge">
                          <span class="label label-light-primary label-inline font-weight-bold">new</span>
                        </span>
                      </a>
                    </li>
                    <li class="navi-item">
                      <a href="#" class="navi-link">
                        <span class="navi-icon">
                          <i class="flaticon2-bell-2"></i>
                        </span>
                        <span class="navi-text">Calls</span>
                      </a>
                    </li>
                    <li class="navi-item">
                      <a href="#" class="navi-link">
                        <span class="navi-icon">
                          <i class="flaticon2-gear"></i>
                        </span>
                        <span class="navi-text">Settings</span>
                      </a>
                    </li>
                    <li class="navi-separator my-3"></li>
                    <li class="navi-item">
                      <a href="#" class="navi-link">
                        <span class="navi-icon">
                          <i class="flaticon2-magnifier-tool"></i>
                        </span>
                        <span class="navi-text">Help</span>
                      </a>
                    </li>
                    <li class="navi-item">
                      <a href="#" class="navi-link">
                        <span class="navi-icon">
                          <i class="flaticon2-bell-2"></i>
                        </span>
                        <span class="navi-text">Privacy</span>
                        <span class="navi-link-badge">
                          <span class="label label-light-danger label-rounded font-weight-bold">5</span>
                        </span>
                      </a>
                    </li>
                  </ul>
                  <!--end::Navigation-->
                </div>
              </div>
            </div>
          </div>
          <!--end::Header-->
          <!--begin::Body-->
          <div class="card-body pt-0">
            <!--begin::Item-->
            <div class="d-flex align-items-center mb-9 bg-light-warning rounded p-5">
              <!--begin::Icon-->
              <span class="svg-icon svg-icon-warning mr-5">
                <span class="svg-icon svg-icon-lg">
                  <!--begin::Svg Icon | path:assets/media/svg/icons/Home/Library.svg-->
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    xmlns:xlink="http://www.w3.org/1999/xlink"
                    width="24px"
                    height="24px"
                    viewBox="0 0 24 24"
                    version="1.1"
                  >
                    <g stroke="none" stroke-width="1" fill="none" fill-rule="evenodd">
                      <rect x="0" y="0" width="24" height="24" />
                      <path
                        d="M5,3 L6,3 C6.55228475,3 7,3.44771525 7,4 L7,20 C7,20.5522847 6.55228475,21 6,21 L5,21 C4.44771525,21 4,20.5522847 4,20 L4,4 C4,3.44771525 4.44771525,3 5,3 Z M10,3 L11,3 C11.5522847,3 12,3.44771525 12,4 L12,20 C12,20.5522847 11.5522847,21 11,21 L10,21 C9.44771525,21 9,20.5522847 9,20 L9,4 C9,3.44771525 9.44771525,3 10,3 Z"
                        fill="#000000"
                      />
                      <rect
                        fill="#000000"
                        opacity="0.3"
                        transform="translate(17.825568, 11.945519) rotate(-19.000000) translate(-17.825568, -11.945519)"
                        x="16.3255682"
                        y="2.94551858"
                        width="3"
                        height="18"
                        rx="1"
                      />
                    </g>
                  </svg>
                  <!--end::Svg Icon-->
                </span>
              </span>
              <!--end::Icon-->
              <!--begin::Title-->
              <div class="d-flex flex-column flex-grow-1 mr-2">
                <a
                  href="#"
                  class="font-weight-bold text-dark-75 text-hover-primary font-size-lg mb-1"
                >Group lunch celebration</a>
                <span class="text-muted font-weight-bold">Due in 2 Days</span>
              </div>
              <!--end::Title-->
              <!--begin::Lable-->
              <span class="font-weight-bolder text-warning py-1 font-size-lg">+28%</span>
              <!--end::Lable-->
            </div>
            <!--end::Item-->
            <!--begin::Item-->
            <div class="d-flex align-items-center bg-light-success rounded p-5 mb-9">
              <!--begin::Icon-->
              <span class="svg-icon svg-icon-success mr-5">
                <span class="svg-icon svg-icon-lg">
                  <!--begin::Svg Icon | path:assets/media/svg/icons/Communication/Write.svg-->
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    xmlns:xlink="http://www.w3.org/1999/xlink"
                    width="24px"
                    height="24px"
                    viewBox="0 0 24 24"
                    version="1.1"
                  >
                    <g stroke="none" stroke-width="1" fill="none" fill-rule="evenodd">
                      <rect x="0" y="0" width="24" height="24" />
                      <path
                        d="M12.2674799,18.2323597 L12.0084872,5.45852451 C12.0004303,5.06114792 12.1504154,4.6768183 12.4255037,4.38993949 L15.0030167,1.70195304 L17.5910752,4.40093695 C17.8599071,4.6812911 18.0095067,5.05499603 18.0083938,5.44341307 L17.9718262,18.2062508 C17.9694575,19.0329966 17.2985816,19.701953 16.4718324,19.701953 L13.7671717,19.701953 C12.9505952,19.701953 12.2840328,19.0487684 12.2674799,18.2323597 Z"
                        fill="#000000"
                        fill-rule="nonzero"
                        transform="translate(14.701953, 10.701953) rotate(-135.000000) translate(-14.701953, -10.701953)"
                      />
                      <path
                        d="M12.9,2 C13.4522847,2 13.9,2.44771525 13.9,3 C13.9,3.55228475 13.4522847,4 12.9,4 L6,4 C4.8954305,4 4,4.8954305 4,6 L4,18 C4,19.1045695 4.8954305,20 6,20 L18,20 C19.1045695,20 20,19.1045695 20,18 L20,13 C20,12.4477153 20.4477153,12 21,12 C21.5522847,12 22,12.4477153 22,13 L22,18 C22,20.209139 20.209139,22 18,22 L6,22 C3.790861,22 2,20.209139 2,18 L2,6 C2,3.790861 3.790861,2 6,2 L12.9,2 Z"
                        fill="#000000"
                        fill-rule="nonzero"
                        opacity="0.3"
                      />
                    </g>
                  </svg>
                  <!--end::Svg Icon-->
                </span>
              </span>
              <!--end::Icon-->
              <!--begin::Title-->
              <div class="d-flex flex-column flex-grow-1 mr-2">
                <a
                  href="#"
                  class="font-weight-bold text-dark-75 text-hover-primary font-size-lg mb-1"
                >Home navigation optimization</a>
                <span class="text-muted font-weight-bold">Due in 2 Days</span>
              </div>
              <!--end::Title-->
              <!--begin::Lable-->
              <span class="font-weight-bolder text-success py-1 font-size-lg">+50%</span>
              <!--end::Lable-->
            </div>
            <!--end::Item-->
            <!--begin::Item-->
            <div class="d-flex align-items-center bg-light-danger rounded p-5 mb-9">
              <!--begin::Icon-->
              <span class="svg-icon svg-icon-danger mr-5">
                <span class="svg-icon svg-icon-lg">
                  <!--begin::Svg Icon | path:assets/media/svg/icons/Communication/Group-chat.svg-->
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    xmlns:xlink="http://www.w3.org/1999/xlink"
                    width="24px"
                    height="24px"
                    viewBox="0 0 24 24"
                    version="1.1"
                  >
                    <g stroke="none" stroke-width="1" fill="none" fill-rule="evenodd">
                      <rect x="0" y="0" width="24" height="24" />
                      <path
                        d="M16,15.6315789 L16,12 C16,10.3431458 14.6568542,9 13,9 L6.16183229,9 L6.16183229,5.52631579 C6.16183229,4.13107011 7.29290239,3 8.68814808,3 L20.4776218,3 C21.8728674,3 23.0039375,4.13107011 23.0039375,5.52631579 L23.0039375,13.1052632 L23.0206157,17.786793 C23.0215995,18.0629336 22.7985408,18.2875874 22.5224001,18.2885711 C22.3891754,18.2890457 22.2612702,18.2363324 22.1670655,18.1421277 L19.6565168,15.6315789 L16,15.6315789 Z"
                        fill="#000000"
                      />
                      <path
                        d="M1.98505595,18 L1.98505595,13 C1.98505595,11.8954305 2.88048645,11 3.98505595,11 L11.9850559,11 C13.0896254,11 13.9850559,11.8954305 13.9850559,13 L13.9850559,18 C13.9850559,19.1045695 13.0896254,20 11.9850559,20 L4.10078614,20 L2.85693427,21.1905292 C2.65744295,21.3814685 2.34093638,21.3745358 2.14999706,21.1750444 C2.06092565,21.0819836 2.01120804,20.958136 2.01120804,20.8293182 L2.01120804,18.32426 C1.99400175,18.2187196 1.98505595,18.1104045 1.98505595,18 Z M6.5,14 C6.22385763,14 6,14.2238576 6,14.5 C6,14.7761424 6.22385763,15 6.5,15 L11.5,15 C11.7761424,15 12,14.7761424 12,14.5 C12,14.2238576 11.7761424,14 11.5,14 L6.5,14 Z M9.5,16 C9.22385763,16 9,16.2238576 9,16.5 C9,16.7761424 9.22385763,17 9.5,17 L11.5,17 C11.7761424,17 12,16.7761424 12,16.5 C12,16.2238576 11.7761424,16 11.5,16 L9.5,16 Z"
                        fill="#000000"
                        opacity="0.3"
                      />
                    </g>
                  </svg>
                  <!--end::Svg Icon-->
                </span>
              </span>
              <!--end::Icon-->
              <!--begin::Title-->
              <div class="d-flex flex-column flex-grow-1 mr-2">
                <a
                  href="#"
                  class="font-weight-bold text-dark-75 text-hover-primary font-size-lg mb-1"
                >Rebrand strategy planning</a>
                <span class="text-muted font-weight-bold">Due in 2 Days</span>
              </div>
              <!--end::Title-->
              <!--begin::Lable-->
              <span class="font-weight-bolder text-danger py-1 font-size-lg">-27%</span>
              <!--end::Lable-->
            </div>
            <!--end::Item-->
            <!--begin::Item-->
            <div class="d-flex align-items-center bg-light-info rounded p-5">
              <!--begin::Icon-->
              <span class="svg-icon svg-icon-info mr-5">
                <span class="svg-icon svg-icon-lg">
                  <!--begin::Svg Icon | path:assets/media/svg/icons/General/Attachment2.svg-->
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    xmlns:xlink="http://www.w3.org/1999/xlink"
                    width="24px"
                    height="24px"
                    viewBox="0 0 24 24"
                    version="1.1"
                  >
                    <g stroke="none" stroke-width="1" fill="none" fill-rule="evenodd">
                      <rect x="0" y="0" width="24" height="24" />
                      <path
                        d="M11.7573593,15.2426407 L8.75735931,15.2426407 C8.20507456,15.2426407 7.75735931,15.6903559 7.75735931,16.2426407 C7.75735931,16.7949254 8.20507456,17.2426407 8.75735931,17.2426407 L11.7573593,17.2426407 L11.7573593,18.2426407 C11.7573593,19.3472102 10.8619288,20.2426407 9.75735931,20.2426407 L5.75735931,20.2426407 C4.65278981,20.2426407 3.75735931,19.3472102 3.75735931,18.2426407 L3.75735931,14.2426407 C3.75735931,13.1380712 4.65278981,12.2426407 5.75735931,12.2426407 L9.75735931,12.2426407 C10.8619288,12.2426407 11.7573593,13.1380712 11.7573593,14.2426407 L11.7573593,15.2426407 Z"
                        fill="#000000"
                        opacity="0.3"
                        transform="translate(7.757359, 16.242641) rotate(-45.000000) translate(-7.757359, -16.242641)"
                      />
                      <path
                        d="M12.2426407,8.75735931 L15.2426407,8.75735931 C15.7949254,8.75735931 16.2426407,8.30964406 16.2426407,7.75735931 C16.2426407,7.20507456 15.7949254,6.75735931 15.2426407,6.75735931 L12.2426407,6.75735931 L12.2426407,5.75735931 C12.2426407,4.65278981 13.1380712,3.75735931 14.2426407,3.75735931 L18.2426407,3.75735931 C19.3472102,3.75735931 20.2426407,4.65278981 20.2426407,5.75735931 L20.2426407,9.75735931 C20.2426407,10.8619288 19.3472102,11.7573593 18.2426407,11.7573593 L14.2426407,11.7573593 C13.1380712,11.7573593 12.2426407,10.8619288 12.2426407,9.75735931 L12.2426407,8.75735931 Z"
                        fill="#000000"
                        transform="translate(16.242641, 7.757359) rotate(-45.000000) translate(-16.242641, -7.757359)"
                      />
                      <path
                        d="M5.89339828,3.42893219 C6.44568303,3.42893219 6.89339828,3.87664744 6.89339828,4.42893219 L6.89339828,6.42893219 C6.89339828,6.98121694 6.44568303,7.42893219 5.89339828,7.42893219 C5.34111353,7.42893219 4.89339828,6.98121694 4.89339828,6.42893219 L4.89339828,4.42893219 C4.89339828,3.87664744 5.34111353,3.42893219 5.89339828,3.42893219 Z M11.4289322,5.13603897 C11.8194565,5.52656326 11.8194565,6.15972824 11.4289322,6.55025253 L10.0147186,7.96446609 C9.62419433,8.35499039 8.99102936,8.35499039 8.60050506,7.96446609 C8.20998077,7.5739418 8.20998077,6.94077682 8.60050506,6.55025253 L10.0147186,5.13603897 C10.4052429,4.74551468 11.0384079,4.74551468 11.4289322,5.13603897 Z M0.600505063,5.13603897 C0.991029355,4.74551468 1.62419433,4.74551468 2.01471863,5.13603897 L3.42893219,6.55025253 C3.81945648,6.94077682 3.81945648,7.5739418 3.42893219,7.96446609 C3.0384079,8.35499039 2.40524292,8.35499039 2.01471863,7.96446609 L0.600505063,6.55025253 C0.209980772,6.15972824 0.209980772,5.52656326 0.600505063,5.13603897 Z"
                        fill="#000000"
                        opacity="0.3"
                        transform="translate(6.014719, 5.843146) rotate(-45.000000) translate(-6.014719, -5.843146)"
                      />
                      <path
                        d="M17.9142136,15.4497475 C18.4664983,15.4497475 18.9142136,15.8974627 18.9142136,16.4497475 L18.9142136,18.4497475 C18.9142136,19.0020322 18.4664983,19.4497475 17.9142136,19.4497475 C17.3619288,19.4497475 16.9142136,19.0020322 16.9142136,18.4497475 L16.9142136,16.4497475 C16.9142136,15.8974627 17.3619288,15.4497475 17.9142136,15.4497475 Z M23.4497475,17.1568542 C23.8402718,17.5473785 23.8402718,18.1805435 23.4497475,18.5710678 L22.0355339,19.9852814 C21.6450096,20.3758057 21.0118446,20.3758057 20.6213203,19.9852814 C20.2307961,19.5947571 20.2307961,18.9615921 20.6213203,18.5710678 L22.0355339,17.1568542 C22.4260582,16.76633 23.0592232,16.76633 23.4497475,17.1568542 Z M12.6213203,17.1568542 C13.0118446,16.76633 13.6450096,16.76633 14.0355339,17.1568542 L15.4497475,18.5710678 C15.8402718,18.9615921 15.8402718,19.5947571 15.4497475,19.9852814 C15.0592232,20.3758057 14.4260582,20.3758057 14.0355339,19.9852814 L12.6213203,18.5710678 C12.2307961,18.1805435 12.2307961,17.5473785 12.6213203,17.1568542 Z"
                        fill="#000000"
                        opacity="0.3"
                        transform="translate(18.035534, 17.863961) scale(1, -1) rotate(45.000000) translate(-18.035534, -17.863961)"
                      />
                    </g>
                  </svg>
                  <!--end::Svg Icon-->
                </span>
              </span>
              <!--end::Icon-->
              <!--begin::Title-->
              <div class="d-flex flex-column flex-grow-1 mr-2">
                <a
                  href="#"
                  class="font-weight-bold text-dark-75 text-hover-primary font-size-lg mb-1"
                >Product goals strategy meet-up</a>
                <span class="text-muted font-weight-bold">Due in 2 Days</span>
              </div>
              <!--end::Title-->
              <!--begin::Lable-->
              <span class="font-weight-bolder text-info py-1 font-size-lg">+8%</span>
              <!--end::Lable-->
            </div>
            <!--end::Item-->
          </div>
          <!--end::Body-->
        </div>
        <!--end::List Widget 11-->
      </div>
    </div>
    <!--end::Row-->
  </page-view>
</template>

<script src="./home.ts"></script>
