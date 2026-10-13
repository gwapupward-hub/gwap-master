# Module: Ionic Framework

**Source:** https://github.com/ionic-team/ionic-framework  
**Reviewed:** 2026-09-29  
**Pinned release:** `v9.0.5`  
**Pinned release commit:** `b86733f289642a2ae27440bef4145a8359153a50`  
**Trust tier:** T1_OFFICIAL  
**License:** MIT  
**Integration pattern:** REFERENCE_ONLY with FUTURE_MOBILE_PILOT trigger  
**GwapOS status:** REFERENCE_ONLY

## Problem It Can Help Solve

Ionic provides a mature cross-platform UI system for building mobile-first interfaces with web technologies. Its strongest value to GwapOS today is as a source of proven patterns for:

- mobile interaction behavior;
- platform-adaptive UI;
- touch targets and gesture-aware controls;
- sheets, modals, popovers, menus, tabs, and navigation transitions;
- theming through CSS variables;
- web-component architecture;
- accessibility behavior;
- responsive mobile layouts;
- PWA/native-shell design thinking;
- automated component and end-to-end testing.

## Current Upstream Snapshot

At the reviewed release:

- `@ionic/core`: `9.0.5`
- `@ionic/react`: `9.0.5`
- `@ionic/react-router`: `9.0.5`
- React peer support: React 18 or 19
- Ionic React Router peer support: React Router `>=6.4.0 <7`
- core implementation: Web Components / Stencil
- license: MIT

The upstream repository is active and maintained.

## GwapOS Decision

**Do not install Ionic Framework into the existing GwapOS Next.js application by default.**

The existing GwapOS public/application shell is already a Next.js architecture. Ionic can be used with React and its documentation references Next.js as compatible tooling, but first-class Next.js SSR / partial pre-rendering support remains an explicit upstream compatibility concern. The official issue requesting first-class Next.js SSR and partial page pre-rendering support remained open at review time.

Therefore:

- treat Ionic as a design/interaction/component-architecture reference today;
- do not replace Next.js App Router with Ionic React Router;
- do not add `@ionic/react-router` merely to gain mobile navigation effects;
- do not convert server-rendered GwapOS pages into client-only Ionic pages without a measured product reason;
- do not import global Ionic CSS into GwapOS until visual and bundle impact is tested in isolation.

## What We Adopt Now

### 1. Mobile interaction patterns

Use Ionic as a reference when GwapOS needs:

- bottom sheets / action sheets;
- mobile-friendly modals;
- menus / drawers;
- segmented controls;
- tabs;
- pull-to-refresh;
- toasts;
- loading and progress indicators;
- mobile-safe form controls;
- touch-first list and card behavior;
- keyboard-aware layouts;
- platform-sensitive spacing and navigation.

Copy the behavior and UX principle when possible, not necessarily the dependency.

### 2. Component API discipline

Prefer component contracts with:

- explicit properties;
- emitted events;
- controlled state;
- accessible semantics;
- platform-independent behavior;
- theme variables/tokens;
- predictable loading/error/disabled states.

### 3. Accessibility and automated testing patterns

Use Ionic's mature component testing approach as reference material for:

- keyboard interaction;
- ARIA synchronization;
- focus behavior;
- overlay behavior;
- viewport/mobile E2E tests;
- Playwright-based interaction tests;
- regression tests around responsive layouts.

Do not assume upstream tests are sufficient for GwapOS-specific accessibility requirements.

### 4. Theming concepts

Ionic's CSS-variable approach is useful as an architecture reference.

For GwapOS:
- preserve the GwapSpot token system and brand colors;
- map mobile components to existing design tokens;
- do not let Ionic defaults become the GwapOS visual identity;
- avoid importing large default theme bundles if a smaller local implementation is sufficient.

## What We Do Not Adopt Automatically

- full Ionic app architecture;
- Ionic CLI as the primary GwapOS build system;
- Ionic Router as the GwapOS router;
- a migration away from Next.js;
- global Ionic styling;
- Ionic-specific page wrappers everywhere;
- Cordova assumptions;
- any Capacitor/native runtime dependency solely because Ionic mentions it;
- upstream dependency versions that conflict with the current GwapOS lockfile/toolchain.

Capacitor is a separate capability and must receive its own repository intake before becoming a GwapOS runtime dependency.

## Next.js Boundary

Before any Ionic runtime dependency is introduced into a Next.js GwapOS surface, verify:

1. current Next.js version;
2. current React version;
3. server/client component boundary;
4. App Router compatibility;
5. hydration behavior;
6. CSS ordering and reset conflicts;
7. bundle-size effect;
8. route/history behavior;
9. wallet-provider behavior;
10. iOS Safari behavior;
11. accessibility;
12. Vercel build/runtime behavior.

The pilot must use an isolated route or package first.

## Future Mobile-App Trigger

Reconsider Ionic as a runtime framework when GwapOS intentionally starts one of these:

- a dedicated iOS/Android GwapOS application;
- a native-shell app around a web experience;
- a mobile-specific application package in a monorepo;
- an offline-first/PWA product requiring richer mobile interaction primitives.

At that point compare at least:

- Ionic React + Capacitor;
- existing Next.js/PWA approach;
- React Native / Expo if native-first requirements justify it;
- direct native implementations if platform-specific functionality dominates.

Do not preselect Ionic before that comparison.

## Pilot Acceptance Criteria

If a runtime pilot is approved, it must prove:

```text
same wallet/auth behavior
same route correctness
no SSR/hydration regressions
no iOS Safari regression
acceptable bundle impact
acceptable Core Web Vitals
GwapSpot design tokens preserved
keyboard/focus/accessibility behavior verified
Vercel preview green
mobile E2E green
rollback is one small PR/revert
```

## Security / Supply-Chain Rules

- use official `@ionic/*` packages only;
- pin the approved major/minor through the normal package manager and lockfile;
- review migration guides before major upgrades;
- do not copy substantial upstream code without preserving MIT attribution requirements;
- do not execute upstream project scripts in GwapOS unless independently reviewed;
- treat Ionic plugins/native integrations as separate dependencies requiring their own review.

## Re-review Triggers

Re-review this module when:

- GwapOS begins a dedicated mobile app;
- Ionic releases a new major version;
- Next.js SSR/partial-rendering compatibility changes materially;
- React Router compatibility changes;
- GwapOS changes its React/Next.js versions;
- Capacitor is proposed for adoption;
- the current GwapOS shell develops a mobile interaction problem that existing components cannot solve cleanly.
