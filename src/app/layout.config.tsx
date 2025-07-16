import type { BaseLayoutProps } from 'fumadocs-ui/layouts/shared';

/**
 * Shared layout configurations
 *
 * you can customise layouts individually from:
 * Home Layout: app/(home)/layout.tsx
 * Docs Layout: app/docs/layout.tsx
 */
export const baseOptions: BaseLayoutProps = {
  nav: {
    title: (
      <>
        <div className='flex items-center justify-center gap-2'>
          <svg width='24' height='24' xmlns='http://www.w3.org/2000/svg' aria-label='Logo'>
            <circle cx={12} cy={12} r={12} fill='currentColor' />
          </svg>
          <span className='bg-primary from-foreground via-rose-200 to-primary bg-clip-text font-semibold text-transparent dark:bg-gradient-to-b '>
            Embedded Learning
          </span>
        </div>
      </>
    ),
    transparentMode: 'top',
  },
  // see https://fumadocs.dev/docs/ui/navigation/links
  links: [],
};
