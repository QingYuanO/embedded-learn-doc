import type { BaseLayoutProps } from 'fumadocs-ui/layouts/shared';
import Image from 'next/image';

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
          <Image src='/logo.png' alt='Logo' width={36} height={36} />
          <span className='bg-[var(--primary)] from-foreground via-rose-200 to-[var(--primary)] bg-clip-text font-semibold text-transparent dark:bg-gradient-to-b '>
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
