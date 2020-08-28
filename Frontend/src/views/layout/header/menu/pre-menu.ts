import { IMenu } from './model';

export const providedMenu: Array<IMenu> = [
    {
        isVisable: true, name: 'dashboard', route: '#',
        children: [
            { isVisable: true, name: 'attendanceAttendenceDashboard', icon: 'icon-layers', route: 'attendanceAttendenceDashboard' },
            { isVisable: true, name: 'concessionDashboard', icon: 'icon-layers', route: 'concessionDashboard' },
            { isVisable: true, name: 'admissionDashboard', icon: 'icon-layers', route: 'admissionDashboard' },
            { isVisable: true, name: 'revenueDashboard', icon: 'icon-layers', route: 'revenueDashboard' },
            { isVisable: true, name: 'feePaidDashboard', icon: 'icon-layers', route: 'feePaidDashboard' }
        ]
    },
    {
        isVisable: true, name: 'ssetup', route: '#',
        children: [
            {
                isVisable: true, name: 'rsetup', route: '#',
                children: [
                    { isVisable: true, name: 'setupSession', icon: 'icon-layers', route: 'setupSession' },
                    { isVisable: true, name: 'setupCampusProgramLink', icon: 'icon-layers', route: 'setupCampusProgramLink' },
                    { isVisable: true, name: 'registrationProgramCourseLink', icon: 'icon-layers', route: 'registrationProgramCourseLink' },
                    { isVisable: true, name: 'setupBoard', icon: 'icon-layers', route: 'setupBoard' },
                    { isVisable: true, name: 'setupBoardType', icon: 'icon-layers', route: 'setupBoardType' },
                    { isVisable: true, name: 'setupGender', icon: 'icon-layers', route: 'setupGender' },
                    { isVisable: true, name: 'setupMedium', icon: 'icon-layers', route: 'setupMedium' },
                    { isVisable: true, name: 'setupMonth', icon: 'icon-layers', route: 'setupMonth' },
                    { isVisable: true, name: 'setupNationality', icon: 'icon-layers', route: 'setupNationality' },
                    { isVisable: true, name: 'setupReligion', icon: 'icon-layers', route: 'setupReligion' },
                    { isVisable: true, name: 'setupAdmissionType', icon: 'icon-layers', route: 'setupAdmissionType' },
                    { isVisable: true, name: 'setupDegree', icon: 'icon-layers', route: 'setupDegree' },
                    { isVisable: true, name: 'setupGroup', icon: 'icon-layers', route: 'setupGroup' },
                    { isVisable: true, name: 'attendanceAttendenceStatus', icon: 'settings', route: 'attendanceAttendenceStatus' },

                ]
            },
            {
                isVisable: true, name: 'gsetup', route: '#',
                children: [
                    { isVisable: true, name: 'setupBusinessGroup', icon: 'icon-layers', route: 'setupBusinessGroup' },
                    { isVisable: true, name: 'setupBusinessUnit', icon: 'icon-layers', route: 'setupBusinessUnit' },
                    { isVisable: true, name: 'setupInstitution', icon: 'icon-layers', route: 'setupInstitution' },
                    { isVisable: true, name: 'setupCampus', icon: 'icon-layers', route: 'setupCampus' },
                    { isVisable: true, name: 'setupZone', icon: 'icon-layers', route: 'setupZone' },
                    { isVisable: true, name: 'setupCountry', icon: 'icon-layers', route: 'setupCountry' },
                    { isVisable: true, name: 'setupProvince', icon: 'icon-layers', route: 'setupProvince' },
                    { isVisable: true, name: 'setupCity', icon: 'icon-layers', route: 'setupCity' },
                    { isVisable: true, name: 'setupSubCity', icon: 'icon-layers', route: 'setupSubCity' },
                    { isVisable: true, name: 'setupClass', icon: 'icon-layers', route: 'setupClass' },
                    { isVisable: true, name: 'franchise', icon: 'icon-layers', route: 'franchise' },
                    { isVisable: true, name: 'setupInstitutionType', icon: 'icon-layers', route: 'setupInstitutionType' },
                    { isVisable: true, name: 'messageSMSAPIList', icon: 'icon-layers', route: 'messageSMSAPIList' },
                    { isVisable: true, name: 'setupShift', icon: 'icon-layers', route: 'setupShift' },
                    { isVisable: true, name: 'gradingPolicyBulk', icon: 'icon-layers', route: 'gradingPolicyBulk' },
                    { isVisable: true, name: 'failCriteria', icon: 'icon-layers', route: 'failCriteria' },
                    { isVisable: true, name: 'messageTemplate', icon: 'icon-layers', route: 'messageTemplate' }
                ]
            }
        ]
    },
    {
        isVisable: true, name: 'bsetup', route: '#',
        children: [
            { isVisable: true, name: 'admissionEligibilityCriteria', icon: 'icon-layers', route: 'admissionEligibilityCriteria' },
            { isVisable: true, name: 'feeChallanValidity', icon: 'icon-layers', route: 'feeChallanValidity' },
            { isVisable: true, name: 'feeChallanValidityUpdate', icon: 'icon-layers', route: 'feeChallanValidityUpdate' },
            { isVisable: true, name: 'feeCampusBankLink', icon: 'icon-layers', route: 'feeCampusBankLink' },
            { isVisable: true, name: 'setupCollector', icon: 'icon-layers', route: 'setupCollector' },
            { isVisable: true, name: 'setupConcessionRemarks', icon: 'icon-layers', route: 'setupConcessionRemarks' },
            { isVisable: true, name: 'concessionRenew', icon: 'icon-layers', route: 'concessionRenew' },
            { isVisable: true, name: 'campusGradingMapping', icon: 'icon-layers', route: 'campusGradingMapping' },
            { isVisable: true, name: 'campusFailCriteriaMapping', icon: 'icon-layers', route: 'campusFailCriteriaMapping' },
            { isVisable: true, name: 'customSms', icon: 'icon-layers', route: 'customSms' },
            { isVisable: true, name: 'approvesms', icon: 'icon-layers', route: 'smsapproval' },
            { isVisable: true, name: 'KinshipStudent', icon: 'icon-layers', route: 'kinshipstd' },
            { isVisable: true, name: 'ConcessStudent', icon: 'icon-layers', route: 'concessstdd' },
            { isVisable: true, name: 'OnlineFormApproval', icon: 'icon-layers', route: 'onlineFormApproval' },
            { isVisable: true, name: 'BulkScholarship', icon: 'icon-layers', route: 'concesskinsstdd' },

            { isVisable: true, name: 'programTransfer', icon: 'icon-layers', route: 'programTransfer' },
        ]
    }
];